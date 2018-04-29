import json
import discord.events.parser_helpers as ph

switch_dict
{
    'READY'                         : ph.ready_event,
    'CHANNEL_CREATE'                : ph.channel_create_event,
    'CHANNEL_UPDATE'                : ph.channel_update_event,
    'CHANNEL_DELETE'                : ph.channel_delete_event,
    'CHANNEL_PINS_UPDATE'           : ph.channel_pins_update_event,
    'GUILD_CREATE'                  : ph.guild_create_event,
    'GUILD_UPDATE'                  : ph.guild_update,
    'GUILD_DELETE'                  : ph.guild_delete,
    'GUILD_BAN_ADD'                 : ph.guild_ban_add_event,
    'GUILD_BAN_REMOVE'              : ph.guild_ban_remove_event,
    'GUILD_EMOJI_UPDATE'            : ph.guild_emoji_update_event,
    'GUILD_INTEGRATIONS_UPDATE'     : ph.guild_integrations_update_event,
    'GUILD_MEMBER_ADD'              : ph.guild_member_add_event,
    'GUILD_MEMBER_REMOVE'           : ph.guild_member_remove_event,
    'GUILD_MEMBER_UPDATE'           : ph.guild_member_update_event,
    'GUILD_MEMBER_CHUNK'            : ph.guild_member_chunk_event,
    'GUILD_ROLE_CREATE'             : ph.guild_role_create_event,
    'GUILD_ROLE_UPDATE'             : ph.guild_role_update_event,
    'GUILD_ROLE_DELETE'             : ph.guild_role_delete_event,
    'MESSAGE_CREATE'                : ph.message_create_event,
    'MESSAGE_UPDATE'                : ph.message_update_event,
    'MESSAGE_DELETE'                : ph.message_delete_event,
    'MESSAGE_DELETE_BULK'           : ph.message_delete_bulk_event,
    'MESSAGE_REACTION_ADD'          : ph.message_reaction_add_event,
    'MESSAGE_REACTION_REMOVE'       : ph.message_reaction_remove_event,
    'MESSAGE_REACTION_REMOVE_ALL'   : ph.message_reaction_remove_all_event,
    'PRESENCE_UPDATE'               : ph.presence_update_event,
    'TYPING_START'                  : ph.typing_start_event,
    'USER_UPDATE'                   : ph.user_update_event,
    'VOICE_STATE_UPDATE'            : ph.voice_state_update_event,
    'VOICE_SERVER_UPDATE'           : ph.voice_server_update_event,
    'WEBHOOKS_UPDATE'               : ph.webhooks_update_event
}

# dispatch of event parse
def parse_event(event):
    pass

