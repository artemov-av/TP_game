from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import pyqtSignal, QEvent

from HexagonalTileItem import *
from UnitItem import *
from Game import Game


class GameScene(QGraphicsScene):
	tile_clicked = pyqtSignal(int, int)

	def __init__(self):
		super().__init__()
		self.tile_radius_ = 30
		self.margin_x_ = 40
		self.margin_y_ = 40
		self.unit_size_ = 32
		self.unit_matrix_ = {}

	def add_map_tiles(self):
		game_map = Game().get_game_map()		
		for y in range(game_map.get_height()):
			for x in range(game_map.get_width()):
				if game_map.is_there_tile(y, x):
					tile = HexagonalTileItem(self.tile_radius_, y, x)
					tile.setPos(self.translate_coords(x, y))
					self.addItem(tile)
					tile.installEventFilter(self)

	def translate_coords(self, x, y):
		return QPointF(self.margin_x_ + self.tile_radius_*math.sin(math.pi/3)*(2*x+2-y % 2),
					   self.margin_y_ + self.tile_radius_*3/2*(y+1))

	def eventFilter(self, object, event):
		if event.type() == QEvent.GraphicsSceneMousePress:
			self.tile_clicked.emit(object.x_, object.y_)
		return True

	def set_pos(self, unit_item, x, y):
		translated_coords = self.translate_coords(x, y)
		translated_coords.setX(translated_coords.x() - self.unit_size_ / 2)
		translated_coords.setY(translated_coords.y() - self.unit_size_ / 2)
		unit_item.setPos(translated_coords)

		self.unit_matrix_[(x, y)] = unit_item

	def add_unit_item(self, unit, x, y):
		y, x = x, y
		unit_item = UnitWithHpBar(unit)

		self.set_pos(unit_item, x, y)
		self.addItem(unit_item)
		unit_item.update()

	def remove_unit_item(self, x, y):
		y, x = x, y
		unit_item = self.unit_matrix_[(x, y)]
		self.removeItem(unit_item)
		unit_item.update()

	def move_unit_item(self, unit_x, unit_y, x, y):
		unit_y, unit_x = unit_x, unit_y
		y, x = x, y

		unit_item = self.unit_matrix_[(unit_x, unit_y)]
		self.unit_matrix_.pop((unit_x, unit_y))

		self.set_pos(unit_item, x, y)
		unit_item.update()

	def update_unit_item(self, x, y):
		self.unit_matrix_[(x, y)].update()
