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
import discord.data.voice_region as voice_region
import discord.data.voice_state as voice_state
import discord.utility as u

def update_channel(discord, data):
    pass

def update_emoji(discord, guild, data):
    pass

def update_guild(discord, data):
    guild = discord.guilds.get(data["id"])
    if not guild: #if not set, create and insert
        guild = guild.Guild()
        discord.guilds[data["id"]] = guild

    memb_list = data.pop("members", None)
    role_list = data.pop("roles", None)
    emoj_list = data.pop("emojis", None)
    voic_list = data.pop("voice_states", None)
    chan_list = data.pop("channels", None)

    for key, value in data.iteritems():
        guild.__dict__[key] = value

    if memb_list:
        for it in data["members"]: update_member(discord, guild, it)

    if role_list:
        for it in data["roles"]: update_role(guild, it)

    if emoj_list:
        for it in data["emojis"]: update_emoji(discord, guild, it)

    if voic_list:
        for it in data["voice_states"]: update_voice_state(discord, it)

    if chan_list:
        for it in data["channels"]: update_channel(discord, it)

def update_member(discord, guild, data):
    pass

def update_presence(discord, data):
    pass

def update_role(guild, data):
    role = guild.roles.get(data["id"])
    if not role: # if not set, create and insert
        role = Role()
        guild.roles[data["id"]] = role

    for key, value in data.iteritems():
        role.__dict__[key] = value

def update_user(discord, data):
    pass

def update_voice_region(discord, data):
    pass

def update_voice_state(discord, data):
    pass

# # PARSE EMOJI's
# self.emojis = {}
# for em in event["emojis"]:
#     obj = emoji.Emoji(em)
#     self.emojis[obj.id] = obj

# # PARSE FEATURES

# self.mfa_level = event["mfa_level"]
# self.system_channel_id = event["system_channel_id"]

# # optional values
# self.owner = u.get_safe(event, "owner")
# self.permissions = u.get_safe(event, "permissions")
# self.afk_channel_id = u.get_safe(event, "afk_channel_id")
# self.embed_enabled = u.get_safe(event, "embed_enabled")
# self.embed_channel_id = u.get_safe(event, "embed_channel_id")
# self.application_id = u.get_safe(event, "application_id")
# self.widget_enabled = u.get_safe(event, "widget_enabled")
# self.widget_channel_id = u.get_safe(event, "widget_channel_id")
# self.joined_at = u.get_safe(event, "joined_at")
# self.large = u.get_safe(event, "large")
# self.unavailable = u.get_safe(event, "unavailable")
# self.member_count = u.get_safe(event, "member_count")

# #PARSE VOICE STATES

# #PARSE MEMBERS
# self.members = {}
# memlist = u.get_safe(event, "members")
# if(memlist):
#     for mem in memlist:
#         obj = member.Member(mem, self)
#         self.members[obj.id] = obj

# #PARSE CHANNELS
# self.channels = {}
# chanlist = u.get_safe(event, "channels")
# if(chanlist):
#     for chan in chanlist:
#         obj = channel.Channel(chan)
#         self.channels[obj.id] = obj

# #PARSE PRESENCES