import discord.internals.data as d

import discord.data.attachment as attachment

class Message(d.Data):

    def __init__(self, discord, data):
        self.guild = discord._guild_by_cid(data["channel_id"])
        if self.guild:
            self.channel = self.guild.get_channel(data["channel_id"])
        else:
            self.channel = discord.dm_channels[data["channel_id"]]
        del data["channel_id"]

        self.author = None
        self.nonce = None
        self.webhook_id = None
        self.activity = None
        self.application = None

        self.reactions = []

        if not data.get("webhook_id"):
            self.author = discord._user_by_data(data["author"])
        del data["author"] # vieze edge case fuck dat.

        self.mentions = [None] * len(data["mentions"])
        for it in range(0, len(data["mentions"])):
            self.mentions[it] = discord._user_by_data(data["mentions"][it])
        del data["mentions"]

        self.mention_roles = [None] * len(data["mention_roles"])
        for it in range(0, len(data["mention_roles"])):
            self.mention_roles[it] = guild.get_role(data["mention_roles"][it])
        del data["mention_roles"]

        self.attachments = [None] * len(data["attachments"])
        for it in range(0, len(data["attachments"])):
            self.attachments[it] = attachment.Attachment(data["attachments"][it])
        del data["attachments"]

        #EMBEDS KOMEN LATER
        del data["embeds"]

        if "reactions" in data:
            self.reactions = [None] * len(data["reactions"])
            for it in range(0, len(data["reactions"])):
                self.reactions[it] = channel.Reaction(guild, data["reactions"][it])
            del data["reactions"]

        if "activity" in data:
            self.activity = MessageActivity(data["activity"])
            del data["activity"]

        if "application" in data:
            self.application = MessageApplication(data["application"])
            del data["application"]

        self._update(data)

class MessageActivity(d.Data):

    def __init__(self, data):
        self.type = data["type"]
        self.party_id = data.get("type")
        # Hier kan meer mee maar voor nu fuck it


class MessageApplication(d.Data):

    def __init__(self, data):
        self._update(data)




