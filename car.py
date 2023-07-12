from abc import ABC, abstractmethod
from servicable import Servicable

class Car(Servicable):
    def __init__(self, engine,battery):
        self._engine = engine
        self._battery = battery

    @abstractmethod
    def needs_service(self):
        return self.engine.need_services() or self.battery.needs_service()