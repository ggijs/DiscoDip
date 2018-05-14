import discord.internals.data as d

class Webhook(d.Data):

    def __init__(self):
        self.id = None
        self.guild_id = None
        self.channel_id = None
        self.user = None
        self.name = None
        self.avatar = None
        self.token = None