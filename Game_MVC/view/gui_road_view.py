import tkinter as tk
from PIL import ImageTk

from view.keys import Keys
from view.road_view import RoadView
from model.road import Road
from view.image import Images

class GUIRoadView(RoadView):

    def __init__(self, road: Road, window) -> None:
        self.window = window
        self.road = []
        super().__init__(road)

    def display(self, road):
        self.road = road
        images = [tk.Label(image=ImageTk.PhotoImage(Images.car)) for i in range(6)]
        for i,img in enumerate(images):
            img.image = ImageTk.PhotoImage(Images.car)
            img.grid(row=1, column=i)


        text = [tk.Label(text=self.road[i]) for i in range(6)]

        for i,text in enumerate(text):
            text.grid(row=0, column=i)

        return images +  text


        

