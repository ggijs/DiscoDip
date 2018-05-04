

class Webhook:

    def __init__(self):
        self.id = None
        self.guild_id = None
        self.channel_id = None
        self.user = None
        self.name = None
        self.avatar = None
        self.token = None

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == 'user' and value:
                msg += ('    ' * indent) + 'User:\r\n'
                msg += value.__str__(indent + 1) + '\r\n'
            else:
                msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)
        return msg