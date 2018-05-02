import discord.data.user as user
import discord.utility as u

class Emoji():

    def __init__(self):
        #Guaranteed
        self.id = None
        self.name = None

        #Optional
        self.roles = None
        self.require_colons = None
        self.managed = None
        self.animated = None
        self.user = None

    def __str__(self, indent = 0):
        msg = ''
        for key,value in self.__dict__.items():
            if key == "user":
                    msg += "user:\r\n"
                if value:
                    msg += self.user.__str__(indent + 1) + '\r\n'
            else:
                msg += ('    ' *indent) + str(key) + " : " + str(value) + '\r\n'
        return msg