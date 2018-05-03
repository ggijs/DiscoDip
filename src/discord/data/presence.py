

class Presence:

    def __init__(self):
        self.user = None
        self.roles = [] # Dit is een rare value hier, wtf?
        self.game = None
        self.status = None

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == "roles":
                msg += ('    ' * indent) + 'Roles:\r\n'
                for role in value:
                    msg += ('    ' * (indent + 1)) + role + '\r\n'
            elif key == "game":
                msg += ('    ' * indent) + 'game:\r\n'
                if value:
                    msg += value.__str__(indent + 1) + '\r\n'
            else:
                msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)
        return msg