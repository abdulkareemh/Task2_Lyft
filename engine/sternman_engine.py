from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self,last_service_mileage,current_milage):
        self._last_service_mileage=last_service_mileage
        self._current_milage=current_milage

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False