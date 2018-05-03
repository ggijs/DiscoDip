import json

#yay >_>
import discord.data.activity as activity
import discord.data.channel as channel
import discord.data.emoji as emoji
import discord.data.guild as guild
import discord.data.member as member
import discord.data.presence as presence
import discord.data.role as role
import discord.data.user as user
import discord.data.voice_state as voice_state
import discord.utility as u

def update_channel(discord, data):
    pass

def update_emoji(discord, guild, data):
    pass

def update_guild(discord, data):
    gld = discord.guilds.get(data["id"])
    if not gld: #if not set, create and insert
        gld = guild.Guild()
        discord.guilds[data["id"]] = gld

    memb_list = data.pop("members", None)
    role_list = data.pop("roles", None)
    emoj_list = data.pop("emojis", None)
    voic_list = data.pop("voice_states", None)
    chan_list = data.pop("channels", None)

    for key, value in data.items():
        gld.__dict__[key] = value

    if memb_list:
        for it in memb_list: update_member(discord, gld, it)

    if role_list:
        for it in role_list: update_role(gld, it)

    if emoj_list:
        for it in emoj_list: update_emoji(discord, gld, it)

    if voic_list:
        for it in voic_list: update_voice_state(discord, it)

    if chan_list:
        for it in chan_list: update_channel(discord, it)

def update_member(discord, guild, data):
    pass

def update_presence(discord, data):
    pass

def update_role(guild, data):
    rol = guild.roles.get(data["id"])
    if not rol: # if not set, create and insert
        rol = role.Role()
        guild.roles[data["id"]] = rol

    for key, value in data.items():
        rol.__dict__[key] = value

def update_user(discord, data):
    pass

def update_voice_region(discord, data):
    pass

def update_voice_state(discord, data):
    pass