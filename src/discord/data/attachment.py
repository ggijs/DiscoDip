import discord.internals.data as d

class Attachment(d.Data):

    def __init__(self, data):
        self._update(data)
