import discord.data.user as user
import discord.internals.data as d

class Emoji(d.Data):

    def __init__(self, discord, guild, data):
        #Optional values
        self.roles = []
        self.user = None
        self.require_colons = None
        self.managed = None
        self.animated = None

        if "roles" in data:
            self.roles = [None] * len(data["roles"])
            for it in range(0, len(data["roles"])):
                self.roles[it] = guild.get_role(data["roles"][it]["id"])
            del data["roles"]
        
        if "user" in data:
            self.user = discord._user_by_data(data["user"])
            del data["user"]

        self._update(data)