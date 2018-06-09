import discord.internals.data as d

class VoiceState(d.Data):
    
    def __init__(self, guild, data):
        if "guild_id" in data:
            del data["guild_id"]
        del data["user_id"]

        self.channel = guild.get_channel(data["channel_id"])
        del data["channel_id"]

        self._update(data)