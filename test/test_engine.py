import unittest
from datetime import datetime
from car_factory import CarFactory



class CapuletEngineTest(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = 0
        current_mileage = 31000
        last_service_mileage = 0
        current_date = today

        car = CarFactory.create_thovex(current_mileage, last_service_mileage,last_service_date, current_date)
        self.assertTrue(car.needs_service())
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date =0
        current_mileage = 2
        last_service_mileage = 0
        current_date = today

        car = CarFactory.create_thovex(current_mileage, last_service_mileage, last_service_date, current_date)
        self.assertTrue(car.needs_service())
    
class WilloughbyEngineTest(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = 0
        current_mileage = 61000
        last_service_mileage = 0
        current_date = today

        car = CarFactory.create_rorschach(current_mileage, last_service_mileage,last_service_date, current_date)
        self.assertTrue(car.needs_service())
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date =0
        current_mileage = 2
        last_service_mileage = 0
        current_date = today

        car = CarFactory.create_rorschach(current_mileage, last_service_mileage, last_service_date, current_date)
        self.assertTrue(car.needs_service())
    
class SternmanEngineTest(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = 0
        warning_light_on =True
        current_date = today

        car = CarFactory.create_palindrome( current_date,last_service_date,warning_light_on)
        self.assertTrue(car.needs_service())
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = 0
        warning_light_on =False
        current_date = today

        car = CarFactory.create_palindrome(current_date,last_service_date,warning_light_on)
        self.assertTrue(car.needs_service())
    
