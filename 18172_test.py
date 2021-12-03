# from slack import slack

# notice = slack()

# notice.slack("TEST POST")

# from DateTime import DateTime

# dt = DateTime()

# print(dt.get_date())
# print(dt.get_time())
# print(dt.get_date_time())

# from PowerControl import PowerControl
from th import pin
from slack import slack

th_pin = pin(14)
temp, humid = th_pin.pinset()
temp = str(temp)
humid = str(humid)
slack = slack()
slack.slack("temp: " + temp + "humid : " + humid)
# pw = PowerControl()

# while True:
#     print("press on or off: ")
#     word = input()
#     if word == "on":
#         pw.usb_power_on()
#     elif word == "off":
#         pw.usb_power_off()
#     else:
#         print("typo")
# pw.usb_power_off()