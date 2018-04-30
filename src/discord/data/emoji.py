import json

'''
    Emoji class,

    guaranteed fields:
        - id (snowflake)
        - name (string)
    
    optional fields:
        - roles (array)(whitelisted for these roles)
        - user (user object)(that created emoji)
        - require_colons (bool)
        - managed (bool)
        - animated (bool)
'''
