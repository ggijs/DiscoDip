import discord.internals.data as d

class Presence(d.Data):

    def __init__(self):
        self.user = None
        self.roles = [] # Dit is een rare value hier, wtf?
        self.game = None
        self.status = None