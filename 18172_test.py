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

th_pin = pin()
pw = PowerControl()

print("press enter: ")
e = input()

slack.slack(th_pin.pin())
pw.usb_power_off()