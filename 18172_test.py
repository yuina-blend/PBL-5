# from slack import slack

# notice = slack()

# notice.slack("TEST POST")

# from DateTime import DateTime

# dt = DateTime()

# print(dt.get_date())
# print(dt.get_time())
# print(dt.get_date_time())

from PowerControl import PowerControl
from temphumid import pin
from slack import slack

th_pin = pin(14)
pw = PowerControl()

print("press enter: ")
e = input()

s = th_pin.pinset()
print(s)
# slack.slack(str(th_pin.pin()[0]))
# pw.usb_power_off()