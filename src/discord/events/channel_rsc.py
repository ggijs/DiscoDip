import json
import requests

def get_channel(connection, channel_id):
    # DO YA THANG
    data = connection.get("/channel/{}".format(channel_id))

#def get(url, header)

#def post(url, whaeva, nog iets meer)
