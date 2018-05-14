import discord.internals.data as d

class VoiceState(d.Data):
    
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