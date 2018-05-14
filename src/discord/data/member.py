import discord.data.user as user
import discord.internals.data as d
import discord.utility as u

class Member(d.Data):
    '''
        Constructs the member object
    '''
    def __init__(self):
        self.user = None
        self.nick = None
        self.roles = []
        self.joined_at = None
        self.deaf = None
        self.mute = None