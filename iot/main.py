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
    lcd.setText("Bienvenido/a")
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
                lcd.setText("Temp: %.1f C" % temperature + "    Humedad: %.1f %%" % humidity)
                time.sleep(4)
        if contador == 0:
            if temperature > 19 or humidity > 70 or gas > 160:
                lcd.setRGB(255,0,0)
                Buzzer.notification()
                contador += 1
                lcd.setText("VENTILADOR ACTIVADO")
                time.sleep(4)
            
            else:
                lcd.setRGB(0,0,255)
                lcd.setText("Temp: %.1f C" % temperature + "    Humedad: %.1f %%" % humidity)
                time.sleep(4)
        else:
            time.sleep(4)
            lcd.setRGB(0,0,255)
            lcd.setText("Temp: %.1f C" % temperature + "    Humedad: %.1f %%" % humidity)
            time.sleep(30)
            contador = 0

if __name__ == '__main__':
	main()

