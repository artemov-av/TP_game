from PyQt5.QtGui import QColor, QPainterPath, QBrush
from PyQt5.QtCore import QRectF, QPointF
from PyQt5.QtWidgets import QGraphicsObject

import math


class HexagonalTileItem(QGraphicsObject):
	def __init__(self, radius, x, y):
		super().__init__()
		self.radius_ = radius
		self.x_ = x
		self.y_ = y
		self.pressed_ = False

	def get_coords(self):
		return self.x_, self.y_

	def boundingRect(self):
		return QRectF(-self.radius_*math.sin(math.pi/3), -self.radius_, 2*self.radius_*math.sin(math.pi/3), 2*self.radius_)

	def shape(self):
		path = QPainterPath()
		path.moveTo(QPointF(0, -self.radius_))
		path.lineTo(QPointF(self.radius_*math.sin(math.pi/3), -self.radius_/2))
		path.lineTo(QPointF(self.radius_*math.sin(math.pi/3), self.radius_/2))
		path.lineTo(QPointF(0, self.radius_))
		path.lineTo(QPointF(-self.radius_*math.sin(math.pi/3), self.radius_/2))
		path.lineTo(QPointF(-self.radius_*math.sin(math.pi/3), -self.radius_/2))
		path.lineTo(QPointF(0, -self.radius_))

		return path

	def paint(self, painter, option, widget):
		color = QColor(51, 204, 51)
		if self.pressed_:
			print('pressed')
			painter.fillPath(self.shape(), QBrush(QColor('green')))
		else:
			painter.fillPath(self.shape(), QBrush(QColor(color)))
		painter.drawPath(self.shape())

	def mousePressEvent(self, event):
		super().mousePressEvent(event)

