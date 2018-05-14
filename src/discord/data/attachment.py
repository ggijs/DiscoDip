import discord.internals.data as d

class Attachment(d.Data):

    def __init__(self):
        self.id = None
        self.filename = None
        self.size = None
        self.url = None
        self.proxy_url = None
        self.height = None
        self.width = None
