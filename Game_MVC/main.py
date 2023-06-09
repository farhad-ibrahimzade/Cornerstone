import time
from serial import Serial

from model.game import Game
from view.gui_game_view import GUIGameView
from controller.game_controller import GameController

ser = Serial('COM6', 9800, timeout=1)
time.sleep(2)

model = Game()
view = GUIGameView(model)
controller = GameController(model, view, ser)

controller.run_game()