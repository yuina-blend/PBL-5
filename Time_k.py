from DateTime import DateTime
import time



class Time_k:
    def __init__(self):
        self.start = list()
        self.end = list()

    def kyusui(self):
        t = DateTime()
        self.start = t.get_time()
        self.start = list(map(int, self.start.split(':')))
        print(self.start)
        print(f"{self.start[0]}:{self.start[1]}:{self.start[2]} 開始")

        time.sleep(60)

        self.end = t.get_time()
        self.end = list(map(int, self.end.split(':')))
        print(self.end)
        if self.end[-2] == self.start[-2]+1:
            print(f"{self.end[0]}:{self.end[1]}:{self.end[2]} 終了")