
class Road:

    def __init__(self, size: int = 6) -> None:
        self.size = size
        self.lanes = []  # underscore indicated the parameter is not used, it is a convention

    def __getitem__(self, index: int):
        return self.lanes[index]
    
    def __setitem__(self, index: int, value: str):
        self.lanes[index] = value

    def addLane(self, value: str):
        self.lanes.append(value)

    def check_full(self):
        return not self.lanes[-1] == ""
           