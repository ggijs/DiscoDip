import json
import select
import threading
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
        self.heartbeat_response = False
        self.session_id = None

    #########################
    ##      INTERFACE      ##
    #########################

    def connect(self):
        url = utility.get_connection_url(self.token)["url"]
        self.socket = websocket.WebSocket()
        self.socket.connect('{}/?v=6&encoding=json'.format(url))
        
        # consume hello message
        hello = json.loads(self.socket.recv())
        self.heartbeat_interval = hello["d"]["heartbeat_interval"]
        print('Heartbeat interval: {}ms'.format(self.heartbeat_interval))
        
        self._send(msg_builder.identify(self.token))

    def dispatch(self, op, t, data):
        raise ex.DiscordException('Dispatch callable was not bound.')

    def update(self):
        self._heartbeat()

        while self._pending_data():
            self._pre_dispatch(self.socket.recv())

    #########################
    ##      INTERNALS      ##
    #########################
    def _pre_dispatch(self, event):
        event = json.loads(event)

        if event["s"] and event["s"] > self.sequence:
            self.sequence = event["s"]
        if event["op"] == 11:
            self.heartbeat_response = True
        else:
            self.dispatch(event["op"], event["t"], event["d"])

    def _heartbeat(self):
        self.ticks_since_hb += 1
        if self.ticks_since_hb * 100 >= self.heartbeat_interval:
            if not self.heartbeat_response:
                self._resume()
            else:
                msg = {
                    'op': 1,
                    'd':self.sequence
                }
                self._send(json.dumps(msg))
            
            self.ticks_since_hb = 0
            self.heartbeat_response = False

    def _pending_data(self):
        return select.select([self.socket], [], [], 0)[0]

    def _resume(self):
        pass

    def _send(self, message):
        with self.socket_lock:
            self.socket.send(message)