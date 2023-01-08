import RPi.GPIO as GPIO

GPIO.setup(18, GPIO.IN)

class Button:

    def is_pressed():
        if GPIO.input(18):
            return True
        else:
            return False
    

