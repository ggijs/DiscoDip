import discord.internals.data as d

class Channel(d.Data):
    
    def __init__(self):
        #Guaranteed
        self.id = None
        self.type = None
        self.permission_overwrites = []
        self.recipients = []

        #Optional
        self.guild_id = None
        self.position = None
        self.name = None
        self.topic = None
        self.nsfw = None
        self.last_message_id = None
        self.bitrate = None
        self.user_limit = None
        self.owner_id = None
        self.application_id = None
        self.parent_id = None
        self.last_pin_timestamp = None
