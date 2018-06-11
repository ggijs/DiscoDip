import concurrent.futures
import json
import multiprocessing
import random
import requests
import select
import threading
import time
import websocket

import discord.internals.exception as ex
import discord.internals.msg_builder as msg_builder

class Connection():

    def __init__(self,token):
        self.dispatch = None
        self.sequence = 0
        self.socket = None
        self.token = token
        self.ticks_since_hb = 0
        self.heartbeat_interval = None
        self.heartbeat_response = True
        self.session_id = None
        
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers = 1)
        self.request_lock = threading.Lock()
        
        self.req_url = 'https://discordapp.com/api'
        self.req_header = {
            "Authorization" : "Bot {}".format(self.token),
            "User-Agent" : "DiscoDip (http://wavycolt.com, v0.1)",
            "Content-Type" : "application/json" }

    #########################
    ##      INTERFACE      ##
    #########################

    def connect(self, resume = False):
        url = self._get_connection_url(self.token)["url"]
        self.socket = websocket.WebSocket()
        self.socket.connect('{}/?v=6&encoding=json'.format(url))
        
        # consume hello message
        hello = json.loads(self.socket.recv())
        self.heartbeat_interval = hello["d"]["heartbeat_interval"]
        print('Heartbeat interval: {}ms'.format(self.heartbeat_interval))

        if not resume:
            self._gateway_send(msg_builder.identify(self.token))

    def disconnect(self):
        self._gateway_send(msg_builder.presence('', 'offline', False))
        self.socket.close()

    def dispatch(self, op, t, data):
        raise ex.DiscordException('Dispatch callable was not bound.')

    def update(self):
        self._heartbeat()

        while self._pending_data():
            data = self.socket.recv()
            if data == "":
                print('Received empty string')
            else: 
                self._pre_dispatch(data)

    # API access helpers, throws when rate-limit is exceeded #

    # DELETE
    def delete(self, url, ratelimit = None):
        return self.executor.submit(self.__impl_delete, url, ratelimit)

    def __impl_delete(self, url, ratelimit = None):
        with self.request_lock:
            pass

    # GET
    def get(self, url, ratelimit = None):
        return self.executor.submit(self.__impl_get, url, ratelimit)

    def __impl_get(self, url, ratelimit = None):
        with self.request_lock:
            if ratelimit and not ratelimit.allowed():
                raise ex.DiscordException("Rate limit exceeded for '{}'".format(url))
            
            response = requests.get("{}{}".format(self.req_url, url), headers = self.req_header)
            if ratelimit: ratelimit.update(response.headers)
            return response.text

    # PATCH
    def patch(self, url, ratelimit = None):
        return self.executor.submit(self.__impl_patch, url, ratelimit)

    def __impl_patch(self, url, ratelimit = None):
        with self.request_lock:
            pass

    # POST
    def post(self, url, content, ratelimit = None):
        return self.executor.submit(self.__impl_post, url, content, ratelimit)

    def __impl_post(self, url, content, ratelimit = None):
        with self.request_lock:
            if ratelimit and not ratelimit.allowed():
                raise ex.DiscordException("Rate limit exceeded for '{}'".format(url))

            response = requests.post("{}{}".format(self.req_url, url), headers = self.req_header, data=json.dumps(content))
            if ratelimit: ratelimit.update(response.headers)
            return response.text

    # PUT
    def put(self, url, ratelimit = None):
        return self.executor.submit(self.__impl_put, url, ratelimit)

    def __impl_put(self, url, ratelimit = None):
        with self.request_lock:
            pass

    #########################
    ##      INTERNALS      ##
    #########################
    def _get_connection_url(self, token):
        headers = {"Authorization" : "Bot {}".format(token)}
        response = requests.get("https://discordapp.com/api/gateway/bot", headers=headers)
        response.raise_for_status()
        return json.loads(response.text)

    def _ms_time(self):
        return int(time.time() * 1000)

    def _pre_dispatch(self, event):
        event = json.loads(event)

        if event["s"] and event["s"] > self.sequence:
            self.sequence = event["s"]
        
        if event["op"] == 11:
            print('heartbeat ACK:', event)
            self.heartbeat_response = True
        elif event["op"] == 9:
            self.disconnect()
            print('[Connection]: Invalid session, takin a nap...')
            time.sleep(random.randint(2, 5))
            print('Lets try again!')
            self.connect()
        elif event ["op"] ==  7:
            print('[Connection]: Reconnecting succesfull!')
        else:
            self.dispatch(event["op"], event["t"], event["d"])

    def _heartbeat(self):
        self.ticks_since_hb += 1
        if self.ticks_since_hb * 100 >= self.heartbeat_interval:
            if not self.heartbeat_response:
                self._resume()
            else:
                msg = msg_builder.heartbeat(self.sequence)
                print(msg)
                self._gateway_send(msg)
            
            self.ticks_since_hb = 0
            self.heartbeat_response = False

    def _pending_data(self):
        return select.select([self.socket], [], [], 0)[0]

    def _resume(self):
        self.disconnect()
        self.connect(resume = True)
        self._gateway_send(msg_builder.resume(self.token,self.session_id,self.sequence))
        print('[Connecion]: Attemping to restore session')

    def _gateway_send(self, message):
        self.socket.send(message)