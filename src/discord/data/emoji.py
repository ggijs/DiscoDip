import discord.data.user as user
import discord.internals.data as d

class Emoji(d.Data):

    def __init__(self):
        #Guaranteed
        self.id = None
        self.name = None

        #Optional
        self.require_colons = None
        self.managed = None
        self.animated = None
        self.user = None

        self.roles = []