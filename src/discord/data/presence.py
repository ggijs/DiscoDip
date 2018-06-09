import discord.internals.data as d

class Presence(d.Data):

    def __init__(self, data):
        self.game = Activity(data["game"])
        self.status = data["status"]

class Activity(d.Data):

    def __init__(self, data):
        if not data:
            return

        self.url = None
        self.timestamps = None
        self.application_id = None
        self.details = None
        self.state = None
        self.party = None
        self.assets = None
        self.secrets = None
        self.instance = None
        self.flags = None

        if "timestamps" in data:
            self.timestamps = Timestamp(data["timestamps"])
            del data["timestamps"]
        
        if "party" in data:
            self.party = Party(data["party"])
            del data["party"]

        if "assets" in data:
            self.assets = ActivityAsset(data["assets"])
            del data["assets"]
        
        if "secrets" in data:
            self.secrets = ActivitySecret(data["secrets"])
            del data["secrets"]

        self._update(data)
        

class Timestamp(d.Data):
    
    def __init__(self, data):
        self.start = data.get("start")
        self.end = data.get("end")

class Party(d.Data):
    
    def __init__(self, data):
        self.id = None
        self.size = []

        self._update(data)

class ActivityAsset(d.Data):

    def __init__(self, data):
        self.large_image = data.get("large_image")
        self.large_text = data.get("large_text")
        self.small_image = data.get("small_image")
        self.small_text = data.get("small_text")

class ActivitySecret(d.Data):

    def __init(self, data):
        self.join = data.get("join")
        self.spectate = data.get("spectate")
        self.match = data.get("match")