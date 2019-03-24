from PyQt5.QtGui import QPolygonF, QColor, QPainterPath, QBrush
from PyQt5.QtCore import QRectF, QPointF
from PyQt5.QtWidgets import QGraphicsItem
import math


class HexagonalTileItem(QGraphicsItem):
	def __init__(self, radius):
		super().__init__()
		self.radius_ = radius

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
		painter.fillPath(self.shape(), QBrush(QColor("green")))
		painter.drawPath(self.shape())
		# painter.drawPolygon(polygon)
		# painter.fillPolygon(QPolygonF(points), QColor(0, 255, 0))
		# painter.drawPoint(QPointF(0, 0))
