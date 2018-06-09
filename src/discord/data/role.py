import discord.internals.data as d

class Role(d.Data):
    '''
    Constructs the role object based on a discord role object dict.
    '''
    def __init__(self, data):
        self._update(data)