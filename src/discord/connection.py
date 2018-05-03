import json
import random
import select
import threading
import time
import websocket

import discord.exception as ex
import discord.utility as utility
import discord.msg_builder as msg_builder

class Connection():

    def __init__(self,token):
        self.dispatch = None
        self.socket_lock = threading.Lock()
        self.sequence = 0
        self.socket = None
        self.token = token
        self.ticks_since_hb = 0
        self.heartbeat_interval = None
        self.heartbeat_response = True
        self.session_id = None

        self.req_header = {
            "Authorization" : "Bot {}".format(self.token),
            "User-Agent" : "DiscoDip (http://wavycolt.com, v0.1)",
            "Content-Type" : "application/json" }

    #########################
    ##      INTERFACE      ##
    #########################

    def connect(self, resume = False):
        url = utility.get_connection_url(self.token)["url"]
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

    #########################
    ##      INTERNALS      ##
    #########################
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

    def _pending_data(self):
        return select.select([self.socket], [], [], 0)[0]

    def _resume(self):
        self.disconnect()
        self.connect(resume = True)
        self._send(msg_builder.resume(self.token,self.session_id,self.sequence))
        print('[Connecion]: Attemping to restore session')

    def _send(self, message):
        with self.socket_lock:
            self.socket.send(message)