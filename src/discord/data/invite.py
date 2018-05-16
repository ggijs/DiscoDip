import discord.internals.data as d

class Invite(d.Data):
    
    def __init__(self):
        self.code = None
        self.guild = None
        self.channel = None
        self.approximate_presence_count = None
        self.approximate_member_count = None

class InviteMetadata(d.Data):
    
    def __init__(self):
        self.inviter = None
        self.uses = None
        self.max_uses = None
        self.max_age = None
        self.temporary = None
        self.created_at = None
        self.revoked = None