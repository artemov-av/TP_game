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
		self.hp_bar_length_ = super().boundingRect().width()
		self.hp_bar_width_ = 5
		self.hp_bar_offset_ = 2
		self.hp_bar_color_ = QColor(204, 0, 0)


	def boundingRect(self):
		old_rect = super().boundingRect()
		y_delta = self.hp_bar_width_ + self.hp_bar_offset_
		return QRectF(old_rect.x(), old_rect.y() - y_delta, old_rect.width(), old_rect.height() + y_delta)


	def paint(self, painter, option, widget):
		super().paint(painter, option, widget)
		hp_bar = QRectF(0, -self.hp_bar_width_-self.hp_bar_offset_, self.hp_bar_length_*(self.unit_.get_hp()/self.unit_.get_max_hp()), self.hp_bar_width_)
		painter.fillRect(hp_bar, QBrush(self.hp_bar_color_))
