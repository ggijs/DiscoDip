import time

'''
    This class represents a rate limit, checker & updater by header
'''

class Ratelimit:

    def __init__(self):
        self.rate_reset = int(time.time())
        self.rate_limit = 0

    def allowed(self):
        if self.rate_limit > 0:
            return True
        if self.rate_reset <= int(time.time()):
            return True
        return False

    # Expects requests header
    def update(self, header):
        self.rate_reset = int(header["X-RateLimit-Reset"])
        self.rate_limit = int(header["X-RateLimit-Remaining"])

    def __repr__(self):
        return "Limit / Reset in: {} / {}S".format(self.rate_limit, self.rate_reset - int(time.time()))
    
    def __str__(self):
        return self.__repr__()