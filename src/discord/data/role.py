import discord.utility as u

class Role:
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

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            msg += ('    ' * indent) + '{} : {}\r\n'.format(key, value)
        return msg
