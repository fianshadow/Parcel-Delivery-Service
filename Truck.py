import datetime

class Truck:
    def __init__(self, number, start_time, capacity=16):
        self.mileage = 0
        self.route = '1'
        self.packageList = []
        self.capacity = capacity
        self.number = number
        self.start_time = start_time
        self.time_value = 0