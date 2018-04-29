import json
import discord.utility as u

'''
    This represents a guild that the bot is member of, contains all relevant information for this server (i.e. roles, members, emoji's channels etc...)
'''
class Guild:

    '''
        Constructs the guild object, parsed from a peeled GUILD_CREATE event,
        autofills all optional and not-present data (may be None)
    '''
    def __init__(self, event):
        # Guaranteed values
        self.id = event["id"]
        self.name = event["name"]
        self.icon = event["icon"]
        self.splash = event["splash"]
        self.owner_id = event["owner_id"]
        self.region = event["region"]
        self.afk_timeout = event["afk_timout"]
        self.verification_level = event["verification_level"]
        self.default_message_notifications = event["default_message_notifications"]
        self.explicit_content_filter = event["explicit_content_filter"]
        # PARSE ROLES
        # PARSE EMOJI's
        # PARSE FEATURES
        self.mfa_level = event["mfa_level"]
        self.system_channel_id = event["system_channel_id"]

        # optional values
        self.owner = u.get_safe(event, "owner")
        self.permissions = u.get_safe(event, "permissions")
        self.afk_channel_id = u.get_safe(event, "afk_channel_id")
        self.embed_enabled = u.get_safe(event, "embed_enabled")
        self.embed_channel_id = u.get_safe(event, "embed_channel_id")
        self.application_id = u.get_safe(event, "application_id")
        self.widget_enabled = u.get_safe(event, "widget_enabled")
        self.widget_channel_id = u.get_safe(event, "widget_channel_id")
        self.joined_at = u.get_safe(event, "joined_at")
        self.large = u.get_safe(event, "large")
        self.unavailable = u.get_safe(event, "unavailable")
        self.member_count = u.get_safe(event, "member_count")
        #PARSE VOICE STATES
        #PARSE MEMBERS
        #PARSE CHANNELS
        #PARSE PRESENCES

        def __str__(self):
            return str(self.__dict__)