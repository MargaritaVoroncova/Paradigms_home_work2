# Мы разрабатываем систему управления ресурсами в офисе. У нас есть несколько комнат, в каждой из которых размещены
# разные устройства (компьютеры, принтеры, лампы и т. д.).
# Каждое устройство имеет следующие характеристики: тип (компьютер, принтер, лампа и т. д.),
# статус (включено или выключено), идентификатор.

class Device:
    def __init__(self, device_type, status, identifier):
        self.device_type = device_type
        self.status = status
        self.identifier = identifier

class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def toggle_device_status(self, device_identifier):
        for device in self.devices:
            if device.identifier == device_identifier:
                device.status = not device.status

    def find_devices_by_type_and_status(self, device_type, status):
        matching_devices = []
        for device in self.devices:
            if device.device_type == device_type and device.status == status:
                matching_devices.append(device)
        return matching_devices

    def get_all_devices(self):
        return self.devices

class Office:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def count_devices_by_type(self):
        device_count = {}
        for room in self.rooms:
            for device in room.devices:
                if device.device_type in device_count:
                    device_count[device.device_type] += 1
                else:
                    device_count[device.device_type] = 1
        return device_count


# Создание устройств
device1 = Device('Computer', True, 'PC001')
device2 = Device('Printer', False, 'Printer001')
device3 = Device('Lamp', True, 'Lamp001')

# Создание комнаты и добавление устройств
room1 = Room('Conference Room')
room1.add_device(device1)
room1.add_device(device2)

room2 = Room('Office')
room2.add_device(device3)

# Создание офиса и добавление комнат
office = Office()
office.add_room(room1)
office.add_room(room2)

# Включение/выключение устройства
room1.toggle_device_status('PC001')

# Поиск устройств по типу и статусу
print(room1.find_devices_by_type_and_status('Computer', True))

# Получение списка устройств в комнате
print(room1.get_all_devices())

# Подсчет устройств по типу в офисе
print(office.count_devices_by_type())