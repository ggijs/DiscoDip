import json
import requests

import discord.data.channel as channel

def get_channel(discord, channel_id):
    return discord.connection.get("/channel/{}".format(channel_id))

def modify_channel(discord, channel_id, channel_update):
    pass

def delete_channel(discord, channel_id):
    pass

def get_channel_messages(discord, channel_id, query = None, limit = None):
    pass

def get_channel_message(discord, channel_id, message_id):
    pass

def create_message(discord, channel_id, message):
    pass

def create_reaction(discord, channel_id, message_id, emoji):
    pass

def delete_own_reaction(discord, channel_id, message_id, emoji):
    pass

def delete_user_reaction(discord, channel_id, message_id, emoji, user_id):
    pass

def get_reactions(discord, channel_id, message_id, emoji):
    pass

def delete_all_reactions(discord, channel_id, message_id):
    pass

def edit_message(discord,channel_id, message_id, message_update):
    pass

def delete_message(discord, channel_id, message_id):
    pass

def bulk_delete_messages(discord, channel_id, message_ids):
    pass

def edit_channel_permissions(discord, channel_id, overwrite_id, overwrite):
    pass

def get_channel_invites(discord, channel_id):
    pass

def create_channel_invite(discord, channel_id, invite_parameters):
    pass

def delete_channel_permission(discord, channel_id, overwrite_id):
    pass

def trigger_typing_indicator(discord, channel_id):
    pass

def get_pinned_messages(discord, channel_id):
    pass

def add_pinned_channel_message(discord, channel_id, message_id):
    pass
    
def delete_pinned_channel_message(discord, channel_id, message_id):
    pass

def group_dm_add_recipient(discord, channel_id, user_id, access_token):
    pass

def group_dm_remove_recipient(discord, channel_id, user_id):
    pass