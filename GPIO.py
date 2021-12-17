import RPi.GPIO as GPIO
import time

PIN = 17  # ピン番号(BCMの番号)

# GPIOを扱う準備
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:
    # 1秒ごとに点灯/消灯を繰り返す
    while(True):
        GPIO.output(PIN, GPIO.HIGH)

except KeyboardInterrupt:
    # Ctrl+Cで終了した場合、GPIO設定をクリア
    GPIO.cleanup()
