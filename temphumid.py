import RPi.GPIO as GPIO
import dht11
import time
import datetime
import math

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#class
class pin:
    pin_num = int()
    def __init__(self, pin):
        self.pin = pin_num
    def pinset(self):
        import RPi.GPIO as GPIO
        import dht11
        import time
        import datetime
        import math
        import RPi.GPIO as GPIO

        # initialize GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
        # read data using pin 14
        instance = dht11.DHT11(self.pin_num)

     result = instance.read()
     if result.is_valid():
       print("Last valid input: " + str(datetime.datetime.now()))
       print("Temperature: %d C" % result.temperature)
       print("Humidity: %d %%" % result.humidity)
       return result





