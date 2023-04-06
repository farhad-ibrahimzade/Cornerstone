from serial import Serial
import PySimpleGUI as gui

from model.game import Game
from view.game_view import GameView


class GameController:
    def __init__(self, model: Game, view: GameView, ser: Serial) -> None:
        self.model = model
        self.view = view
        self.ser = ser

    def run_game(self):
        game_ended = False
        
        while not game_ended:
            while True:
                lane = self.get_lane()
                if lane == "":
                    # Break when all lanes scanned
                    break
                self.model.make_move(lane)
                game_ended = self.model.check_finished()
                game_ended = self.view.refresh()

            
            #game_ended = self.model.check_finished()
            self.view.refresh()

        self.view.end()

    def get_lane(self):
        return "Test"
        # line = self.ser.readline()
        # if line:
        #     string = line.decode()  # convert the byte string to a unicode string
        #     if string == "Done":
        #         return ""
        #     data = string.split(",")
        #     return data[0]
        
        # else:
        #     self.get_lane()
        