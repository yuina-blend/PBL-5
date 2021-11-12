# from slack import slack

# notice = slack()

# notice.slack("TEST POST")

# from DateTime import DateTime

# dt = DateTime()

# print(dt.get_date())
# print(dt.get_time())
# print(dt.get_date_time())

from PowerControl import PowerControl

print("press enter: ")
enter = input()

power = PowerControl()
power.usb_power_off()