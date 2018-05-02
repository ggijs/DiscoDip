import discord.utility as u

class User:

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
    
    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            msg += ('    ' * indent) + '{} : {}\r\n'.format(key, value)
        return msg