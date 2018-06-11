import discord.internals.data as d
import discord.internals.ratelimit as rl

import discord.data.emoji as emoji

'''
    Some information in the channel data is unlinked
    Because this information may not be directly available for
    the discord client, and barely ever relevant for the users.
    The request functions can however be used to resolve this data.
'''
class Channel(d.Data):
    
    def __init__(self, discord, guild, data):
        self.ratelimit = rl.Ratelimit()
        
        #Optional
        if "guild_id" in data:
            del data["guild_id"]

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
        self.recipients = None
        self.permission_overwrites = []

        if "permission_overwrites" in data:
            self.permission_overwrites = [None] * len(data["permission_overwrites"])
            for it in range(0, len(data["permission_overwrites"])):
                self.permission_overwrites[it] = Overwrite(guild, data["permission_overwrites"][it])
            del data["permission_overwrites"]

        if "recipients" in data:
            self.recipients = [None] * len(data["recipients"])
            for it in range(0, len(data["recipients"])):
                self.recipients[it] = discord._user_by_data(data["recipients"][it])
            del data["recipients"]
        
        self._update(data)

class Overwrite(d.Data):

    def __init__(self, guild, data):
        self._update(data)

class Reaction(d.Data):

    def __init__(self, guild, data):
        self.count = data["count"]
        self.me = data["me"]
        
        if not guild:
            self.emoji = emoji.Emoji(None, None, {"id": None, "name": data["emoji"]["name"]})
        else:
            guild.get_emoji(data["emoji"]["id"])