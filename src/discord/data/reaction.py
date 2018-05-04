

class Reaction:

    def __init__(self):
        self.count = None
        self.me = None
        self.emoji = None

    def __str__(self):
        msg = ''
        msg += ('    ' * indent) + "{} : {}\r\n".format('count', self.count)
        msg += ('    ' * indent) + "{} : {}\r\n".format('me', self.count)
        msg += ('    ' * indent) + "Emoji:\r\n"
        msg += self.emoji.__str__(indent + 1) + '\r\n'
        return msg