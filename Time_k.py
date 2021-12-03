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
        self.otime = [x1 - x2 for (x1, x2) in zip(self.now, self.start)]
        print(self.otime)
        print(self.otime[2])

        if self.otime[2] > 3:
            return self.otime
        else:
            return "on"
