import time
from serial import Serial

from model.game import Game
from view.gui_game_view import GUIGameView
from controller.game_controller import GameController


ser = None #Serial('COM5', 9800, timeout=1)
time.sleep(2)

model = Game()
view = GUIGameView(model.road)
controller = GameController(model, view, ser)

controller.run_game()