# from Unit import *


class Tile:
	pass


class GameMap:
	def __init__(self, width, height):
		self.tile_map_ = [[Tile() for x in range(width)] for x in range(height)]
		self.unit_map_ = [[None for x in range(width)] for x in range(height)]

	def add_unit(self, unit, x, y):
		self.unit_map_[x][y] = unit

	def get_unit(self, x, y):
		return self.unit_map_[x][y]

	def can_unit_be_placed(self, x, y):
		return self.is_there_tile(x, y) and self.unit_map_[x][y] is None

	def is_there_tile(self, x, y):
		return self.tile_map_[x][y] is not None

	def remove_unit(self, x, y):
		self.unit_map_[x][y] = None

	def get_width(self):
		return len(self.tile_map_[0])

	def get_height(self):
		return len(self.tile_map_)
