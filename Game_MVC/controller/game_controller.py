from serial import Serial
import tkinter as tk
from view.image import Images

from model.game import Game
from view.gui_game_view import GUIGameView
from PIL import ImageTk

class GameController:
    def __init__(self, model: Game, view,  ser: Serial) -> None:
        self.model = model
        self.view = view
        self.ser = ser

    def run_game(self):
        self.view.update([tk.Label(text="Welcome to the fix the Road Game"),
                       tk.Label(image=ImageTk.PhotoImage(Images.start)),
                        tk.Button(self.view.window, text="Done Scanning", command = lambda: self.update_road())])
        game_ended = False
        self.view.refresh()
        # while not game_ended:
        #     while True:
        #         lane = self.get_lane()
        #         if lane == "":
        #             # Break when all lanes scanned
        #             break
        #         self.model.make_move(lane)
        #         game_ended = self.model.check_finished()
        #         game_ended = self.view.refresh()

            
        #     #game_ended = self.model.check_finished()
        #     self.view.refresh()

        # self.view.end()

    def update_road(self):
        while True:
            lane = self.get_lane()
            if lane == "":
                break
            self.model.make_move(lane)

        self.view.display_road()

        
    
    def get_lane(self):
        line = self.ser.readline()
        string = line.decode()  # convert the byte string to a unicode string
        string = string[:-2]
        if string == "Done":
            return ""
        data = string.split(",")
        return data[0]
        