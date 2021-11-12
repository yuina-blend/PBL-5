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
        print("start")
        print(self.start)

        time.sleep(60)

        self.end = t.get_time()
        self.end = list(map(int, self.end.split(':')))
        if self.end[-2] == self.start[-2]+1:
            print(self.end)
            print("end")