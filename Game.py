from enum import Enum
from PyQt5.QtCore import pyqtSignal, QObject

from Unit import *
from GameMap import *
from UnitFraction import UnitFraction


class UnitType(Enum):
	SWORDSMAN = 1
	ARCHER = 2
	CAVALRY = 3


class Player(ABC):
	def __init__(self):
		self.money_ = 1000
		self.fraction_ = None

	def get_money(self):
		return self.money_

	def add_swordsman(self):
		unit = self.unit_factory_.create_swordsman()
		if unit.get_price() > self.money_:
			return None
		if unit is not None:
			self.money_ -= unit.get_price()

		return unit

	def add_archer(self):
		unit = self.unit_factory_.create_archer()
		if unit.get_price() > self.money_:
			return None
		if unit is not None:
			self.money_ -= unit.get_price()

		return unit

	def add_cavalry(self):
		unit = self.unit_factory_.create_cavalry()
		if unit.get_price() > self.money_:
			return None
		if unit is not None:
			self.money_ -= unit.get_price()

		return unit

	def get_fraction(self):
		return self.fraction_


class FrenchPlayer(Player):
	def __init__(self):
		super().__init__()
		self.unit_factory_ = FrenchUnitFactory()
		self.fraction_ = UnitFraction.FRANCE

	def __str__(self):
		return "French Player"


class BritishPlayer(Player):
	def __init__(self):
		super().__init__()
		self.unit_factory_ = BritishUnitFactory()
		self.fraction_ = UnitFraction.BRITAIN

	def __str__(self):
		return "British Player"


class GamePhase(Enum):
	PLACEMENT = 1
	BATTLE = 2
	END_GAME = 3


class TurnUnitsState:
	def __init__(self, game_map):
		self.game_map_ = game_map
		self.attacked_ = [[None for x in range(game_map.get_width())] for x in range(game_map.get_height())]
		self.move_points_spent_ = [[None for x in range(game_map.get_width())] for x in range(game_map.get_height())]
		self.refresh()

	def refresh(self):
		for x in range(self.game_map_.get_height()):
			for y in range(self.game_map_.get_width()):
				unit = self.game_map_.get_unit(x, y)
				if unit is not None:
					self.attacked_[x][y] = False
					self.move_points_spent_[x][y] = 0

	def update_attack(self, x1, y1, x2, y2):
		if not self.attacked_[x1][y1]:
			distance = self.game_map_.get_attacking_distance(x1, y1, x2, y2)
			if distance <= self.game_map_.get_unit(x1, y1).get_range():
				self.attacked_[x1][y1] = True
				return True
		return False

	def update_move_points(self, x1, y1, x2, y2):
		path = self.game_map_.get_walking_path(x1, y1, x2, y2)
		if path is None:
			return False
		distance = len(path) - 1
		if self.move_points_spent_[x1][y1] + distance <= self.game_map_.get_unit(x1, y1).get_move_points():
			self.attacked_[x1][y1], self.attacked_[x2][y2] = self.attacked_[x2][y2], self.attacked_[x1][y1]
			self.move_points_spent_[x1][y1], self.move_points_spent_[x2][y2] = self.move_points_spent_[x2][y2], self.move_points_spent_[x1][y1]
			self.move_points_spent_[x2][y2] += distance
			return True
		return False

	def remove_unit(self, x, y):
		self.attacked_[x][y] = self.move_points_spent_[x][y] = None


class Game(QObject):
	turn_changed = pyqtSignal()
	unit_added_in_map = pyqtSignal(Unit, int, int)
	game_phase_changed = pyqtSignal(GamePhase)
	unit_died = pyqtSignal(int, int)
	unit_moved = pyqtSignal(int, int, int, int)
	unit_updated = pyqtSignal(int, int)
	unit_clicked = pyqtSignal(int, int)
	unit_unclicked = pyqtSignal()

	instance_ = None
	was_created_ = False
	was_inited_ = False

	def __init__(self):
		if not self.was_inited_:
			self.was_inited_ = True
			super().__init__()
			self.game_phase_ = GamePhase.PLACEMENT
			self.placement_ended_ = False
			self.french_player_ = FrenchPlayer()
			self.british_player_ = BritishPlayer()
			self.active_player_ = self.british_player_
			self.game_map_width_ = 10
			self.game_map_height_ = 5
			self.game_map_ = GameMap(self.game_map_width_, self.game_map_height_)
			self.instance_ = self

	def __new__(cls):
		if not cls.was_created_:
			cls.instance_ = QObject.__new__(cls)
			cls.was_created_ = True
		return cls.instance_

	def get_french_player(self):
		return self.french_player_

	def get_british_player(self):
		return self.british_player_

	def get_active_player(self):
		return self.active_player_

	def get_game_map(self):
		return self.game_map_

	def get_game_scene(self):
		return self.game_scene_

	def get_phase(self):
		return self.game_phase_

	def add_unit_in_map(self, unit_type, x, y):
		if self.game_map_.can_unit_be_placed(x, y):
			new_unit = None
			if unit_type == UnitType.SWORDSMAN:
				new_unit = self.active_player_.add_swordsman()
			elif unit_type == UnitType.ARCHER:
				new_unit = self.active_player_.add_archer()
			elif unit_type == UnitType.CAVALRY:
				new_unit = self.active_player_.add_cavalry()

			if new_unit is not None:
				self.game_map_.add_unit(new_unit, x, y)
				self.unit_added_in_map.emit(new_unit, x, y)
				if not self.placement_ended_:
					self.end_turn()

	def end_turn(self):
		if self.active_player_ is self.british_player_:
			self.active_player_ = self.french_player_
		else:
			self.active_player_ = self.british_player_
		if self.game_phase_ == GamePhase.BATTLE:
			self.turn_units_state_.refresh()
		self.turn_changed.emit()

	def end_placement(self):
		if self.game_phase_ != GamePhase.PLACEMENT:
			return
		self.end_turn()
		if not self.placement_ended_:
			self.placement_ended_ = True
		else:
			self.game_phase_ = GamePhase.BATTLE
			self.placement_ended_ = None
			self.turn_units_state_ = TurnUnitsState(self.game_map_)
			self.game_phase_changed.emit(self.game_phase_)

	def get_unit_by_coords(self, x, y):
		return self.game_map_.get_unit(x, y)

	def move_unit(self, x1, y1, x2, y2):
		if self.turn_units_state_.update_move_points(x1, y1, x2, y2):
			self.game_map_.move_unit(x1, y1, x2, y2)
			self.unit_moved.emit(x1, y1, x2, y2)
			return True
		return False

	def attack_unit(self, x1, y1, x2, y2):
		if self.turn_units_state_.update_attack(x1, y1, x2, y2):
			self.game_map_.get_unit(x1, y1).attack(self.game_map_.get_unit(x2, y2))
			if not self.game_map_.get_unit(x2, y2).is_alive():
				self.game_map_.remove_unit(x2, y2)
				self.turn_units_state_.remove_unit(x2, y2)
				self.unit_died.emit(x2, y2)
			else:
				self.unit_updated.emit(x2, y2)
			self.unit_updated.emit(x1, y1)
			return True
		return False

	def click_unit(self, x, y):
		if self.game_map_.get_unit(x, y) is not None:
			self.unit_clicked.emit(x, y)

	def unclick_units(self):
		self.unit_unclicked.emit()
