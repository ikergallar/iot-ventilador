from grove.adc import ADC
 
class GasSensor:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()
 
    @property
    def MQ2(self):
        value = self.adc.read(self.channel)
        return value
    
    def getValue(pin:int):
        sensor = GasSensor(pin)        
        return sensor.MQ2
 
 