import discord.internals.data as d

class Integration(d.Data):
    
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

class IntegrationAccount(d.Data):
    
    def __init__(self):
        self.id = None
        self.name = None

class Ban(d.Data):
    
    def __init__(self):
        self.reason = None
        self.user = None