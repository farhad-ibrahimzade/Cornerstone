from abc import ABC, abstractmethod
from model.road import Road

class RoadView(ABC):
    def __init__(self, road: Road) -> None:
        self.road = road

    @abstractmethod
    def display(self):
        pass