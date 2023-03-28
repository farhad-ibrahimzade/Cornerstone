import PySimpleGUI as gui

from view.keys import Keys
from view.game_view import GameView
from view.gui_road_view import GUIRoadView
from model.road import Road

class GUIGameView(GameView):
    def __init__(self, road: Road) -> None:
        self.layout = [[gui.Text('Lane 1: '), gui.Text(key=Keys.keys[1])],
                        [gui.Text('Lane 2: '), gui.Text(key=Keys.keys[2])],
                        [gui.Text('Lane 3: '), gui.Text(key=Keys.keys[3])],
                        [gui.Text('Lane 4: '), gui.Text(key=Keys.keys[4])],
                        [gui.Text('Lane 5: '), gui.Text(key=Keys.keys[5])],
                        [gui.Text('Lane 6: '), gui.Text(key=Keys.keys[6])],
                        [gui.Button("Refresh")],]
        self.window = gui.Window("Road Lane Game", self.layout)
        road_view = GUIRoadView(road, self.window)
        super().__init__(road_view)
    
    def display_winner(self, winner, is_draw: bool):
        pass


    def refresh(self) -> str:
        event, values = self.window.read()
        return event
    
    def end(self):
        self.window.close()