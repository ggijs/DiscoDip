
class Invite:
    
    def __init__(self):
        self.code = None
        self.guild = None
        self.channel = None
        self.approximate_presence_count = None
        self.approximate_member_count = None

    def __str__(self, indent = 0):
        msg = ''
        msg += ('    ' * indent) + 'code: ' + str(self.code) + '\r\n'
        msg += ('    ' * indent) + 'approximate_presence_count: ' + str(self.approximate_presence_count) + '\r\n'
        msg += ('    ' * indent) + 'approximate_member_count: ' + str(self.approximate_member_count) + '\r\n'
        msg += ('    ' * indent) + 'Guild:\r\n' + self.guild.__str__(indent + 1) + '\r\n'
        msg += ('    ' * indent) + 'Channel:\r\n' + self.channel.__str__(indent + 1) + '\r\n'
        return msg

class InviteMetadata:
    
    def __init__(self):
        self.inviter = None
        self.uses = None
        self.max_uses = None
        self.max_age = None
        self.temporary = None
        self.created_at = None
        self.revoked = None

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == 'inviter':
                msg += ('    ' * indent) + 'Inviter\r\n'
                msg += value.__str__(indent + 1) + '\r\n'
            else:
                msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)
        return msg