import PySimpleGUI as gui

from view.keys import Keys
from view.road_view import RoadView
from model.road import Road

class GUIRoadView(RoadView):

    def __init__(self, road: Road, window: gui.Window) -> None:
        self.window = window
        self.road = []
        super().__init__(road)

    def display(self):
        i = 1
        for lane in self.road:
            if i == 7:
                break
            self.window[Keys.keys[i]].update(lane)
            i += 1

        self.window.refresh()

