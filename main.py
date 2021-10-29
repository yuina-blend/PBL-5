from DateTime import DateTime
from PowerControl import PowerControl
import time

date_time = DateTime()
usb = PowerControl()
time = date_time.get_time().split(':')

for i in range(3):
    time[i] = int(time[i])

while True:
    if time[0] == 14 and time[1] >= 25:
        usb.usb_power_off()
    time.sleep(30)