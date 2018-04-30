import discord.utility as u

class Role:
    '''
    Constructs the role object based on a discord role object dict.
    '''
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.color = data["color"]
        self.hoist = data["hoist"]
        self.position = data["position"]
        self.permissions = data["permissions"]
        self.managed = data["managed"]
        self.mentionable = data["mentionable"]

    def __str__(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            msg += ('    ' * indent) + '{} : {}\r\n'.format(key, value)
        return msg