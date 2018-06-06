import discord.data.activity as activity
import discord.data.attachment as attachment
import discord.data.audit_log as audit_log
import discord.data.channel as channel
import discord.data.connection as connection
import discord.data.embed as embed
import discord.data.emoji as emoji
import discord.data.guild as guild
import discord.data.integration as integration
import discord.data.invite as invite
import discord.data.member as member
import discord.data.message as message
import discord.data.overwrite as overwrite
import discord.data.presence as presence
import discord.data.reaction as reaction
import discord.data.role as role
import discord.data.user as user
import discord.data.voice_state as voice_state
import discord.data.webhook as webhook

'''
    For every toplevel container there is a create and an update function.

    Create generates a new object correctly linked based on dictionary data, and
    returns it. Update merges the data into the current discord state (creating 
    new objects when required.)

    Extra create functions may be present (but not guaranteed).
'''
def _convert_list(discord, func, key, data):
    if key in data:
        return [func(discord, x) for x in data[key]]
    return []

##########################
#        ACTIVITY        #
##########################

def create_activity(discord, data):
    pass

def update_activity(discord, data):
    pass

############################
#        ATTACHMENT        #
############################

def create_attachment(discord, data):
    pass

def update_attachment(discord, data):
    pass
    
###########################
#        AUDIT LOG        #
###########################

def create_audit_log(discord, data):
    pass
    
def update_audit_log(discord, data):
    pass
    
#########################
#        CHANNEL        #
#########################
def create_channel(discord, data):
    data["permission_overwrites"] = _convert_list(discord, create_overwrite, "permission_overwrites", data)
    data["recipients"] = _convert_list(discord, find_user, "recipients", data)

    c = channel.Channel()
    c._update(data)
    return c

def update_channel(discord, data):
    chan = create_channel(discord, data)
    
    if not chan.guild_id:
        if chan.id in discord.dm_channels:
            discord.dm_channels[chan.id]._update(chan)
            return discord.dm_channels[chan.id]
        else:
            discord.dm_channels[chan.id] = chan
            return chan

    #else
    gld = discord.guilds[chan.guild_id]
    gch = gld.get_channel(chan.id)
    gch._update(chan)
    return gch

############################
#        CONNECTION        #
############################

def create_connection(discord, data):
    pass

def update_connection(discord, data):
    pass
    
#######################
#        EMBED        #
#######################

def create_embed(discord, data):
    pass

def update_embed(discord, data):
    pass
    
#######################
#        EMOJI        #
#######################
def create_emoji(discord, guild, data):
    e = emoji.Emoji()

    if "roles" in data:
        data["roles"] = [guild.get_role(rid) for rid in data["roles"]]
    else:
        data["roles"] = []

    e._update(data)
    return e

#######################
#        GUILD        #
#######################
def create_guild(discord, data):
    g = guild.Guild()
    g.roles = [create_role(discord, role) for role in data["roles"]]
    g.emoji = [create_emoji(discord, g, emoji) for emoji in data["emojis"]]
    if "members" in data:
        g.members = [create_member(discord, g, mem) for mem in data["members"]]
        del data["members"]
    
    del data["roles"]
    del data["emojis"]
    
    data["voice_states"] = _convert_list(discord, create_voice_state, "voice_states", data)
    data["channels"] = _convert_list(discord, create_channel, "channels", data)
    data["presences"] = _convert_list(discord, create_presence, "presences", data)

    # voice_states & presences will be parsed into member objects.
    g._update(data)
    return g

def update_guild(discord, data):
    id = data["id"]
    if id in discord.guilds:
        discord.guilds[id]._update(create_guild(discord, data))
        return discord.guilds[id]
    else:
        guild = create_guild(discord, data)
        discord.guilds[guild.id] = guild
        return guild

#############################
#        INTEGRATION        #
#############################

def create_integration(discord, data):
    pass

def update_integration(discord, data):
    pass
    
########################
#        INVITE        #
########################

def create_invite(discord, data):
    pass

def update_invite(discord, data):
    pass

########################
#        MEMBER        #
########################
def create_member(discord, guild, data):
    data["roles"] = [guild.get_role(rol) for rol in data["roles"]]
    data["user"] = find_user(discord, data["user"])
    m = member.Member()
    m._update(data)
    return m
    

def update_member(discord, guild, data):
    pass

#########################
#        MESSAGE        #
#########################

def create_message(discord, data):
    pass

def update_message(discord, data):
    pass

###########################
#        OVERWRITE        #
###########################

def create_overwrite(discord, data):
    pass

def update_overwrite(discord, data):
    pass

##########################
#        PRESENCE        #
##########################
def create_presence(discord, data):
    pass

def update_presence(discord, data):
    pass

######################
#        ROLE        #
######################
def create_role(discord, data):
    pass

def update_role(discord, data):
    pass

##########################
#        REACTION        #
##########################

def create_reaction(discord, data):
    pass

def update_reaction(discord, data):
    pass

######################
#        ROLE        #
######################

def create_role(discord, data):
    r = role.Role()
    r._update(data)
    return r

# Mind! this does not take a role dict, but a 
# role update dict. { guild_id, role }
def update_role(discord, data):
    gld = discord.guild[data["guild_id"]]
    
    new = create_role(data["role"])
    old = gld.get_role(new.id)

    if not old:
        discord.roles.append(new)
        return new
    
    old._update(new)
    return old

######################
#        USER        #
######################
def create_user(discord, data):
    u = user.User()
    u._update(data)
    return u

def update_user(discord, data):
    id = data["id"]
    if id in discord.users:
        discord.users[id]._update(data)
        return discord.users[id]
    else:
        user = create_user(discord, data)
        discord.users[user.id] = user
        return user

def find_user(discord, data):
    id = data["id"]
    if id in discord.users:
        return discord.users[id]
    else:
        return update_user(discord, data)

#############################
#        VOICE STATE        #
#############################
def create_voice_state(discord, data):
    pass

def update_voice_state(discord, data):
    pass

#########################
#        WEBHOOK        #
#########################