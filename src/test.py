#from discord import *
#import logintoken as tokens

#connection = discord.Discord(tokens.get_token())
#connection.connect()

import discord.data.emoji as emoji

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
  "require_colons": 'true',
  "managed": 'false',
  "animated": 'false'
}

flut = emoji.Emoji(eex)
print flut