class PowerControl:

    usb_on_cmd = ['sudo', 'uhubctl', '-l', '1-1', '-a', 'on']
    usb_off_cmd = ['sudo', 'uhubctl', '-l', '1-1', '-a', 'off']


    def __init__(self):
        pass

    def usb_power_on(self, GPIO_pin):
        import RPi.GPIO as GPIO
        import time
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_pin, GPIO.OUT)
        GPIO.output(GPIO_pin, GPIO.HIGH)
        time.sleep(0.5)
        import subprocess
        subprocess.call(self.usb_on_cmd)
        print("USB Power ON.")
        GPIO.cleanup()

    def usb_power_off(self):
        import subprocess
        subprocess.call(self.usb_off_cmd)
        print("USB Power OFF.")

