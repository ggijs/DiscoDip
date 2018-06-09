import discord.data.user as user
import discord.internals.data as d

class Member(d.Data):
    '''
        Constructs the member object
    '''
    def __init__(self, discord, guild, data):
        # optional
        self.nick = None

        # external
        self.voice_state = None
        self.presence = None

        self.user = discord._user_by_data(data["user"])
        del data["user"]

        self.roles = [None] * len(data["roles"])
        for it in range(0, len(self.roles)):
            self.roles[it] = guild.get_role(data["roles"][it])
        del data["roles"]

        self._update(data)
        