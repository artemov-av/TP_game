from PyQt5.QtGui import QPixmap, QColor, QBrush
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import QRectF

from UnitImageMapper import UnitImageMapper


class UnitItem(QGraphicsPixmapItem):
	def __init__(self, unit):
		super().__init__()
		self.unit_ = unit
		self.pixmap = QPixmap(UnitImageMapper.get_path_to_image(unit))
		self.setPixmap(self.pixmap)

	def get_unit(self):
		return self.unit


class NewUnitItem(UnitItem):
	def __init__(self, unit):
		super().__init__(unit)
		self.rect = QRectF(0, -5, 32, 5)

	def paint(self, painter, option, widget):
		super().paint(painter, option, widget)
		color = QColor(204, 0, 0)
		painter.fillRect(self.rect, QBrush(color))

	def update_health_bar(self, percentage):
		self.rect = QRectF(0, -5, 32*percentage, 5)
		self.update()
