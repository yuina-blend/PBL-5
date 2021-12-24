# from DateTime import DateTime
# from PowerControl import PowerControl
# import time

# date_time = DateTime()
# usb = PowerControl()

# while True:
#     time_now = date_time.get_time().split(':')

#     for i in range(3):
#         time_now[i] = int(time_now[i])
#     print(time_now)
#     if time_now[0] == 14 and time_now[1] >= 40:
#         usb.usb_power_off()
#     time.sleep(10)
# 

import subprocess
from subprocess import PIPE

while True:
    try:
        proc = subprocess.run(['python3', 'app.py'], stdout=PIPE, stderr=PIPE, shell=True)
        print('reset')
    except KeyboardInterrupt:
        import sys
        sys.exit()