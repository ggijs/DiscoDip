import json

def payload(op, d, s=None, t=None):
    msg = {
      'op': op,
      'd' : d,
      's' : s,
      't' : t
    }
    return json.dumps(msg)
  
def heartbeat(seq_num):
    msg = {
      'op': 1,
      'd' : seq_num
    }
    return json.dumps(msg)
  
def identify(token):
    msg = {
  	'token': token,
      	'properties': {
            '$os': 'raspbian',
            '$browser': 'Alberto',
            '$device': 'DiscoLib'
        },
      	'compress': False,
      	'large_threshold': 250,
      	"presence": {
            "since": None,
            "game": {
            "name": "Hello Kitty's Murderous adventure.",
            "type": 0
            },
            "status": "online",
            "afk": False
        }
        }
    return payload(2, msg)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
