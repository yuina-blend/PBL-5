from DateTime import DateTime
import time

t = DateTime()

class Time_k:
    def __init__(self):
        self.start = t.get_time()
        self.start = list(map(int, self.start.split(':')))
<<<<<<< HEAD
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
=======
        print(self.start)
        print(f"{self.start[0]}:{self.start[1]}:{self.start[2]} 開始")
>>>>>>> fba017156e3ee38fea160ec9da3cf321e36185d0

        if self.otime[2] > 30:
            return self.otime
        else:
            return

<<<<<<< HEAD
        
=======
        self.end = t.get_time()
        self.end = list(map(int, self.end.split(':')))
        print(self.end)
        if self.end[-2] == self.start[-2]+1:
            print(f"{self.end[0]}:{self.end[1]}:{self.end[2]} 終了")
>>>>>>> fba017156e3ee38fea160ec9da3cf321e36185d0
