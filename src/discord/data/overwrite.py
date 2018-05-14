import discord.internals.data as d

class Overwrite(d.Data):

    def __init__(self):
        self.id = None
        self.type = None
        self.allow = None
        self.deny = None