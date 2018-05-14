import discord.internals.data as d

class Embed(d.Data):

    def __init__(self):
        self.title = None
        self.type = None
        self.description = None
        self.url = None
        self.timestamp = None
        self.color = None
        self.footer = None
        self.image = None
        self.thumbnail = None
        self.video = None
        self.provider = None
        self.author = None
        self.fields = []

class EmbedThumbnail(d.Data):

    def __init__(self):
        self.url = None
        self.proxy_url = None
        self.height = None
        self.width = None

class EmbedVideo(d.Data):

    def __init__(self):
        self.url = None
        self.height = None
        self.width = None

class EmbedImage(d.Data):

    def __init__(self):
        self.url = None
        self.proxy_url = None
        self.height = None
        self.width = None

class EmbedProvider(d.Data):
    
    def __init__(self):
        self.name = None
        self.url = None

class EmbedAuthor(d.Data):

    def __init__(d.Data):
        self.name = None
        self.url = None
        self.icon_url = None
        self.proxy_icon_url = None

class EmbedFooter(d.Data):

    def __init__(self):
        self.text = None
        self.icon_url = None
        self.proxy_icon_url = None

class EmbedField(d.Data):

    def __init__(self):
        self.name = None
        self.value = None
        self.inline = None