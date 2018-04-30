import discord.utility as u

class User:

    '''
        Cosntructs the user object
    '''
    def __init__(self, data):
        self.id = data["id"]
        self.username = data["username"]
        self.discriminator = data["discriminator"]
        self.avatar = data["avatar"]
        
        self.bot = u.get_safe(data, "bot")
        self.mfa_enabled = u.get_safe(data, "mfa_enabled")
        self.verified = u.get_safe(data, "verified")
        self.email = u.get_safe(data, "email")
    
    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            msg += ('    ' * indent) + '{} : {}\r\n'.format(key, value)
        return msg
