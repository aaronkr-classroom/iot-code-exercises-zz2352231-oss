room_sensors = []

kitchen = RoomSensor("Kitchen", 24.5)
bedroom = RoomSensor("Bedroom", 21.0)
balcony = RoomSensor("Balcony", 18.2)

room_sensors.append(kitchen)
room_sensors.append(bedroom)
room_sensors.append(balcony)

for sensor in room_sensors:
    print(f"위치: {sensor.name}, 현재 값: {sensor.value}")

sensors = [
    {
        "name": "Kitchen",
        "temperature": 31,
        "humidity": 72,
        "light": 180
    },
    {
        "name": "Living Room",
        "temperature": 24,
        "humidity": 45,
        "light": 500
    }
]