import RPi.GPIO as GPIO
import time
import Adafruit_DHT
from lcd import LCD
from gas_sensor import GasSensor
from buzzer import Buzzer
from speech_recognizer import SpeechRecognicer
from button import Button

sensor = Adafruit_DHT.DHT11
lcd = LCD()
gas_sensor = GasSensor
GPIO.setwarnings(False)

def main():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, 24)
    gas = gas_sensor.getValue(0)
    lcd.setRGB(200,255,255)
    lcd.setText("Bienvenido a nuestra demo")
    time.sleep(3)

    contador = 0

    while True:
        if Button.is_pressed():
            if SpeechRecognicer.init() == "gas":
                lcd.setText('Gas value: {0}'.format(gas))
                lcd.setRGB(0,255,0)
                time.sleep(4)
            if SpeechRecognicer.init() == "temperatura" or "humedad":
                lcd.setRGB(0,0,255)
		lcd.setText("Temperatura: %.1f C" % temperature + "Humedad: %.1f %%" % humidity)
                time.sleep(4)
        if contador == 0:
            if temperature > 21 or humidity > 70 or gas > 160:
                lcd.setRGB(255,0,0)
                Buzzer.notification()
                contador += 1
                lcd.setText("VENTILADOR ACTIVADO")
                time.sleep(4)
            
            else:
                time.sleep(10)
                lcd.setRGB(0,0,255)
                lcd.setText("Temperatura: %.1f C" % temperature + "Humedad: %.1f %%" % humidity)
                time.sleep(4)

def read_dht_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, 24)

    if humidity is not None and temperature is not None:
        return print("Temperatura: %.1f C" % temperature)
        return print("Humedad: %.1f %%" % humidity)
        

    else:
        print("Failed to read from the sensor")


def read_gas():
    print('Gas value: {0}'.format(gas_sensor.getValue(0)))

def speech_recognizer():

    print(SpeechRecognicer.init())

def show_menu():
    # Display the menu
    print("1. Show temperature and humidity")
    print("2. Show gas concentration")
    print("3. Transcribe speech")
    print("4. Quit")

    # Get the user's selection
    selection = int(input("Enter your selection: "))

    # Call the appropriate function based on the selection
    if selection == 1:
        read_dht_sensor()
    elif selection == 2:
        read_gas()
    elif selection == 3:
        speech_recognizer()
    elif selection == 4:
        return
    else:
        print("Invalid selection")


if __name__ == '__main__':
	main()
