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

    # game_scene.tile_clicked.connect(controller.tile_clicked)
    # view.unit_changed.connect(controller.changed_unit_type)
    # game.unit_added_in_map.connect(view.update_after_adding_unit)
    # game.turn_changed.connect(view.update_after_turn_change)
    # game.game_phase_changed.connect(view.change_phase)
    # game.unit_added_in_map.connect(game_scene.add_unit_item)
    # view.end_placement_clicked.connect(controller.end_placement_button_clicked)

    sys.exit(app.exec_())
