import json
import requests

def get_connection_url(token):
    headers = {"Authorization" : "Bot {}".format(token)}
    response = requests.get("https://discordapp.com/api/gateway/bot", headers=headers)
    response.raise_for_status()
    return json.loads(response.text)

def get_safe(data, key):
    if key in data:
        return data[key]
    return None