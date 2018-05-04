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
            "name": "HuniePop",
            "type": 0
            },
            "status": "online",
            "afk": False
        }
    }
    return payload(2, msg)
    
def resume(token, session_id, sequence_num):
    msg = {
        "token" : token,
        "session_id" : session_id,
        "seq" : sequence_num
    }
    return payload(6, msg)
    
    
def presence(game, status, afk):
    msg = {
        "since" : None,
        "game" : {
            "name" : game,
            "type" : 0
        },
        "status" : status,
        "afk" : afk
    }
    return payload(3, msg)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
