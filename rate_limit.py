import time

class RateLimit:

    def __init__(self, rps_limit):
        self.rps_limit = rps_limit
        self.requests = []

    def check(self): 
        self.requests.append(time.time())
        if len(self.requests) <= self.rps_limit:
            return True 
        elif time.time() > self.requests[-self.rps_limit-1] + 10:       
            self.requests = self.requests[-self.rps_limit:]
            return True
        else:
            self.requests = self.requests[-self.rps_limit:]
            return False
