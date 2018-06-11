import discodip as dip
import logintoken as tokens

import discord.module as m
import discord.internals.channel_rsc as crsc

connection = dip.Discodip(tokens.get_token())

class Thing(m.Module):
    
    def __init__(self, discodip):
        self.discodip = discodip

    def guild_created(self, event):
        self.guild = event

    def message_received(self, message):
        print("Module received msg: '{}'".format(message.content))
        
        if message.content == "!ping":
            crsc.create_message(self.discodip, message.channel, "Pong!")

connection.register_module(Thing(connection))
connection.run()