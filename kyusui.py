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
        print(self.start[-2])
        print(self.start)
        print("開始")

        time.sleep(60)

        self.end = t.get_time()
        self.end = list(map(int, self.end.split(':')))
        print(self.end)
        if self.end[-2] == self.start[-2]+1:
            print("終了")


clsC = Time_k()
clsC.kyusui()