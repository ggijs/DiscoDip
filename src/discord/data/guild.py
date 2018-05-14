import discord.data.channel as channel
import discord.data.emoji as emoji
import discord.data.member as member
import discord.data.role as role
import discord.internals.data as d
import discord.utility as u

'''
    This represents a guild that the bot is member of, contains all relevant information for this server (i.e. roles, members, emoji's channels etc...)
'''
class Guild(d.Data):

    '''
        Constructs the guild object, parsed from a peeled GUILD_CREATE event,
        autofills all optional and not-present data (may be None)
    '''
    def __init__(self):
        # Guaranteed values
        self.id = None
        self.name = None
        self.icon = None
        self.splash = None
        self.owner_id = None
        self.region = None
        self.afk_channel_id = None
        self.afk_timeout = None
        self.verification_level = None
        self.default_message_notifications = None
        self.explicit_content_filter = None
        self.features = None
        self.mfa_level = None
        self.application_id = None
        self.system_channel_id = None

        # Optional values
        self.owner = None
        self.permissions = None
        self.embed_enabled = None
        self.embed_channel_id = None
        self.widget_enabled = None
        self.widget_channel_id = None
        self.joined_at = None
        self.large = None
        self.unavailable = None
        self.member_count = None

        self.roles = {}
        self.emojis = {}
        self.voice_states = {}
        self.members = {}
        self.channels = {}