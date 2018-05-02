

class VoiceState:
    
    def __init__(self):
        self.channel_id = None
        self.user_id = None
        self.session_id = None
        self.deaf = None
        self.mute = None
        self.self_deaf = None
        self.self_mute = None
        self.suppress = None
        
        self.guild_id = None

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.iteritems():
            msg += ('    ' * indent) + "{} : {}\r\n".format(key, value)
        return msg