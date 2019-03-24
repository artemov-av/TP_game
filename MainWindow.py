import sys
from enum import Enum
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QGraphicsView, QGraphicsScene, QLabel, QGroupBox, QRadioButton

from Game import *
from GameScene import GameScene


class UnitCreatingPanel(QWidget):
	def __init__(self, player):
		super().__init__()
		self.player_ = player
		self.setFixedWidth(200)
		layout = QVBoxLayout()
		self.add_labels(layout)
		self.add_creating_tools(layout)
		layout.addStretch()

	def add_labels(self, layout):
		self.player_lbl_ = QLabel(str(self.player_))
		self.money_lbl_ = QLabel(str(self.player_.get_money()) + " gold")
		layout.addWidget(self.player_lbl_);
		layout.addWidget(self.money_lbl_);
		self.setLayout(layout)

	def add_creating_tools(self, layout):
		self._swordsman_radio_ = QRadioButton("Swordsman")
		self._archer_radio_ = QRadioButton("Archer")
		self._cavalry_radio_ = QRadioButton("Cavalry")
		self._swordsman_radio_.setChecked(True)

		self._creating_tools_group_ = QGroupBox("Create unit:")
		group_layout = QVBoxLayout()
		group_layout.addWidget(self._swordsman_radio_)
		group_layout.addWidget(self._archer_radio_)
		group_layout.addWidget(self._cavalry_radio_)
		self._creating_tools_group_.setLayout(group_layout)

		layout.addWidget(self._creating_tools_group_)


class GameView(QGraphicsView):
	def __init__(self):
		super().__init__()
		self.game_scene_ = GameScene()
		self.setScene(self.game_scene_)
		self.game_scene_.add_map_tiles()


class MainGameWidget(QWidget):
	def __init__(self, french_player, british_player):
		super().__init__()
		self.british_creating_panel_ = UnitCreatingPanel(british_player)
		self.french_creating_panel_ = UnitCreatingPanel(french_player)
		self.game_view_ = GameView()
		layout = QHBoxLayout()
		layout.addWidget(self.british_creating_panel_)
		layout.addWidget(self.game_view_)
		self.setLayout(layout)


class GameWindow(QMainWindow):
	def __init__(self, french_player, british_player):
		super().__init__()
		self._main_widget = MainGameWidget(french_player, british_player)
		self._main_widget.setMinimumSize(700, 700)
		self.setCentralWidget(self._main_widget)
		self.setWindowTitle('rly stupid gama')
		self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = GameWindow(Game().get_french_player(), Game().get_british_player())
    sys.exit(app.exec_())