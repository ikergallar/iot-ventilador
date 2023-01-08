import time
import RPi.GPIO as GPIO
import speech_recognition as sr

recognizer = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(recognizer, GPIO.IN)

class SpeechRecognicer:

    def init():
            input = GPIO.input(recognizer)

            if input == 1:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source)

                try:
                    text = r.recognize_google(audio)
                    print(text)
                    return text
                except:
                    print("Sorry, I could not understand you.")
            else:
                print("No input detected.")