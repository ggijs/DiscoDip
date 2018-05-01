import json
import select
import threading
import time
import websocket

import discord.connection as connection
import discord.utility as utility
import discord.data.guild as guild
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
            start += self.tickspeed
            if(worktime > self.tickspeed):
                print('Warning! event loop is not keeping up, last update took {}S.'.format(worktime))
                continue
            time.sleep(self.tickspeed - worktime)

    # Subject to change
    def register_module(self, module):
        pass

    ########################
    ##      INTERNALS     ##
    ########################

    def _dispatch(self, op, t, data):
        if op == 0:
            if t == 'GUILD_CREATE':
                gld = guild.Guild(data["d"])
                self.guild[gld.id] = gld

                print('parsed guild named {}'.format(gld.name))
                return
            if t == 'READY':
                self._connection.session_id = data["session_id"]
                
                return
        print('\n', '{}, {}: \r\n{}\r\n'.format(op, t, data))