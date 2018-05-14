import discord.internals.data as d

class Connection(d.Data):

    def __init__(self):
        self.id = None
        self.name = None
        self.type = None
        self.revoked = None
        self.integrations = []