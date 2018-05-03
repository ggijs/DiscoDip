

class Activity:

    def __init__(self):
        self.name = None
        self.type = None
        self.timestamps = []
        
        self.url = None
        self.application_id = None
        self.details = None
        self.state = None
        self.party = None
        self.assets = None

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == "timestamps":
                msg += ('    ' * indent) + "Timestamps:\r\n"
                for it in value:
                    msg += it.__str__(indent + 1) + "\r\n"
            elif key == 'party' and value:
                msg += ('    ' * indent) + "Party:\r\n"
                msg += value.__str__(indent + 1)
            elif key == 'assets' and value:
                msg += ('    ' * indent) + "Assets:\r\n"
                msg += value.__str__(indent + 1)
            else:
                msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)

class Timestamp:
    
    def __init__(self):
        self.start = None
        self.end = None

    def __str__(self, indent = 0):
        msg = ''
        msg += ('    ' * indent) + "{} : {}\r\n".format('start', self.start)
        msg += ('    ' * indent) + "{} : {}\r\n".format('end', self.end)
        return msg

class Party:
    
    def __init__(self):
        self.id = None
        self.size = []

    def __str__(self, indent = 0):
        msg = ''
        msg += ('    ' + indent) + '{} : {}\r\n'.format('id', self.id)
        msg += ('    ' + indent) + '{} : {}\r\n'.format('size', self.id)
        return msg

class ActivityAsset:

    def __init__(self):
        self.large_image = None
        self.large_text = None
        self.small_image = None
        self.small_text = None

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)
        return msg
