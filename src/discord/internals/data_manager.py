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
    pass

def update_channel(discord, data):
    pass

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
def create_emoji(discord, data):
    pass

def update_emoji(discord, data):
    pass

#######################
#        GUILD        #
#######################
def create_guild(discord, data):
    data["roles"] = [create_role(discord, role) for role in data["roles"]]
    data["emojis"] = [create_emoji(discord, emoji) for emoji in data["emojis"]]
    data["voice_states"] = _convert_list(discord, create_voice_state, "voice_states", data)
    data["members"] = _convert_list(discord, create_member, "members", data)
    data["channels"] = _convert_list(discord, create_channel, "channels", data)
    data["presences"] = _convert_list(discord, create_presence, "presences", data)

    g = guild.Guild()
    g._update(data)
    return g

def update_guild(discord, data):
    # TODO: Bind original values  if guild already exists
    guild = create_guild(discord, data)
    guild._print()

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
def create_member(discord, data):
    pass

def update_member(discord, data):
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
    pass
    
def update_role(discord, data):
    pass
    
######################
#        USER        #
######################
def create_user(discord, data):
    pass

def update_user(discord, data):
    pass

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