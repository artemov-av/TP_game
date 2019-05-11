from PyQt5.QtGui import QPixmap, QColor, QBrush
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import QRectF

from UnitImageMapper import UnitImageMapper


class UnitItem(QGraphicsPixmapItem):
	def __init__(self, unit):
		super().__init__()
		self.unit_ = unit
		self.pixmap_ = QPixmap(UnitImageMapper.get_path_to_image(unit))
		self.setPixmap(self.pixmap_)

	def get_unit(self):
		return self.unit


class UnitWithHpBar(UnitItem):
	def __init__(self, unit):
		super().__init__(unit)

	def paint(self, painter, option, widget):
		super().paint(painter, option, widget)
		bar_color = QColor(204, 0, 0)
		hp_bar = QRectF(0, -5, 32 * (self.unit_.hp_ / self.unit_.max_hp_), 5)
		painter.fillRect(hp_bar, QBrush(bar_color))
