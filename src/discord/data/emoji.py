import user
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
            msg += ('    ' *indent) + str(key) + " : " + str(value) + '\r\n'

eex = {
  "id": "41771983429993937",
  "name": "LUL",
  "roles": [ "41771983429993000", "41771983429993111" ],
  "user": {
    "username": "Luigi",
    "discriminator": "0002",
    "id": "96008815106887111",
    "avatar": "5500909a3274e1812beb4e8de6631111"
  },
  "require_colons": true,
  "managed": false,
  "animated": false
}

flut = Emoji(eex)
print flut