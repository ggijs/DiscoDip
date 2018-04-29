import json
import select
import time
import websocket

import utility

class Discord:

    def __init__(self, token):
        self.guilds = {}
        self.heartbeat_interval = None
        self.heartbeat_response = False
        self.socket_lock = None
        self.modules = []
        self.sequence = None
        self.socket = None
        self.token = token
        self.ticks_since_hb = 0
        self.tickspeed = 0.1 # every 100ms

    def connect(self):
        url = utility.get_connection_url(self.token)
        self.socket = websocket.Websocket()
        self.socket.connect(f'{url}/?v=6&encoding=json')
        
        # consume hello message
        hello = json.loads(self.socket.recv())
        self.heartbeat_interval = hello["d"]["heartbeat_interval"]
        
        self.event_loop()

    def heartbeat(self):
        self.ticks_since_hb +=1
        if self.ticks_since_hb*100 >= self.heartbeat_interval:
            # TODO: no heart_Ack -> connection error.
            msg = {
            'op': 1,
            'd':self.sequence
            }
            self.send(json.dumps(msg))
            self.tick_since_hb = 0
            self.heartbeat_response = False


    def send(self, message):
        with self.socket_lock:
            self.socket.send(message)

    def dispatch(self, message):
        print('***********************\n***********************')
        print(message)

    def event_loop(self):
        time_start = time.time()

        while True:
            self.heartbeat()

        while self.pending_data():
            self.dispatch(self.socket.recv())

        for m in self.modules:
            m.update()

        worktime = time.time() - start
        start += self.tickspeed
        if(worktime > self.tickspeed):
            print(f'Warning! event loop is not keeping up, last update took {worktime}S.')
            continue
        time.sleep(self.tickspeed - worktime)

    def peel(self, message):
        self.sequence = message["s"]
        return message["d"]

    def pending_data(self):
        return select.select([self.socket], [], [], 0)[0]

    # Subject to change
    def register_module(self, module):
        pass