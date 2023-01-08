import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

class Buzzer:

    def on():
        GPIO.output(5, True)
        time.sleep(0.1)

    def off():
        GPIO.output(5, False)
        time.sleep(0.1)

    def notification():
        GPIO.output(5, True)
        time.sleep(0.3)

        GPIO.output(5, False)
        time.sleep(0.1)
    

