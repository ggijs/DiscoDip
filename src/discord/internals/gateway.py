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
    Handles (most) gateway events & updates
    Not handled here: Hello, Ready, Resumed, Invalid Session.
'''

def __channel_create(discord, event):
    pass

def __channel_update(discord, event):
    pass

def __channel_delete(discord, event):
    pass

def __channel_pins_update(discord, event):
    pass

def __guild_create(discord, event):
    id = event["id"]
    if id in discord.guilds:
        print("*** WARNING: CREATING ALREADY EXISTING GUILD... ***")

    g = guild.Guild()
    g._load(discord, event)
    discord.guilds["id"] = g
    return g

def __guild_update(discord, event):
    pass

def __guild_delete(discord, event):
    pass

def __guild_ban_add(discord, event):
    pass

def __guild_ban_remove(discord, event):
    pass

def __guild_emojis_update(discord, event):
    pass

def __guild_integrations_update(discord, event):
    pass

def __guild_member_add(discord, event):
    pass

def __guild_member_remove(discord, event):
    pass

def __guild_member_update(discord, event):
    pass

def __guild_members_chunk(discord, event):
    pass

def __guild_role_create(discord, event):
    pass

def __guild_role_update(discord, event):
    pass

def __guild_role_delete(discord, event):
    pass

def __message_create(discord, event):
    pass

def __message_update(discord, event):
    pass

def __message_delete(discord, event):
    pass

def __message_delete_bulk(discord, event):
    pass

def __message_reaction_add(discord, event):
    pass

def __message_reaction_remove(discord, event):
    pass

def __message_reaction_remove_all(discord, event):
    pass

def __presence_update(discord, event):
    pass

def __typing_start(discord, event):
    pass

def __user_update(discord, event):
    pass

def __voice_state_update(discord, event):
    pass

def __voice_server_update(discord, event):
    pass

def __webhooks_update(discord, event):
    pass

'''
    This function dispatches events called over the available functions.
'''

# This dict dispatches the event to the correct function
__switch = \
{
    "GUILD_CREATE" : __guild_create,
}

def __default_action(discord, t):
    print("*** UNMANAGED EVENT TYPE: {} ***".format(t))

def consume(discord, t, data):
    func = __switch.get(t)
    if func:
        return func(discord, data)
    return __default_action(discord, t)