import datetime

class Truck:
    def __init__(self, number, capacity=16):
        self.mileage = 0
        self.route = '1'
        self.packageList = []
        self.capacity = capacity
        self.number = number
        self.time = datetime.time(8, 00)
        self.time_value = 0
