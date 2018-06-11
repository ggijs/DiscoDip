import json
import requests

def get_guild(discord, guild): # toss?
    pass

def modify_guild(discord, guild, guild_update):
    pass

def delete_guild(discord, guild):
    pass

def get_guild_channels(discord, guild): # toss?
    pass

def create_guild_channel(discord, guild, channel_params):
    pass

def modify_guild_channel_positions(discord, guild, channel_update):
    pass

def get_guild_member(discord, guild, user_id): # toss?
    pass

def list_guild_members(discord, guild, query_string_params = None):
    pass

def add_guild_member(discord, guild, user_id, acces_token):
    pass

def modify_guild_member(discord, guild, user_id, user_update):
    pass

def modify_current_user_nick(discord, guild, nickname):
    pass

def add_guild_member_role(discord, guild, user_id, role_id):
    pass

def remove_guild_member_role(discord, guild, user_id, role_id):
    pass

def remove_guild_member(discord, guild, user_id):
    pass

def get_guild_bans(discord, guild): # toss?
    pass

def get_guild_ban(discord, guild, user_id): # toss?
    pass

def create_guild_ban(discord, guild, user_id, ban_params):
    pass

def remove_guild_ban(discord, guild, user_id):
    pass

def get_guild_roles(discord, guild): # toss?
    pass

def create_guild_role(discord, guild, role_params = None):
    pass

def modify_guild_role_positions(discord, guild, position_update):
    pass

def modify_guild_role(discord, guild, role_id, role_update):
    pass

def delete_guild_role(discord, guild, role_id):
    pass

def get_guild_prune_count(discord, guild, prune_query): # toss?
    pass

def begin_guild_prune(discord, guild, prune_query):
    pass

def get_guild_voice_regions(discord, guild): # toss?
    pass

def get_guild_invites(discord, guild): # toss?
    pass

def get_guild_integrations(discord, guild): # toss?
    pass

def create_guild_integration(discord, guild, integration_reference):
    pass

def modify_guild_integration(discord, guild, integration_id, integration_update):
    pass

def delete_guild_integration(discord, guild, integration_id):
    pass

def sync_guild_integration(discord, guild, integration_id):
    pass

def get_guild_embed(discord, guild): # toss?
    pass

def modify_guild_embed(discord, guild, guild_embed):
    pass

def get_guild_vanity_url(discord, guild, vanity_code):
    pass