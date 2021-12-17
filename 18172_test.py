# from slack import slack

# notice = slack()

# notice.slack("TEST POST")

# from DateTime import DateTime

# dt = DateTime()

# print(dt.get_date())
# print(dt.get_time())
# print(dt.get_date_time())

from PowerControl import PowerControl

usb = PowerControl()

while True:
    print("press on or off:")
    s = input()
    if s == "on":
        usb.usb_power_on(17)
    if s == "off":
        usb.usb_power_off()
