from abc import ABC
from enum import Enum

from Unit import *
from GameMap import *


class Player(ABC):
	def __init__(self):
		self.money_ = 1000
		self.army_ = []

	def get_money(self):
		return self.money_

	def add_swordsman(self):
		unit = unit_factory_.create_swordsman()
		if unit.get_cost() > self.money_:
			return None
		if unit is not None:
			self.army_.append(unit)
			self.money_ -= unit.get_price()

		return unit

	def add_archer(self):
		unit = unit_factory_.create_archer()
		if unit.get_cost() > self.money_:
			return None
		if unit is not None:
			self.army_.append(unit)
			self.money_ -= unit.get_price()

		return unit

	def add_cavalry(self):
		unit = unit_factory_.create_cavalry()
		if unit.get_cost() > self.money_:
			return None
		if unit is not None:
			self.army_.append(unit)
			self.money_ -= unit.get_price()

		return unit


class FrenchPlayer(Player):
	def __init__(self):
		super().__init__()
		self.unit_factory_ = FrenchUnitFactory()

	def __str__(self):
		return "French Player"


class BritishPlayer(Player):
	def __init__(self):
		super().__init__()
		self.unit_factory_ = BritishUnitFactory()

	def __str__(self):
		return "British Player"

class Singleton(type):
	is_created = False
	instance = None
	def __call__(cls):
		if not cls.is_created:
			cls.is_created = True
		cls.instance = super().__call__()
		return cls.instance


class Game(metaclass=Singleton):
	def __init__(self):
		self.french_player_ = FrenchPlayer()
		self.british_player_ = BritishPlayer()
		self.active_player_ = self.british_player_
		self.game_map_ = GameMap(10, 5)

	def get_french_player(self):
		return self.french_player_

	def get_british_player(self):
		return self.british_player_

	def get_game_map(self):
		return self.game_map_
