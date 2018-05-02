import discord.utility as u

class Channel():
    
    def __init__(self):
        #Guaranteed
        self.id = None
        self.type = None
        self.permission_overwrites = []
        self.recipients = []

        #Optional
        self.guild_id = None
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


    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == "permission_overwrites":
                msg += ('    ' * indent) + "Permission overwrites:\r\n"
                for it in self.permission_overwrites:
                    msg += it.__str__(indent + 1) + '\r\n'
            elif key == "recipients":
                msg += ('    ' * indent + 1) + "- {}\r\n".format(value.username)
            else:
                msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)
        return msg
