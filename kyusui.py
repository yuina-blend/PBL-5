import time

num = 6
i = 0
power = 0

for i in range(num):
    if i==3:
        print("停止")
        while 1:  #on...1 off...0
            print("電源が再びつくまで待つ")
            time.sleep(10)
            power += 0.5
            if power == 1:
                print("電源ON")
                break

    time.sleep(10)
    i += 1
print("終了")