import discord.data.channel as channel
import discord.data.emoji as emoji
import discord.data.member as member
import discord.data.presence as presence
import discord.data.role as role
import discord.data.voice_state as voice_state
import discord.internals.data as d

'''
    This represents a guild that the bot is member of, contains all relevant information for this server (i.e. roles, members, emoji's channels etc...)
'''
class Guild(d.Data):

    '''
        Constructs the guild object, parsed from a peeled GUILD_CREATE event,
        autofills all optional and not-present data (may be None)
    '''
    def __init__(self, discord, data):
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

        # load roles (always)
        self.roles = [None] * len(data["roles"])
        for it in range(0, len(self.roles)):
            self.roles[it] = role.Role(data["roles"][it])
        del data["roles"]

        # manage emojis (always)
        self.emojis = [None] * len(data["emojis"])
        for it in range(0, len(self.emojis)):
            self.emojis[it] = emoji.Emoji(discord, self, data["emojis"][it])
        del data["emojis"]

        # manage features (always)
        self.features = [None] * len(data["features"])
        for it in range(0, len(self.features)):
            self.features[it] = data["features"][it]
        del data["features"]
        
        # manage members (?)
        if "members" in data:
            self.members = [None] * len(data["members"])
            for it in range(0, len(self.members)):
                self.members[it] = member.Member(discord, self, data["members"][it])
            del data["members"]
        # no else, if it isn't here this is an update object
        # and we dont want it to overwrite anyway.
        
        # manage channels (?)
        if "channels" in data:
            self.channels = [None] * len(data["channels"])
            for it in range(0, len(data["channels"])):
                self.channels[it] = channel.Channel(discord, self, data["channels"][it])
            del data["channels"]

        # update voice_states into members (?)
        if "voice_states" in data:
            for vs in data["voice_states"]:
                print("voice state: {}".format(vs))
                uid = vs["user_id"]
                self.get_member(uid).voice_state = voice_state.VoiceState(self, vs)
            del data["voice_states"]
        
        # update presences into members (?)
        if "presences" in data:
            for pr in data["presences"]:
                self.get_member(pr["user"]["id"]).presence = presence.Presence(pr)
            del data["presences"]

        self._update(data)

    def get_channel(self, id):
        for chan in self.channels:
            if chan.id == id:
                return chan
        return None

    def get_emoji(self, id):
        for emo in self.emojis:
            if emo.id == id:
                return emo
        # returns a default emoji object (unlisted default emoji)
        return emoji.Emoji(None, self, {"id": None, "name" : id})
    
    def get_role(self, id):
        for rol in self.roles:
            if rol.id == id:
                return rol
        return None

    def get_member(self, id):
        for mem in self.members:
            if mem.user.id == id:
                return mem
        return None