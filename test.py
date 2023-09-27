import RPi.GPIO as GPIO
import time

Led = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(Led, GPIO.OUT)

while True:

    GPIO.output(Led, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(Led, GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()