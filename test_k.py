from Time_k import Time_k
import time

t = Time_k()
i = 0
while i != 10:
    t.kyusui()
    print("---")
    t.check()
    time.sleep(5)
    if i == 5:
        t.reset()
    i += 1
    