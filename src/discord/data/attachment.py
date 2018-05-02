

class Attachment:

    def __init__(self):
        self.id = None
        self.filename = None
        self.size = None
        self.url = None
        self.proxy_url = None
        self.height = None
        self.width = None

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.iteritems():
            msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)
        return msg