from PyQt5.QtWidgets import QGraphicsScene
# from PyQt5 import QtCore
# from PyQt5.QtCore import pyqtSignal, QEvent, QPointF
from PyQt5.QtCore import pyqtSignal, QEvent


from HexagonalTileItem import *
from UnitItem import UnitItem
# from Game import Game, UnitType
from Game import Game


class GameScene(QGraphicsScene):
	tile_clicked = pyqtSignal(int, int)

	def __init__(self):
		super().__init__()
		self.tile_radius_ = 30
		self.margin_x_ = 40
		self.margin_y_ = 40
		self.unit_size_ = 32

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

	def add_unit_item(self, unit, x, y):
		y, x = x, y
		unit_item = UnitItem(unit)
		translated_coords = self.translate_coords(x, y)
		translated_coords.setX(translated_coords.x() - self.unit_size_/2)
		translated_coords.setY(translated_coords.y() - self.unit_size_/2)
		unit_item.setPos(translated_coords)
		self.addItem(unit_item)
