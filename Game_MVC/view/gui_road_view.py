import PySimpleGUI as gui
import tkinter as tk

from view.keys import Keys
from view.road_view import RoadView
from model.road import Road

class GUIRoadView(RoadView):

    def __init__(self, road: Road, window: gui.Window) -> None:
        self.window = window
        self.road = []
        super().__init__(road)

    def display(self, road):
        self.road = road
        return [tk.Label(text=self.road[i]) for i in range(6)]


        

