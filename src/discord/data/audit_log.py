

class AuditLogObject:
    
    def __init__(self):
        self.webhooks = []
        self.users = []
        self.audit_log_entries = []

    def __str__(self, indent = 0):
        msg = ''
        
        msg += ('    ' * indent) + 'Webhooks:\r\n'
        for it in self.webhooks:
            msg += it.__str__(indent + 1) + "\r\n"
        msg += ('    ' * indent) + 'Users:\r\n'
        for it in self.users:
            msg += it.__str__(indent + 1) + "\r\n"
        msg += ('    ' * indent) + 'Audit log entries:\r\n'
        for it in self.audit_log_entries:
            msg += it.__str__(indent + 1) + "\r\n"

        return msg


class AuditLogEntry:
    
    def __init__(self):
        self.target_id = None
        self.user_id = None
        self.id = None
        self.action_type = None
        
        self.changes = []
        
        self.options = None
        self.reason = None

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == "changes":
                msg += ('    ' * indent) + "Changes:\r\n"
                for it in value:
                    msg += it.__str__(indent + 1) + '\r\n'
            else:
                msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)
        return msg


# TODO: check output 
class AuditEntryInfo:
    
    def __init__(self):
        pass

class AuditLogChange:
    pass