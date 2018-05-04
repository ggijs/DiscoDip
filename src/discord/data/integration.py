

class Integration:
    
    def __init__(self):
        self.id = None
        self.name = None
        self.type = None
        self.enabled = None
        self.syncing = None
        self.role_id = None
        self.expire_behavior = None
        self.expire_grade_period = None
        self.user = None
        self.account = None
        self.synced_at = None

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == "user" or key == 'account':
                msg += value.__str__(indent + 1) + '\r\n'
            else:
                msg += ('    ' * indent) + "{} : {}\r\n".format(key. value)
        return msg

class IntegrationAccount:
    
    def __init__(self):
        self.id = None
        self.name = None

    def __str__(indent = 0):
        msg = ''
        msg += "{}{} : {}\r\n".format(('    ' * indent), 'id', self.id)
        msg += "{}{} : {}\r\n".format(('    ' * indent), 'name', self.name)

class Ban:
    
    def __init__(self):
        self.reason = None
        self.user = None

    def __str__(self, indent = 0):
        msg = ''
        msg += "{}{} : {}\r\n".format(('    ' * indent), 'reason', self.reason)
        msg += ('    ' * indent) + "User:\r\n"
        msg += self.user.__str__(indent + 1) + '\r\n'
        return msg