import time

class Time:

    def kyusui(self):

        i = 0
        power = 0
        num = 6

        print("開始")
        
        for i in range(num): #加湿器の時間分繰り返す
            if i==3: #電源offを10秒ごとに確認、停止したと仮定
                print("停止")
                while 1:  #on...1 off...0
                    print("電源が再びつくまで待つ")
                    time.sleep(10)
                    power += 0.5
                    if power == 1:
                        print("電源ON")
                        break
            
            if i==5: #30分前と仮定
                print("LINEBotへの通知")
            
            time.sleep(10)
            i += 1
            print(f"{i*10}s")

        print("終了")


clsC = Time()
clsC.kyusui()