import discord.data.channel as channel
import discord.data.emoji as emoji
import discord.data.member as member
import discord.data.role as role
import discord.utility as u

'''
    This represents a guild that the bot is member of, contains all relevant information for this server (i.e. roles, members, emoji's channels etc...)
'''
class Guild:

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

    '''
        to_string with indent formatting for debug output.
    '''
    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == 'roles':
                msg += ('    ' * indent) + 'Roles:\r\n'
                for r in self.roles.values():
                    msg += r.__str__(indent + 1) + '\r\n'
            elif key == 'members':
                msg += ('    ' * indent) + 'Members:\r\n'
                for m in self.members.values():
                    msg += m.__str__(indent + 1) + '\r\n'
            elif key == 'channels':
                msg += ('    ' * indent) + 'Channels:\r\n'
                for c in self.channels.values():
                    msg += c.__str__(indent + 1) + '\r\n'
            elif key == 'emojis':
                msg += ('    ' * indent) + 'Emojis:\r\n'
                for e in self.emojis.values():
                    msg += e.__str__(indent + 1) + '\r\n'
            else:
                msg += ('    ' * indent) + '{} : {}\r\n'.format(key, value)
        return msg
