
class Overwrite:

    def __init__(self):
        self.id = None
        self.type = None
        self.allow = None
        self.deny = None

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.iteritems():
            msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)
        return msg