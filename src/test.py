import discodip as dip
import logintoken as tokens

import discord.module as m
import discord.internals.channel_rsc as crsc

class Thing(m.Module):
    
    def __init__(self, discodip):
        self.discodip = discodip

    def guild_created(self, event):
        self.guild = event

    def message_received(self, message):
        if message.content == "__output":
            # THIS IS SIN, NEVER DIRECTLY RUN STUFF ON THE EXECUTOR
            # in this case it is hella convenient tho...
            self.discodip._connection.executor.submit(self.guild._print)
            return
        
        if not message.channel.name == "botspam":
            return

        if message.content == "!ping":
            crsc.create_message(self.discodip, message.channel, "Pong!")

connection = dip.Discodip(tokens.get_token())
connection.register_module(Thing(connection))
connection.run()