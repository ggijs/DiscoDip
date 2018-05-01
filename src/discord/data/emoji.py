import discord.data.user as user
import discord.utility as u

class Emoji():

    def __init__(self, emoji):
        #Guaranteed
        self.id = emoji["id"]
        self.name = emoji["name"]

        #Optional
        self.roles = u.get_safe(emoji, "roles")
        self.require_colons = u.get_safe(emoji, "require_colons")
        self.managed = u.get_safe(emoji, "managed")
        self.animated = u.get_safe(emoji, "animated")
        if "user" in emoji.keys():
            self.user = user.User(emoji["user"])
        else:
            self.user = None

    def __str__(self, indent = 0):
        msg = ''
        for key,value in self.__dict__.items():
            if key == "user":
                if value:
                    msg += "user:\r\n"
                    msg += self.user.__str__(indent + 1) + '\r\n'
                else: "user:\r\n"
            else:
                msg += ('    ' *indent) + str(key) + " : " + str(value) + '\r\n'
        return msg