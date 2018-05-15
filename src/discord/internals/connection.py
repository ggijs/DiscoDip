import json
import random
import requests
import select
import threading
import time
import websocket

import discord.exception as ex
import discord.msg_builder as msg_builder

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
        
        # rate limit related stuffs
        self.global_rate_reset = self._ms_time()
        self.channel_rate = 0
        self.channel_rate_reset = self._ms_time()
        self.guilds_rate = 0
        self.guilds_rate_reset = self._ms_time()
        self.webhooks_rate = 0
        self.webhooks_rate_reset = self._ms_time()

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
        url = self.get_connection_url(self.token)["url"]
        self.socket = websocket.WebSocket()
        self.socket.connect('{}/?v=6&encoding=json'.format(url))
        
        # consume hello message
        hello = json.loads(self.socket.recv())
        self.heartbeat_interval = hello["d"]["heartbeat_interval"]
        print('Heartbeat interval: {}ms'.format(self.heartbeat_interval))

        if not resume:
            self._send(msg_builder.identify(self.token))

    def disconnect(self):
        msg_builder.presence('', 'offline', False)
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

    def delete(self, url):
        with self.request_lock:
            pass

    def get(self, url):
        with self.request_lock:
            self._check_ratelimit(url):
            response = requests.get("{}{}".format(self.req_url, url), headers = self.req_header)
            self._parse_response_header(response.headers, url)
            return response.text

    def patch(self, url):
        with self.request_lock:
            pass
    
    def post(self, url):
        with self.request_lock:
            pass

    def put(self, url):
        with self.request_lock:
            pass

    #########################
    ##      INTERNALS      ##
    #########################
     def _get_connection_url(token):
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
        if event["op"] == 9:
            self.disconnect()
            print('[Connection]: Invalid session, takin a nap...')
            time.sleep(random.randint(2, 5))
            print('Lets try again!')
            self.connect()
        if event ["op"] ==  7:
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
                self._send(msg)
            
            self.ticks_since_hb = 0
            self.heartbeat_response = False

    def _parse_response_header(self, header, url):
        if url.startswith("/channel/"):
            self.channel_rate = header["X-RateLimit-Remaining"]
            self.channel_rate_reset = header["X-RateLimit-Reset"]
        
        elif url.startswith("/guilds/"):
            self.guilds_rate = header["X-RateLimit-Remaining"]
            self.guilds_rate_reset = header["X-RateLimit-Reset"]

        elif url.startswith("/webhooks/"):
            self.webhooks_rate = header["X-RateLimit-Remaining"]
            self.webhooks_rate_reset = header["X-RateLimit-Reset"]

    def _pending_data(self):
        return select.select([self.socket], [], [], 0)[0]

    def _resume(self):
        self.disconnect()
        self.connect(resume = True)
        self._send(msg_builder.resume(self.token,self.session_id,self.sequence))
        print('[Connecion]: Attemping to restore session')

    def _send(self, message):
        self.socket.send(message)

    #Expirimental function
    def _within_ratelimit(self, url):
        if url.startswith("/channel/"):
            if self.channel_rate > 0:
                return True
            if self.channel_rate_reset <= self._ms_time():
                return True
            raise ex.DiscordException('Rate limit exceeded (channel path)')
        
        elif url.startswith("/guilds/"):
            if self.guilds_rate > 0:
                return True
            if self.guilds_rate_reset <= self._ms_time():
                return True
            raise ex.DiscordException('Rate limit exceeded (guilds path)')

        elif url.startswith("/webhooks/"):
            if self.webhooks_rate > 0:
                return True
            if self.webhooks_rate_reset <= self._ms_time():
                return True
            raise ex.DiscordException('Rate limit exceeded (webhooks path)')
        return True