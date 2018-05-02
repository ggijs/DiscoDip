

class Message:

    def __init__(self):
        self.id = None
        self.channel = None
        self.author = None
        self.content = None
        self.timestamp = None
        self.edited_timestamp = None
        self.tts = None
        self.mention_everyone = None
        self.pinned = None
        self.type = None

        self.mentions = []
        self.mention_roles = []
        self.attachments = []
        self.embeds = []
        self.reactions = []

        self.nonce = None
        self.webhook_id = None
        self.activity = None
        self.application = None

    #str func geen zin in atm