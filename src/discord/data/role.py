import discord.internals.data as d
import discord.utility as u

class Role(d.Data):
    '''
    Constructs the role object based on a discord role object dict.
    '''
    def __init__(self):
        self.id = None
        self.name = None
        self.color = None
        self.hoist = None
        self.position = None
        self.permissions = None
        self.managed = None
        self.mentionable = None