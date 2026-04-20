 def show_info(self):
        print(f"Sensor: {self.name}")
        print(f"Temperature: {self.temp}")
        print(f"Humidity: {self.hum}")
        print(f"Light: {self.light}")
    def comfort_level(self):
        # Comfortable 조건: 온도가 20~26도 사이 AND 습도가 40~60 사이
        if 20 <= self.temp <= 26 and 40 <= self.hum <= 60:
            return "Comfortable"
        
        elif self.temp >= 30 or self.hum >= 70:
            return "Warning"
      
        else:
            return "Normal"

    if sensor["light"] < 200:
        light_status = "Dark"
    else:
        light_status = "Bright"