import unittest
from datetime import datetime
from car_factory import CarFactory



class SpindlerBatteryTest(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        current_date = today

        car = CarFactory.create_thovex(current_mileage, last_service_mileage,last_service_date, current_date)
        self.assertTrue(car.needs_service())
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        current_date = today

        car = CarFactory.create_thovex(current_mileage, last_service_mileage, last_service_date, current_date)
        self.assertTrue(car.needs_service())
    
class NubbinBatteryTest(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        current_date = today

        car = CarFactory.create_rorschach(current_mileage, last_service_mileage, last_service_date, current_date)
        self.assertTrue(car.needs_service())
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        current_date = today

        car = CarFactory.create_rorschach(current_mileage, last_service_mileage,last_service_date, current_date)
        self.assertTrue(car.needs_service())
    
