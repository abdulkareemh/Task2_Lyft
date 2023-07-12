from battery.battery import Battery
from datetime import datetime, timedelta

class NubbinBattery(Battery):
    def __init__(self,last_service_date,current_date):
        self._last_service_date=last_service_date
        self._current_date=current_date
    
    def needs_service(self):
        two_years_delta = timedelta(days=365*4)
        return (self._current_date - self._last_service_date) >= two_years_delta
