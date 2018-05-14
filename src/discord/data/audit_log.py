import discord.internals.data as d

class AuditLogObject(d.Data):
    
    def __init__(self):
        self.webhooks = []
        self.users = []
        self.audit_log_entries = []

class AuditLogEntry(d.Data):
    
    def __init__(self):
        self.target_id = None
        self.user_id = None
        self.id = None
        self.action_type = None
        
        self.changes = []
        
        self.options = None
        self.reason = None

class AuditEntryInfo(d.Data):
    
    def __init__(self):
        self.delete_member_days = None
        self.members_removed = None
        self.channel_id = None
        self.count = None
        self.id = None
        self.type = None
        self.role_type = None

class AuditLogChange(d.Data):
    
    def __init__(self):
        self.new_value = None
        self.old_value = None
        self.key = None