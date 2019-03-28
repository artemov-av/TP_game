from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem

from Unit import *
from UnitImageMapper import UnitImageMapper


class UnitItem(QGraphicsPixmapItem):
	def __init__(self, unit):
		super().__init__()
		self.unit_ = unit
		self.setPixmap(QPixmap(UnitImageMapper.get_path_to_image(unit)))

	def get_unit(self):
		return self.unit_