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
		self.army_ = []
		self.fraction_ = None

	def get_money(self):
		return self.money_

	def add_swordsman(self):
		unit = self.unit_factory_.create_swordsman()
		if unit.get_price() > self.money_:
			return None
		if unit is not None:
			self.army_.append(unit)
			self.money_ -= unit.get_price()

		return unit

	def add_archer(self):
		unit = self.unit_factory_.create_archer()
		if unit.get_price() > self.money_:
			return None
		if unit is not None:
			self.army_.append(unit)
			self.money_ -= unit.get_price()

		return unit

	def add_cavalry(self):
		unit = self.unit_factory_.create_cavalry()
		if unit.get_price() > self.money_:
			return None
		if unit is not None:
			self.army_.append(unit)
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


class Game(QObject):
	turn_changed = pyqtSignal()
	unit_added_in_map = pyqtSignal(Unit, int, int)
	game_phase_changed = pyqtSignal(GamePhase)


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
			self.game_map_ = GameMap(10, 5)
			self.current_scene_ = None
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
			self.game_phase_changed.emit(self.game_phase_)

	def get_unit_by_coords(self, x, y):
		return self.game_map_.get_unit(x, y)
