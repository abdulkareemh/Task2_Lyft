from engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self,last_service_mileage,current_milage):
        self._last_service_mileage=last_service_mileage
        self._current_milage=current_milage

    def needs_service(self):
        return self.current_milage - self.last_service_milage > 30000