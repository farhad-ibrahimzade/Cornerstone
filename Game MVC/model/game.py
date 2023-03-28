from model.road import Road

class Game:
    def __init__(self, size: int = 6) -> None:
        self.road = Road(size)
        self.size = size

    def make_move(self, lane: str):
        self.road.addLane(lane)

    def check_finished(self):
        return self.road.check_full()
