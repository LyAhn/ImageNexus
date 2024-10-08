from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtGui import QPen, QColor
from PySide6.QtCore import Qt, QRectF, Signal, QObject

class ClickableRectItem(QObject, QGraphicsRectItem):
    """
    A QGraphicsRectItem that emits a signal when clicked.
    """
    faceSelected = Signal(int, bool)  # Signal: face_index, is_selected

    def __init__(self, rect, face_index, parent=None):
        QObject.__init__(self)
        QGraphicsRectItem.__init__(self, rect, parent)
        self.face_index = face_index
        self.selected = False
        self.setPen(QPen(QColor(255, 0, 0), 4)) # Red border, width of 4
        self.setBrush(Qt.NoBrush)
        self.setFlag(QGraphicsRectItem.ItemIsSelectable, True)
        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        self.toggle_selection()
        event.accept()

    def toggle_selection(self):
        self.selected = not self.selected
        self.update_appearance()
        self.faceSelected.emit(self.face_index, self.selected)

    def update_appearance(self):
        color = QColor(0, 255, 0) if self.selected else QColor(255, 0, 0) # Green if selected, red if not
        self.setPen(QPen(color, 4)) # keep the border width at 4

    def hoverEnterEvent(self, event):
        self.setPen(QPen(QColor(0, 0, 255), 4)) # Blue border width of 4
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.update_appearance()
        super().hoverLeaveEvent(event)