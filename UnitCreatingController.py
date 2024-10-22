from Game import Game, UnitType
from GameScene import GameScene

class UnitCreatingController:
	def __init__(self):
		self.chosen_unit_type_ = UnitType.SWORDSMAN

	def changed_unit_type(self, unit_type):
		self.chosen_unit_type_ = unit_type

	def tile_clicked(self, x, y):
		Game().add_unit_in_map(self.chosen_unit_type_, x, y)