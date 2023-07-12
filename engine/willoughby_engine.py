from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self,last_service_mileage,current_milage):
        self._last_service_mileage=last_service_mileage
        self._current_milage=current_milage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000