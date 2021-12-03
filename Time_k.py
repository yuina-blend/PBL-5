class Time_k:
    import time
    from DateTime import DateTime
    t = DateTime()
    def __init__(self):
        self.start = self.t.get_time()
        self.start = list(map(int, self.start.split(':')))
        self.now = list()
        self.otime = list()

    def kyusui(self):
        self.now = self.t.get_time()
        self.now = list(map(int, self.now.split(':')))

        print(self.now)

    def check(self):
        if self.now[2] < self.start[2]:
            self.now[2] += 60
            self.otime[2] = self.now[2] - self.start[2]
            self.now[1] -= 1
            if self.now[1] < self.start[1]:
                self.now[1] += 60
                self.otime[1] = self.now[1] - self.start[1]
                self.now[0] -= 1
                self.otime[0] = self.now[0] - self.start[0]
            else:
                self.otime[1] = self.now[1] - self.start[1]
                self.otime[0] = self.now[0] - self.start[0]

        elif self.now[1] < self.start[1]:
            self.now[1] += 60
            self.otime[1] = self.now[1] - self.start[1]
            self.now[0] -= 1
            self.otime[0] = self.now[0] - self.start[0]

        else:
            self.otime = [x1 - x2 for (x1, x2) in zip(self.now, self.start)]
            
        print(self.otime)
        print(self.otime[2])

        if self.otime[1] > 3:
            return self.otime
        else:
            return "on"
