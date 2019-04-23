# from enum import Enum
from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QGraphicsView, QLabel, QGroupBox, QRadioButton
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QGraphicsView, QGraphicsScene, QLabel, QGroupBox, QRadioButton

from PyQt5.QtCore import pyqtSignal, QObject
from Game import Game, UnitType
# from GameScene import GameScene


class GameView(QObject):
	unit_changed = pyqtSignal(UnitType)

	def __init__(self):
		super().__init__()
		self.game_window_ = QMainWindow()
		self.main_widget_ = QWidget()
		self.view_widget_ = QGraphicsView()
		self.british_creating_panel_ = UnitCreatingPanel(Game().get_british_player())
		self.french_creating_panel_ = UnitCreatingPanel(Game().get_french_player())
		self.current_creating_panel = self.british_creating_panel_

		self.init_window()
		self.init_main_widget()

		self.british_creating_panel_.connect_radios(self.unit_changed)
		self.french_creating_panel_.connect_radios(self.unit_changed)

	def init_window(self):
		self.game_window_.setCentralWidget(self.main_widget_)
		self.game_window_.setWindowTitle('Medieval game v0.1.0')
		self.game_window_.show()

	def init_main_widget(self):
		self.main_widget_.setMinimumSize(1000, 700)
		self.main_widget_layout = QHBoxLayout()
		self.main_widget_layout.addWidget(self.british_creating_panel_)
		self.main_widget_layout.addWidget(self.view_widget_)
		self.main_widget_.setLayout(self.main_widget_layout)

	def set_scene(self, scene):
		self.view_widget_.setScene(scene)
		scene.add_map_tiles()

	def update_after_adding_unit(self):
		self.british_creating_panel_.update_after_adding_unit()
		self.french_creating_panel_.update_after_adding_unit()

	def update_after_turn_change(self):
		self.main_widget_layout.removeWidget(self.current_creating_panel)
		self.current_creating_panel.hide()
		if self.current_creating_panel is self.british_creating_panel_:
			self.current_creating_panel = self.french_creating_panel_
			self.main_widget_layout.addWidget(self.current_creating_panel)
		else:
			self.current_creating_panel = self.british_creating_panel_
			self.main_widget_layout.insertWidget(0, self.current_creating_panel)
		self.current_creating_panel.show()


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
		layout.addWidget(self.player_lbl_)
		layout.addWidget(self.money_lbl_)
		self.setLayout(layout)

	def add_creating_tools(self, layout):
		self.swordsman_radio_ = QRadioButton("Swordsman")
		self.archer_radio_ = QRadioButton("Archer")
		self.cavalry_radio_ = QRadioButton("Cavalry")
		self.swordsman_radio_.setChecked(True)

		self.creating_tools_group_ = QGroupBox("Create unit:")
		group_layout = QVBoxLayout()
		group_layout.addWidget(self.swordsman_radio_)
		group_layout.addWidget(self.archer_radio_)
		group_layout.addWidget(self.cavalry_radio_)
		self.creating_tools_group_.setLayout(group_layout)

		layout.addWidget(self.creating_tools_group_)

	def update_after_adding_unit(self):
		self.money_lbl_.setText(str(self.player_.get_money()) + " gold")

	def connect_radios(self, signal):
		signal.emit(UnitType.SWORDSMAN)
		self.swordsman_radio_.clicked.connect(lambda f: signal.emit(UnitType.SWORDSMAN))
		self.archer_radio_.clicked.connect(lambda f: signal.emit(UnitType.ARCHER))
		self.cavalry_radio_.clicked.connect(lambda f: signal.emit(UnitType.CAVALRY))
