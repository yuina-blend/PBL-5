class Time_k:
    import time
    from DateTime import DateTime
    t = DateTime()
    def __init__(self):
        self.start = self.t.get_time()
        self.start = list(map(int, self.start.split(':')))
        self.now = []
        self.otime = []

    # 現在時刻取得
    def kyusui(self):
        self.now = self.t.get_time()
        self.now = list(map(int, self.now.split(':')))

        f = open('test.txt', 'w')
        start = ''.join(str(self.start))
        f.write('開始時刻 ')
        f.write(start)
        f.write('\n')
        now = ''.join(str(self.now))
        f.write('現在時刻 ')
        f.write(now)
        f.write('\n')
        f.close()

        print(self.now)


    # 稼働時間リセット
    def reset(self):
        for i in range(3):
            self.otime[i] = 0
        self.start = self.t.get_time()
        self.start = list(map(int, self.start.split(':')))
        print("reset")
        print(self.otime)


    # 稼働時間読み込み
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

        f = open('test.txt', 'a')
        otime = ''.join(str(self.otime))
        f.write('稼働時刻 ')
        f.write(otime)
        f.write('\n')
        f.close()

        # 加湿器の稼働時間条件
        if self.otime[1] > 3:
            # 稼働時間内
            return self.otime
        else:
            # 稼働時間外
            return "on"
