import discord.internals.data as d

class Reaction(d.Data):

    def __init__(self):
        self.count = None
        self.me = None
        self.emoji = None