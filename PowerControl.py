class PowerControl:

    usb_on_cmd = ['sudo', 'uhubctl', '-l', '1-1', '-a', 'on']
    usb_off_cmd = ['sudo', 'uhubctl', '-l', '1-1', '-a', 'off']


    def __init__(self):
        pass

    def usb_power_on(self):
        import subprocess
        subprocess.call(self.usb_on_cmd)
        print("USB Power ON.")

    def usb_power_off(self):
        import subprocess
        subprocess.call(self.usb_off_cmd)
        print("USB Power OFF.")
