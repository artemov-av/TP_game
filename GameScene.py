from PyQt5.QtWidgets import QGraphicsScene
from PyQt5 import QtCore

from HexagonalTileItem import *
from Game import Game


class GameScene(QGraphicsScene):
	def __init__(self):
		super().__init__()
		self.tile_radius_ = 30;

	def add_map_tiles(self):
		game_map = Game().get_game_map()
		margin_x = 40
		margin_y = 40
		for y in range(game_map.get_height()):
			for x in range(game_map.get_width()):
				if game_map.is_there_tile(y, x):
					tile = HexagonalTileItem(self.tile_radius_, y, x)
					tile.setPos(margin_x + self.tile_radius_*math.sin(math.pi/3)*(2*x+2-y%2), margin_y + self.tile_radius_*3/2*(y+1))
					self.addItem(tile)
					# tile.installSceneEventFilter(self)
					# self.installEventFilter(self)

	def eventFilter(self, object, event):
		if event.type() == QEvent.GraphicsSceneMousePress:
			print(object.x_, object.y_)
		return True