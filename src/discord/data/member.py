import discord.data.user as user
import discord.utility as u

class Member(user.User):
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

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == 'roles':
                msg += ('    ' * indent) + 'Roles:\r\n'
                for r in self.roles:
                    msg += ('    ' * (indent + 1)) + r.name + '\r\n'
            elif key == 'guild':
                msg += ('    ' * indent) + 'guild: ' + value.name + '\r\n'
            else: 
                msg += ('    ' * indent) + '{} : {}\r\n'.format(key, value)
        return msg
