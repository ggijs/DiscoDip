import json
import requests

def get_connection_url(token):
    headers = {"Authorization" : "Bot {}".format(token)}
    response = requests.get("https://discordapp.com/api/gateway/bot", headers=headers)
    return json.loads(response.text)
