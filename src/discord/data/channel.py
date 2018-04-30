import discord.utility as u

class chat_channel():
    
    def __init__(self, channel):
        #Guaranteed
        self.id = channel["id"]
        self.type = channel["type"]

        #Optional
        self.guild_id = u.get_safe(channel, "guild_id")
        self.position = u.get_safe(channel, "position")
        self.permission_overwrites = u.get_safe(channel, "permission_overwrites")
        self.name = u.get_safe(channel, "name")
        self.topic = u.get_safe(channel, "topic")
        self.nsfw = u.get_safe(channel, "nsfw")
        self.last_message_id = u.get_safe(channel, "last_message_id")
        self.bitrate = u.get_safe(channel, "bitrate")
        self.user_limit = u.get_safe(channel, "user_limit")
        self.recipients = u.get_safe(channel, "recipients")
        self.icon = u.get_safe(channel, "icon")
        self.owner_id = u.get_safe(channel, "owner_id")
        self.application_id = u.get_safe(channel, "application_id")
        self.parent_id = u.get_safe(channel, "parent_id")
        self.last_pin_timestamp = u.get_safe(channel, "last_pin_timestamp")

