class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        # Initializing the four variables through the constructor
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

class SmartSensor:
    def __init__(self, name, temp, hum, light):
        self.name = name
        self.temp = temp
        self.hum = hum
        self.light = light