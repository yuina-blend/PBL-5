from DateTime import DateTime
import time

t = DateTime()

class Time_k:
    def __init__(self):
        self.start = t.get_time()
        self.start = list(map(int, self.start.split(':')))
        self.now = list()
        self.otime = list()

    def kyusui(self):
        self.now = t.get_time()
        self.now = list(map(int, self.now.split(':')))

        print(self.now)

    def check(self):
        self.otime = [x1 - x2 for (x1, x2) in zip(self.now, self.start)]
        print(self.otime)
        print(self.otime[2])

        if self.otime[2] > 30:
            return self.otime
        else:
            return
