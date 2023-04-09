import PySimpleGUI as gui
import tkinter as tk

from view.keys import Keys
from view.game_view import GameView
from view.gui_road_view import GUIRoadView
from model.road import Road
from view.image import Images
from PIL import ImageTk

class GUIGameView(GameView):
    def __init__(self, model) -> None:
        self.window = tk.Tk()
        self.model = model
        self.layout = [tk.Label(text="Welcome to the fix the Road Game")]
        self.images = [tk.Label(image=ImageTk.PhotoImage(Images.start))]
        self.images[0].image = Images.start
        self.pack()
        road_view = GUIRoadView(self.model.road, self.window)
        super().__init__(road_view)
    
    def display_winner(self, winner, is_draw: bool):
        pass

    def update(self,layout, images = None):
        self.clear()
        self.layout = layout
        self.images = images
        self.pack()

    def refresh(self):
        self.window.mainloop()
    
    def end(self):
        self.window.close()

    def pack(self):
        for layout in self.layout:
            layout.pack()

        for image in self.images:
            image.pack()

    def display_road(self):
        images = [tk.Label(image=ImageTk.PhotoImage(Images.car)) for _ in range(6)]
        for i,img in enumerate(images):
            img.image = ImageTk.PhotoImage(Images.car)
            img.grid(row=1, column=i)


        text = [tk.Label(text=self.model.road[i]) for i in range(6)]

        for i,text in enumerate(text):
            text.grid(row=0, column=i)
        self.update(text, images)

    def clear(self):
        for layout in self.layout:
            layout.destroy()