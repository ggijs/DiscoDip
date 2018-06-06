import discord.internals.exception as ex
'''
Data baseclass

Contains methods for merging data into this class, and debug printing.
'''

class Data:

    def _print(self, indent = 0):
        for key, val in self.__dict__.items():
            self.__printer(key, val, indent)
        print("\r\n")

    def __printer(self, key, value, indent = 0):
        if key:
            print("{}{}: ".format(indent * " ", key), end="")
        else:
            print(indent * " ", end="")
       
        if isinstance(value, Data):
            print()
            value._print(indent + 4)
        elif isinstance(value, list):
            if len(value) > 0 and not isinstance(value[0], Data): print()
            for v in value:
                if isinstance(v, Data):
                    self.__printer(None, v, indent)
                else:
                    self.__printer(None, v, indent + 4)
            if not len(value) == 0: print()
        else:
            print("{}".format(value))

    def _update(self, data):
        if isinstance(data, dict):    
            for key, value in data.items():
                self.__dict__[key] = value
            return
        if isinstance(data, Data):
            for key, value in data.__dict__.items():
                self.__dict__[key] = value
            return
        raise ex.DiscordException("Attempted to update on non-dict, non-Data")

    def _load(self, discord, data, extra = None):
        self._update(data)