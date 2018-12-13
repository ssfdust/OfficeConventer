from PyQt5 import QtWidgets , QtCore

class TableWidget(QtWidgets.QTableWidget):
    cellExited = QtCore.pyqtSignal(int, int)
    itemExited = QtCore.pyqtSignal(QtWidgets.QTableWidgetItem)

    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)
        self._last_index = QtCore.QPersistentModelIndex()
        self.viewport().installEventFilter(self)

    def eventFilter(self, widget, event):
        if widget is self.viewport():
            index = self._last_index
            if event.type() == QtCore.QEvent.MouseMove:
                index = self.indexAt(event.pos())
            elif event.type() == QtCore.QEvent.Leave:
                index = QtCore.QModelIndex()
            if index != self._last_index:
                row = self._last_index.row()
                column = self._last_index.column()
                item = self.item(row, column)
                if item is not None:
                    self.itemExited.emit(item)
                self.cellExited.emit(row, column)
                self._last_index = QtCore.QPersistentModelIndex(index)
        return QtWidgets.QTableWidget.eventFilter(self, widget, event)

class Window(QtWidgets.QWidget):
    def __init__(self, rows, columns):
        QtWidgets.QWidget.__init__(self)
        self.table = TableWidget(self)
        for column in range(columns):
            for row in range(rows):
                item = QtWidgets.QTableWidgetItem('Text%d' % row)
                self.table.setItem(row, column, item)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.table)
        self.table.setMouseTracking(True)
        self.table.itemEntered.connect(self.handleItemEntered)
        self.table.itemExited.connect(self.handleItemExited)

    def handleItemEntered(self, item):
        item.setText('11111')

    def handleItemExited(self, item):
        pass


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window(6, 3)
    window.setGeometry(500, 300, 350, 250)
    window.show()
    sys.exit(app.exec_())
