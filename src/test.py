import discodip as dip
import logintoken as tokens

import discord.module as m
import discord.internals.channel_rsc as crsc

connection = dip.Discodip(tokens.get_token())

class Thing(m.Module):
    
    def __init__(self, discodip):
        self.discodip = discodip

    def message_received(self, message):
        print("Module received msg: '{}'".format(message.content))
        
        if message.content == "!ping":
            crsc.create_message(self.discodip, message.channel_id, "Pong!")


connection.modules.append(Thing(connection))
connection.run()