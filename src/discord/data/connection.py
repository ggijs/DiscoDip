
class Connection:

    def __init__(self):
        self.id = None
        self.name = None
        self.type = None
        self.revoked = None
        self.integrations = []

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == 'integrations':
                msg += ('    ' * indent) + "Integrations:\r\n"
                for it in value:
                    msg += it.__str__(indent + 1) + '\r\n'
            else:
                msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)
        return msg