import json
import requests

import discord.data.channel as channel

def get_channel(discord, channel): # toss?
    return discord._connection.get("/channels/{}".format(channel))

def modify_channel(discord, channel, channel_update):
    pass

def delete_channel(discord, channel):
    pass

def get_channel_messages(discord, channel, query = None, limit = None):
    pass

def get_channel_message(discord, channel, message_id): # toss?
    pass

def create_message(discord, channel, message):
    msg = {"content": message}
    discord._connection.post("/channels/{}/messages".format(channel.id), msg, channel.ratelimit)

def create_reaction(discord, channel, message_id, emoji):
    pass

def delete_own_reaction(discord, channel, message_id, emoji):
    pass

def delete_user_reaction(discord, channel, message_id, emoji, user_id):
    pass

def get_reactions(discord, channel, message_id, emoji):
    pass

def delete_all_reactions(discord, channel, message_id):
    pass

def edit_message(discord,channel, message_id, message_update):
    pass

def delete_message(discord, channel, message_id):
    pass

def bulk_delete_messages(discord, channel, message_ids):
    pass

def edit_channel_permissions(discord, channel, overwrite_id, overwrite):
    pass

def get_channel_invites(discord, channel): # toss?
    pass

def create_channel_invite(discord, channel, invite_parameters):
    pass

def delete_channel_permission(discord, channel, overwrite_id):
    pass

def trigger_typing_indicator(discord, channel):
    pass

def get_pinned_messages(discord, channel): 
    pass

def add_pinned_channel_message(discord, channel, message_id):
    pass
    
def delete_pinned_channel_message(discord, channel, message_id):
    pass

def group_dm_add_recipient(discord, channel, user_id, access_token):
    pass

def group_dm_remove_recipient(discord, channel, user_id):
    pass