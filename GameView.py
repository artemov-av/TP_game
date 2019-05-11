from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QGraphicsView
from PyQt5.QtCore import pyqtSignal, QObject

from Game import Game, UnitType, FrenchPlayer, BritishPlayer, GamePhase
from GameScene import GameScene
from PlayerPanel import *


class GameView(QObject):
	unit_changed = pyqtSignal(UnitType)
	end_placement_clicked = pyqtSignal()
	end_turn_clicked = pyqtSignal()

	def __init__(self):
		super().__init__()
		self.game_window_ = QMainWindow()
		self.main_widget_ = QWidget()
		self.view_widget_ = QGraphicsView()
		self.british_panel_ = UnitCreatingPanel(Game().get_british_player())
		self.french_panel_ = UnitCreatingPanel(Game().get_french_player())
		self.current_panel_ = self.british_panel_

		self.init_window()
		self.init_main_widget()
		self.init_scene()

		self.british_panel_.connect_radios(self.unit_changed)
		self.british_panel_.connect_end_placement_button(self.end_placement_clicked)
		self.french_panel_.connect_radios(self.unit_changed)
		self.french_panel_.connect_end_placement_button(self.end_placement_clicked)

	def init_window(self):
		self.game_window_.setCentralWidget(self.main_widget_)
		self.game_window_.setWindowTitle('Medieval game v0.1.0')
		self.game_window_.show()

	def init_main_widget(self):
		self.main_widget_.setMinimumSize(1000, 700)
		self.main_widget_layout_ = QHBoxLayout()
		self.main_widget_layout_.addWidget(self.british_panel_)
		self.main_widget_layout_.addWidget(self.view_widget_)
		self.main_widget_.setLayout(self.main_widget_layout_)

	def init_scene(self):
		self.field_scene_ = GameScene()
		self.view_widget_.setScene(self.field_scene_)
		self.field_scene_.add_map_tiles()

	def get_scene(self):
		return self.field_scene_

	def update_after_adding_unit(self):
		self.british_panel_.update_after_adding_unit()
		self.french_panel_.update_after_adding_unit()

	def update_after_turn_change(self):
		self.main_widget_layout_.removeWidget(self.current_panel_)
		self.current_panel_.hide()
		if self.current_panel_ is self.british_panel_:
			self.current_panel_ = self.french_panel_
			self.main_widget_layout_.addWidget(self.current_panel_)
		else:
			self.current_panel_ = self.british_panel_
			self.main_widget_layout_.insertWidget(0, self.current_panel_)
		self.current_panel_.show()

	def change_phase(self, game_phase):
		if game_phase == GamePhase.BATTLE:
			self.main_widget_layout_.removeWidget(self.british_panel_)
			self.british_panel_.hide()
			self.main_widget_layout_.removeWidget(self.french_panel_)
			self.french_panel_.hide()
			self.british_panel_ = BattlePanel(Game().get_british_player())
			self.french_panel_ = BattlePanel(Game().get_french_player())

			active_player = Game().get_active_player()
			if type(active_player) == BritishPlayer:
				self.current_panel_ = self.british_panel_
				self.main_widget_layout_.insertWidget(0, self.current_panel_)
			else:
				self.current_panel_ = self.french_panel_
				self.main_widget_layout_.addWidget(self.current_panel_)
