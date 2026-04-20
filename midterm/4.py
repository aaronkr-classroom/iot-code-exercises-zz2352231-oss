for sensor in sensors:
    if sensor["temperature"] > 30 or sensor["humidity"] > 70:
        comfort_level = "Warning"
    else:
        comfort_level = "Good"

    if sensor["light"] < 200:
        light_status = "Dark"
    else:
        light_status = "Bright"

    print(f"Sensor: {sensor['name']}")
    print(f"Temperature: {sensor['temperature']}")
    print(f"Humidity: {sensor['humidity']}")
    print(f"Light: {sensor['light']}")
    print(f"Comfort Level: {comfort_level}")
    print(f"Light Status: {light_status}")
    print("-" * 20)  # Separator for readability