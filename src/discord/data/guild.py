import discord.data.channel as channel
import discord.data.emoji as emoji
import discord.data.member as member
import discord.data.role as role
import discord.internals.data as d

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

        self.roles = []
        self.emojis = []
        self.features = []
        #self.voice_states = [] #
        self.members = []
        self.channels = []
        #self.presences = [] #

    # Loads guild info from the data map.
    def _load(self, discord, data, extra = None):
        # load roles
        self.roles = [None] * len(data["roles"])
        for it in range(0, len(data["roles"])):
            self.roles[it] = role.Role()
            self.roles[it]._load(discord, data["roles"][it])

        # manage emojis
        self.emojis = [None] * len(data["emojis"])
        for it in range(0, len(data["emojis"])):
            self.emojis[it] = emoji.Emoji()
            self.emojis[it]._load(discord, data["emojis"][it], self)

        # manage features
        # manage members
        # manage channels

        # update voice_states into members
        # update presences into members

        del data["roles"]
        del data["emojis"]
        del data["features"]
        del data["members"]
        del data["voice_states"]
        del data["presences"]
        del data["channels"]

        self._update(data)

    def get_channel(self, id):
        for chan in self.channels:
            if chan.id == id:
                return chan
        return None

    def get_emoji(self, id):
        pass
    
    def get_role(self, id):
        for rol in self.roles:
            if rol.id == id:
                return rol
        return None

    def get_member(self, id):
        pass