import discord.data.user as user
import discord.utility as u

class Member(user.User):
    '''
        Constructs the member object
    '''
    def __init__(self, data, guild):
        super().__init__(data["user"])
        self.guild = guild
        self.nickname = u.get_safe(data, "nick")
        
        # PARSE ROLES
        self.roles = []
        for r in data["roles"]:
            self.roles.append(self.guild.get_role(r))

        self.joined_at = data["joined_at"]
        self.deaf = data["deaf"]
        self.mute = data["mute"]

    def to_string(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == 'roles':
                msg += ('    ' * indent) + 'Roles:\r\n'
                for r in self.roles:
                    msg += ('    ' * (indent + 1)) + r.name + '\r\n'
            else: 
                msg += ('    ' * indent) + '{} : {}\r\n'.format(key, value)
        return msg
