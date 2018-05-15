'''
Data baseclass

Contains methods for merging data into this class, and debug printing.
'''

class Data:

    def _print(indent = 0):
        for key, val in self.__dict__.items():
            __printer(key, val, indent)
        print("\r\n")

    def __printer(key, value, indent = 0):
        if key:
            print("{}{}: ".format(indent * " ", key))
        else:
            print(indent * " ")
        
        if isinstance(value, Data):
            print("\r\n")
            value._print(indent + 1)
        elif isinstance(value, list):
            print("\r\n")
            for v in value:
                __printer(None, v, indent + 1)
                print("\r\n")
        elif isinstance(value, dict):
            print("\r\n")
            for k, v in value:
                __printer(k, v, indent + 1)
        else:
            print("{}\r\n".format(value))

    def _merge(data):
        for key, value in self.data.items():
            self.__dict__[key] = value