'''
Data baseclass

Contains methods for merging data into this class, and debug printing.
'''

class Data:

    def _print(indent = 0):
        for key, val in self.__dict__.items():
            __printer(key, val, ind)
        print("\r\n")

    def __printer(key, value, indent = 0):
        if key:
            print("{}{}: ".format(indent * " ", key))
        else:
            print(indent * " ")
        
        if isinstance(value, Data):
            value._print(indent + 1)
        elif isinstance(value, list):
            for value in list:
                __printer(None, value, indent + 1)
        else:
            print("{}\r\n".format(value))

    def _merge(data):
        for key, value in self.data.items():
            self.__dict__[key] = value