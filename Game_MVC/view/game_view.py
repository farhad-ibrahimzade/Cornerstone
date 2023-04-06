from abc import ABC, abstractmethod
from view.road_view import RoadView

class GameView(ABC):
    def __init__(self, road_view: RoadView) -> None:
        self.road_view = road_view

    @abstractmethod
    def refresh(self):
        pass

    def display_road(self):
        self.road_view.display()

    @abstractmethod
    def display_winner(self):
        pass

    @abstractmethod
    def end(self):
        pass