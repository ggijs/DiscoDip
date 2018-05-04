import json
import requests

def get_channel(connection, channel_id):
    # DO YA THANG
    r = requests('iets', header = connection.req_header)

def modify_channel(connection, channel_id, channel_update):
    pass

def delete_channel(connection, channel_id):
    pass

def get_channel_messages(connection, channel_id, query = None, limit = None):
    pass

def get_channel_message(connection, channel_id, message_id):
    pass

def create_message(connection, channel_id, message):
    pass

def create_reaction(connection, channel_id, message_id, emoji):
    pass

def delete_own_reaction(connection, channel_id, message_id, emoji):
    pass

def delete_user_reaction(connection, channel_id, message_id, emoji, user_id):
    pass


