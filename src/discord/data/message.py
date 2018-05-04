

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

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == 'mentions':
                msg += ('    ' * indent) + 'Mentions:\r\n'
                for it in value:
                    msg += value.__str__(indent + 1) + '\r\n'
            elif key == 'mention_roles':
                msg += ('    ' * indent) + 'Mention roles:\r\n'
                for it in value:
                    msg += value.__str__(indent + 1) + '\r\n'
            elif key == 'attachments':
                msg += ('    ' * indent) + 'Attachments:\r\n'
                for it in value:
                    msg += value.__str__(indent + 1) + '\r\n'
            elif key == 'embeds':
                msg += ('    ' * indent) + 'Embeds:\r\n'
                for it in value:
                    msg += value.__str__(indent + 1) + '\r\n'
            elif key == 'reactions':
                msg += ('    ' * indent) + 'Reactions:\r\n'
                for it in value:
                    msg += value.__str__(indent + 1) + '\r\n'
            elif key == 'author':
                msg += ('    ' * indent) + 'Author:\r\n'
                msg += value.__str__(indent + 1) + '\r\n'
            elif key == 'activity':
                msg += ('    ' * indent) + 'Activity:\r\n'
                msg += value.__str__(indent + 1) + '\r\n'
            elif key == 'application':
                msg += ('    ' * indent) + 'Application:\r\n'
                msg += value.__str__(indent + 1) + '\r\n'
            else:
                msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)
        return msg