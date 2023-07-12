from abc import ABC, abstractmethod

class Engine(ABC):
    def need_services(self):
        pass