import discord.internals.data as d

class Activity(d.Data):

    def __init__(self):
        self.name = None
        self.type = None
        self.timestamps = []
        
        self.url = None
        self.application_id = None
        self.details = None
        self.state = None
        self.party = None
        self.assets = None

class Timestamp(d.Data):
    
    def __init__(self):
        self.start = None
        self.end = None

class Party(d.Data):
    
    def __init__(self):
        self.id = None
        self.size = []

class ActivityAsset(d.Data):

    def __init__(self):
        self.large_image = None
        self.large_text = None
        self.small_image = None
        self.small_text = None