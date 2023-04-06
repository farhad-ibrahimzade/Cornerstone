import PySimpleGUI as gui
import tkinter as tk

from view.keys import Keys
from view.game_view import GameView
from view.gui_road_view import GUIRoadView
from model.road import Road
from PIL import ImageTk, Image

class GUIGameView(GameView):
    def __init__(self, road: Road) -> None:
        self.window = tk.Tk()
        self.road = road
        img = ImageTk.PhotoImage(Image.open("Images\city.png").resize((500,500)))
        self.layout = [tk.Label(text="Welcome to the fix the Road Game"),
                       tk.Label(image=img),
                        tk.Button(self.window, text="Done Scanning", command = lambda: self.display_road())]
        
        self.layout[1].image = img
        self.pack()
        road_view = GUIRoadView(road, self.window)
        super().__init__(road_view)
    
    def display_winner(self, winner, is_draw: bool):
        pass

    def refresh(self):
        self.window.mainloop()
    
    def end(self):
        self.window.close()

    def pack(self):
        for layout in self.layout:
            layout.pack()

    def display_road(self):
        self.clear()
        self.layout = self.road_view.display(["test" for i in range(6)])
        self.pack()

    def clear(self):
        for layout in self.layout:
            layout.destroy()