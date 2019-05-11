from PyQt5.QtWidgets import QApplication
import sys

from Game import Game
from GameView import GameView
from UnitCreatingController import UnitCreatingController
from ControllerManager import ControllerManager

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    controller = UnitCreatingController()
    view = GameView()

    controller_manager = ControllerManager()
    controller_manager.set_game_model(game)
    controller_manager.set_game_view(view)
    controller_manager.connect_game_and_view()
    controller_manager.change_controller()

    sys.exit(app.exec_())
