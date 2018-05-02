import json
import select
import threading
import time
import websocket

import discord.connection as connection
import discord.utility as utility
import discord.data.guild as guild
import discord.data.manager as manager
import discord.msg_builder as msg_builder

class Discord:

    def __init__(self, token):
        self.guilds = {}
        self.users = {}
        self.modules = {}
        self.dm_channels = {}
        self._tickspeed = 0.1 # every 100ms
        self._connection = connection.Connection(token)
        self._connection.dispatch = self._dispatch

    ########################
    ##      INTERFACE     ##
    ########################

    def run(self):
        self._connection.connect()
        start = time.time()

        while True:
            self._connection.update()

            for m in self.modules:
                m.update()

            worktime = time.time() - start
            start += self._tickspeed
            if(worktime > self._tickspeed):
                print('Warning! event loop is not keeping up, last update took {}S.'.format(worktime))
                continue
            time.sleep(self._tickspeed - worktime)

    # Subject to change
    def register_module(self, module):
        pass

    ########################
    ##      INTERNALS     ##
    ########################

    def _dispatch(self, op, t, data):
        if op == 0:
            if t == 'GUILD_CREATE':
                manager.update_guild(self, data)

                
                
                return
            if t == 'READY':
                self._connection.session_id = data["session_id"]
                return

        print('\n', '{}, {}: \r\n{}\r\n'.format(op, t, data))