import discord.internals.data as d
import discord.utility as u

class User(d.Data):

    '''
        Cosntructs the user object
    '''
    def __init__(self, data):
        self.id = None
        self.username = None
        self.discriminator = None
        self.avatar = None
        
        self.bot = None
        self.mfa_enabled = None
        self.verified = None
        self.email = None