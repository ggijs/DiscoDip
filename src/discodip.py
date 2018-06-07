import json
import select
import signal
import threading
import time
import websocket

import discord.internals.connection as connection
import discord.data.guild as guild
import discord.data.user as user
import discord.internals.gateway as gateway
import discord.internals.msg_builder as msg_builder

class Discodip:

    def __init__(self, token):
        self.guilds = {}
        self.users = {}
        self.modules = {}
        self.dm_channels = {}
        self._running = True
        self._tickspeed = 0.1 # every 100ms
        self._connection = connection.Connection(token)
        self._connection.dispatch = self._dispatch
        signal.signal(signal.SIGINT, self._ctrlc_handler)

        #debug
        self.ticker = 0
        self.runstart = time.time()

    ########################
    ##      INTERFACE     ##
    ########################

    def run(self):
        self._connection.connect()
        start = time.time()

        while self._running:
            self._connection.update()

            for m in self.modules:
                m.update()

            worktime = time.time() - start
            start += self._tickspeed
            if(worktime > self._tickspeed):
                print('Warning! event loop is not keeping up, last update took {}S.'.format(worktime))
                continue
            time.sleep(self._tickspeed - worktime)

            #debug
            self.ticker += 1
            if(self.ticker > 9000):
                self.ticker = 0
                print('** Uptime: {} **'.format(str(datetime.timedelta(seconds=(time.time() - self.runstart)))))
                
        
        self._connection.disconnect()
        # optional cleanup

    # Subject to change
    def register_module(self, module):
        pass

    ########################
    ##      INTERNALS     ##
    ########################

    def _dispatch(self, op, t, data):
        if op == 0:
            if t == 'READY':
                self._connection.session_id = data["session_id"]
                return
            elif t == 'GUILD_CREATE':
                print('received guild_create')
                guild = gateway.consume(self, t, data)
                guild._print()
                print('Guild stuff complete')
            else:
                print(gateway.consume(self, t, data))
                print('\n', '{}, {}: \r\n{}\r\n'.format(op, t, data))

    def _ctrlc_handler(self, signal, frame):
        self._running = False



    # Returns user handle, registers user if it is
    # not registered yet.
    def _user_by_data(self, data):
        id = data["id"]
        if id in self.users:
            return self.users[id]
        
        u = user.User()
        u._load(data)
        self.users[id] = u
        return u
        