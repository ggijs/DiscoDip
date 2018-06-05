import json
import requests

def get_guild(discord, guild_id):
    pass

def modify_guild(discord, guild_id, guild_update):
    pass

def delete_guild(discord, guild_id):
    pass

def get_guild_channels(discord, guild_id):
    pass

def create_guild_channel(discord, guild_id, channel_params):
    pass

def modify_guild_channel_positions(discord, guild_id, channel_update):
    pass

def get_guild_member(discord, guild_id, user_id):
    pass

def list_guild_members(discord, guild_id, query_string_params = None):
    pass

def add_guild_member(discord, guild_id, user_id, acces_token):
    pass

def modify_guild_member(discord, guild_id, user_id, user_update):
    pass

def modify_current_user_nick(discord, guild_id, nickname):
    pass

def add_guild_member_role(discord, guild_id, user_id, role_id):
    pass

def remove_guild_member_role(discord, guild_id, user_id, role_id):
    pass

def remove_guild_member(discord, guild_id, user_id):
    pass

def get_guild_bans(discord, guild_id):
    pass

def get_guild_ban(discord, guild_id, user_id):
    pass

def create_guild_ban(discord, guild_id, user_id, ban_params):
    pass

def remove_guild_ban(discord, guild_id, user_id):
    pass

def get_guild_roles(discord, guild_id):
    pass

def create_guild_role(discord, guild_id, role_params = None):
    pass

def modify_guild_role_positions(discord, guild_id, position_update):
    pass

def modify_guild_role(discord, guild_id, role_id, role_update):
    pass

def delete_guild_role(discord, guild_id, role_id):
    pass

def get_guild_prune_count(discord, guild_id, prune_query):
    pass

def begin_guild_prune(discord, guild_id, prune_query):
    pass

def get_guild_voice_regions(discord, guild_id):
    pass

def get_guild_invites(discord, guild_id):
    pass

def get_guild_integrations(discord, guild_id):
    pass

def create_guild_integration(discord, guild_id, integration_reference):
    pass

def modify_guild_integration(discord, guild_id, integration_id, integration_update):
    pass

def delete_guild_integration(discord, guild_id, integration_id):
    pass

def sync_guild_integration(discord, guild_id, integration_id):
    pass

def get_guild_embed(discord, guild_id):
    pass

def modify_guild_embed(discord, guild_id, guild_embed):
    pass

def get_guild_vanity_url(discord, guild_id, vanity_code):
    pass