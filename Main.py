from PyQt5.QtWidgets import QApplication
import sys

from Game import Game
from GameView import GameView
from GameScene import GameScene
from UnitCreatingController import UnitCreatingController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game_scene = GameScene()
    controller = UnitCreatingController()
    game.set_scene(game_scene)

    view = GameView()
    view.set_scene(game_scene)

    game_scene.tile_clicked.connect(controller.tile_clicked)
    view.unit_changed.connect(controller.changed_unit_type)
    game.unit_added_in_map.connect(view.update_after_adding_unit)
    game.turn_changed.connect(view.update_after_turn_change)

    sys.exit(app.exec_())