# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'default.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QWidget, QFileDialog, QMessageBox,
                             QCheckBox, QHBoxLayout, QProgressDialog)
from PyQt5.QtGui import QPixmap
from collections import OrderedDict
from convert import FullConverter
from shutil import copyfile

import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1127, 615)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(750, 560, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.add3 = QtWidgets.QToolButton(Dialog)
        self.add3.setGeometry(QtCore.QRect(750, 320, 31, 31))
        self.add3.setObjectName("add3")
        self.del3 = QtWidgets.QToolButton(Dialog)
        self.del3.setGeometry(QtCore.QRect(780, 320, 31, 31))
        self.del3.setObjectName("del3")
        self.select3 = QtWidgets.QPushButton(Dialog)
        self.select3.setGeometry(QtCore.QRect(660, 320, 61, 31))
        self.select3.setObjectName("select3")
        self.table1 = QtWidgets.QTableWidget(Dialog)
        self.table1.setGeometry(QtCore.QRect(0, 40, 221, 271))
        self.table1.setObjectName("table1")
        self.table1.setColumnCount(2)
        self.table1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(1, item)
        self.select1 = QtWidgets.QPushButton(Dialog)
        self.select1.setGeometry(QtCore.QRect(80, 320, 61, 31))
        self.select1.setObjectName("select1")
        self.add1 = QtWidgets.QToolButton(Dialog)
        self.add1.setGeometry(QtCore.QRect(160, 320, 31, 31))
        self.add1.setObjectName("add1")
        self.del1 = QtWidgets.QToolButton(Dialog)
        self.del1.setGeometry(QtCore.QRect(190, 320, 31, 31))
        self.del1.setObjectName("del1")
        self.table3 = QtWidgets.QTableWidget(Dialog)
        self.table3.setGeometry(QtCore.QRect(590, 40, 221, 271))
        self.table3.setObjectName("table3")
        self.table3.setColumnCount(2)
        self.table3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table3.setHorizontalHeaderItem(1, item)
        self.table2 = QtWidgets.QTableWidget(Dialog)
        self.table2.setGeometry(QtCore.QRect(290, 40, 221, 271))
        self.table2.setObjectName("table2")
        self.table2.setColumnCount(2)
        self.table2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(1, item)
        self.select2 = QtWidgets.QPushButton(Dialog)
        self.select2.setGeometry(QtCore.QRect(350, 320, 61, 31))
        self.select2.setObjectName("select2")
        self.add2 = QtWidgets.QToolButton(Dialog)
        self.add2.setGeometry(QtCore.QRect(440, 320, 31, 31))
        self.add2.setObjectName("add2")
        self.del2 = QtWidgets.QToolButton(Dialog)
        self.del2.setGeometry(QtCore.QRect(470, 320, 31, 31))
        self.del2.setObjectName("del2")
        self.table4 = QtWidgets.QTableWidget(Dialog)
        self.table4.setGeometry(QtCore.QRect(880, 40, 221, 271))
        self.table4.setObjectName("table4")
        self.table4.setColumnCount(2)
        self.table4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table4.setHorizontalHeaderItem(1, item)
        self.select4 = QtWidgets.QPushButton(Dialog)
        self.select4.setGeometry(QtCore.QRect(950, 320, 61, 31))
        self.select4.setObjectName("select4")
        self.add4 = QtWidgets.QToolButton(Dialog)
        self.add4.setGeometry(QtCore.QRect(1030, 320, 31, 31))
        self.add4.setObjectName("add4")
        self.del4 = QtWidgets.QToolButton(Dialog)
        self.del4.setGeometry(QtCore.QRect(1060, 320, 31, 31))
        self.del4.setObjectName("del4")
        self.pic = QtWidgets.QLabel(Dialog)
        self.pic.setGeometry(QtCore.QRect(20, 400, 331, 191))
        self.pic.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.pic.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pic.setLineWidth(1)
        self.pic.setAlignment(QtCore.Qt.AlignCenter)
        self.pic.setObjectName("pic")

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add3.setText(_translate("Dialog", "+"))
        self.del3.setText(_translate("Dialog", "-"))
        self.select3.setText(_translate("Dialog", "选择"))
        item = self.table1.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "文件名"))
        item = self.table1.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "是否盖章"))
        self.select1.setText(_translate("Dialog", "选择"))
        self.add1.setText(_translate("Dialog", "+"))
        self.del1.setText(_translate("Dialog", "-"))
        item = self.table3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "文件名"))
        item = self.table3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "是否盖章"))
        item = self.table2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "文件名"))
        item = self.table2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "是否盖章"))
        self.select2.setText(_translate("Dialog", "选择"))
        self.add2.setText(_translate("Dialog", "+"))
        self.del2.setText(_translate("Dialog", "-"))
        item = self.table4.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "文件名"))
        item = self.table4.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "是否盖章"))
        self.select4.setText(_translate("Dialog", "选择"))
        self.add4.setText(_translate("Dialog", "+"))
        self.del4.setText(_translate("Dialog", "-"))
        self.pic.setText(_translate("Dialog", "印章预览"))

class ProcessDialog(QWidget):

    def __init__(self, filename=None):
        super().__init__()
        self.title = '处理文件'
        self.left = 300
        self.top = 120
        self.width = 640
        self.height = 480
        self._filename = filename
        self.initUI()

    def initUI(self):
        self.resize(300, 150)
        self.setWindowTitle(self.title)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # self.openProgressDialog()

        self.show()

    def openProgressDialog(self):    
        num = 0
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在转换...")
        progress.setGeometry(self.left, self.top, self.width, self.height)
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(5)
        # progress.setAutoReset(False)
        # progress.setWindowModality(Qt.WindowModal)
        progress.setWindowModality(QtCore.Qt.ApplicationModal)
        # progress.setWindowModality(Qt.NonModal)
        progress.setRange(0, 1000000)
        # progress.setMinimum(5000000)
        # progress.setMaximum(10000000)
        for i in range(num + 1000000):
            # time.sleep(0.1)
            # print(i)
            progress.setValue(i)
            if progress.wasCanceled():
                QMessageBox.warning(self, "提示", "操作失败")
                break
        # else:
        #     progress.setValue(i)
            if i == 1000000:
                QMessageBox.information(self, "提示", "操作成功")
                break

class saveFDialog(QWidget):

    def __init__(self, filename=None, filters=None):
        super().__init__()
        self.filters = filters
        self.title = '保存文件'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self._filename = filename
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.saveFileNameDialog()

        self.show()

    def saveFileNameDialog(self):    
        if self.filters:
            filters = self.filters
        else:
            filters = ("pdf Files (*.pdf);;"
                       )
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, self.title, "合成.pdf",
                                                  filters, options=options)
        if fileName:
            if fileName.endswith('.pdf'):
                self.saveName = fileName
            else:
                self.saveName = fileName + '.pdf'
        elif self._filename == '' or self._filename is None:
            pass

class openFDialog(QWidget):

    def __init__(self, filename=None, filters=None):
        super().__init__()
        self.filters = filters
        self.title = '打开文件'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self._filename = filename
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.openFileNameDialog()

        self.show()

    def openFileNameDialog(self):    
        if self.filters:
            filters = self.filters
        else:
            filters = ("pdf Files (*.pdf);;"
                       "Microsoft Office Word (*.doc *.docx);;"
                       "Microsoft Office Excel (*.xls *.xlsx);;"
                       "All Support Files (*.doc *.docx *.pdf *.xls *.xlsx)"
                       )
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, self.title, "",
                                                  filters, options=options)
        if fileName:
            self.fileName = fileName
        elif self._filename == '' or self._filename is None:
            pass

class MainDialog(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        self.select1.clicked.connect(self.openFile1)
        self.add1.clicked.connect(self.openFile1)
        self.del1.clicked.connect(self.delFile1)
        self.table1.cellClicked.connect(self.showPic1)
        self.select2.clicked.connect(self.openFile2)
        self.add2.clicked.connect(self.openFile2)
        self.del2.clicked.connect(self.delFile2)
        self.table2.cellClicked.connect(self.showPic2)
        self.select3.clicked.connect(self.openFile3)
        self.add3.clicked.connect(self.openFile3)
        self.del3.clicked.connect(self.delFile3)
        self.table3.cellClicked.connect(self.showPic3)
        self.select4.clicked.connect(self.openFile4)
        self.add4.clicked.connect(self.openFile4)
        self.del4.clicked.connect(self.delFile4)
        self.table4.cellClicked.connect(self.showPic4)
        self.contents = {}
        self.buttonBox.accepted.connect(self.convert)
        self.picfilters = "图像文件(*.jpg *.jpeg *.png *.bmp)"

    def setPic(self, pic):
        self.pic.setPixmap(QPixmap(pic))

    def handleClicked1(self, item):
        chCliked = self.table1.sender()
        layout = chCliked.parent().layout()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table1.indexAt(posWidget).row()
        nameItem = self.table1.item(rowIndex, 0)
        fname = nameItem.text()
        btn = layout.itemAt(1).widget()
        if item:
            openPicHandler = openFDialog(filters=self.picfilters)
            if hasattr(openPicHandler, 'fileName'):
                self.contents[fname][1] = openPicHandler.fileName
                self.setPic(openPicHandler.fileName)
                btn.show()
            else:
                chCliked.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.contents[fname][1] = 0
            btn.hide()

    def handleClicked2(self, item):
        chCliked = self.table2.sender()
        layout = chCliked.parent().layout()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table2.indexAt(posWidget).row()
        nameItem = self.table2.item(rowIndex, 0)
        fname = nameItem.text()
        btn = layout.itemAt(1).widget()
        if item:
            openPicHandler = openFDialog(filters=self.picfilters)
            if hasattr(openPicHandler, 'fileName'):
                self.contents[fname][1] = openPicHandler.fileName
                self.setPic(openPicHandler.fileName)
                btn.show()
            else:
                chCliked.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.contents[fname][1] = 0
            btn.hide()

    def handleClicked3(self, item):
        chCliked = self.table3.sender()
        layout = chCliked.parent().layout()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table3.indexAt(posWidget).row()
        nameItem = self.table3.item(rowIndex, 0)
        fname = nameItem.text()
        btn = layout.itemAt(1).widget()
        if item:
            openPicHandler = openFDialog(filters=self.picfilters)
            if hasattr(openPicHandler, 'fileName'):
                self.contents[fname][1] = openPicHandler.fileName
                self.setPic(openPicHandler.fileName)
                btn.show()
            else:
                chCliked.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.contents[fname][1] = 0
            btn.hide()

    def handleClicked4(self, item):
        chCliked = self.table4.sender()
        layout = chCliked.parent().layout()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table4.indexAt(posWidget).row()
        nameItem = self.table4.item(rowIndex, 0)
        fname = nameItem.text()
        btn = layout.itemAt(1).widget()
        if item:
            openPicHandler = openFDialog(filters=self.picfilters)
            if hasattr(openPicHandler, 'fileName'):
                self.contents[fname][1] = openPicHandler.fileName
                self.setPic(openPicHandler.fileName)
                btn.show()
            else:
                chCliked.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.contents[fname][1] = 0
            btn.hide()

        print(self.contents)

    def selPic1(self):
        chCliked = self.table1.sender()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table1.indexAt(posWidget).row()
        nameItem = self.table1.item(rowIndex, 0)
        fname = nameItem.text()
        openPicHandler = openFDialog(filters=self.picfilters)
        if hasattr(openPicHandler, 'fileName'):
            self.contents[fname][1] = openPicHandler.fileName
            self.setPic(openPicHandler.fileName)

    def selPic2(self):
        chCliked = self.table2.sender()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table2.indexAt(posWidget).row()
        nameItem = self.table2.item(rowIndex, 0)
        fname = nameItem.text()
        openPicHandler = openFDialog(filters=self.picfilters)
        if hasattr(openPicHandler, 'fileName'):
            self.contents[fname][1] = openPicHandler.fileName
            self.setPic(openPicHandler.fileName)

    def selPic3(self):
        chCliked = self.table3.sender()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table3.indexAt(posWidget).row()
        nameItem = self.table3.item(rowIndex, 0)
        fname = nameItem.text()
        openPicHandler = openFDialog(filters=self.picfilters)
        if hasattr(openPicHandler, 'fileName'):
            self.contents[fname][1] = openPicHandler.fileName
            self.setPic(openPicHandler.fileName)

    def selPic4(self):
        chCliked = self.table4.sender()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table4.indexAt(posWidget).row()
        nameItem = self.table4.item(rowIndex, 0)
        fname = nameItem.text()
        openPicHandler = openFDialog(filters=self.picfilters)
        if hasattr(openPicHandler, 'fileName'):
            self.contents[fname][1] = openPicHandler.fileName
            self.setPic(openPicHandler.fileName)

    def showPic1(self, row, col):
        if col > 0:
            return 1
        item = self.table1.item(row, col)
        fname = item.text()
        pic = self.contents[fname][1]
        if isinstance(pic, str):
            self.setPic(pic)

    def showPic2(self, row, col):
        if col > 0:
            return 1
        item = self.table2.item(row, col)
        fname = item.text()
        pic = self.contents[fname][1]
        if isinstance(pic, str):
            self.setPic(pic)

    def showPic3(self, row, col):
        if col > 0:
            return 1
        item = self.table3.item(row, col)
        fname = item.text()
        pic = self.contents[fname][1]
        if isinstance(pic, str):
            self.setPic(pic)

    def showPic4(self, row, col):
        if col > 0:
            return 1
        item = self.table4.item(row, col)
        fname = item.text()
        pic = self.contents[fname][1]
        if isinstance(pic, str):
            self.setPic(pic)

    def openFile1(self):
        openFileHandler = openFDialog('')
        if hasattr(openFileHandler, 'fileName'):
            fname = os.path.basename(openFileHandler.fileName)
            if fname in self.contents:
                openFileHandler.hide()
                PopupWindow("选择文件已存在")

                return 1 

            self.contents[fname] = [openFileHandler.fileName, 0]
            rowPosition = self.table1.rowCount()
            self.table1.insertRow(rowPosition)
            item = QtWidgets.QTableWidgetItem()
            item.setText(fname)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.table1.setItem(rowPosition, 0, item)
            cell_widget = QWidget()
            chk_bx = QCheckBox()
            chk_bx.clicked.connect(self.handleClicked1)
            chk_bx.setCheckState(QtCore.Qt.Unchecked)
            btn = QtWidgets.QPushButton()
            btn.setText('修改')
            btn.clicked.connect(self.selPic1)
            btn.hide()
            lay_out = QHBoxLayout(cell_widget)
            lay_out.addWidget(chk_bx)
            lay_out.addWidget(btn)
            lay_out.setAlignment(QtCore.Qt.AlignCenter)
            lay_out.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(lay_out)
            self.table1.setCellWidget(rowPosition, 1, cell_widget)

        return 0

    def openFile2(self):
        openFileHandler = openFDialog('')
        if hasattr(openFileHandler, 'fileName'):
            fname = os.path.basename(openFileHandler.fileName)
            if fname in self.contents:
                openFileHandler.hide()
                PopupWindow("选择文件已存在")

                return 1 

            self.contents[fname] = [openFileHandler.fileName, 0]
            rowPosition = self.table2.rowCount()
            self.table2.insertRow(rowPosition)
            item = QtWidgets.QTableWidgetItem()
            item.setText(fname)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.table2.setItem(rowPosition, 0, item)
            cell_widget = QWidget()
            chk_bx = QCheckBox()
            chk_bx.clicked.connect(self.handleClicked2)
            chk_bx.setCheckState(QtCore.Qt.Unchecked)
            btn = QtWidgets.QPushButton()
            btn.setText('修改')
            btn.clicked.connect(self.selPic2)
            btn.hide()
            lay_out = QHBoxLayout(cell_widget)
            lay_out.addWidget(chk_bx)
            lay_out.addWidget(btn)
            lay_out.setAlignment(QtCore.Qt.AlignCenter)
            lay_out.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(lay_out)
            self.table2.setCellWidget(rowPosition, 1, cell_widget)

        return 0

    def openFile3(self):
        openFileHandler = openFDialog('')
        if hasattr(openFileHandler, 'fileName'):
            fname = os.path.basename(openFileHandler.fileName)
            if fname in self.contents:
                openFileHandler.hide()
                PopupWindow("选择文件已存在")

                return 1 

            self.contents[fname] = [openFileHandler.fileName, 0]
            rowPosition = self.table3.rowCount()
            self.table3.insertRow(rowPosition)
            item = QtWidgets.QTableWidgetItem()
            item.setText(fname)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.table3.setItem(rowPosition, 0, item)
            cell_widget = QWidget()
            chk_bx = QCheckBox()
            chk_bx.clicked.connect(self.handleClicked3)
            chk_bx.setCheckState(QtCore.Qt.Unchecked)
            btn = QtWidgets.QPushButton()
            btn.setText('修改')
            btn.clicked.connect(self.selPic3)
            btn.hide()
            lay_out = QHBoxLayout(cell_widget)
            lay_out.addWidget(chk_bx)
            lay_out.addWidget(btn)
            lay_out.setAlignment(QtCore.Qt.AlignCenter)
            lay_out.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(lay_out)
            self.table3.setCellWidget(rowPosition, 1, cell_widget)

        return 0

    def openFile4(self):
        openFileHandler = openFDialog('')
        if hasattr(openFileHandler, 'fileName'):
            fname = os.path.basename(openFileHandler.fileName)
            if fname in self.contents:
                openFileHandler.hide()
                PopupWindow("选择文件已存在")

                return 1 

            self.contents[fname] = [openFileHandler.fileName, 0]
            rowPosition = self.table4.rowCount()
            self.table4.insertRow(rowPosition)
            item = QtWidgets.QTableWidgetItem()
            item.setText(fname)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.table4.setItem(rowPosition, 0, item)
            cell_widget = QWidget()
            chk_bx = QCheckBox()
            chk_bx.clicked.connect(self.handleClicked4)
            chk_bx.setCheckState(QtCore.Qt.Unchecked)
            btn = QtWidgets.QPushButton()
            btn.setText('修改')
            btn.clicked.connect(self.selPic4)
            btn.hide()
            lay_out = QHBoxLayout(cell_widget)
            lay_out.addWidget(chk_bx)
            lay_out.addWidget(btn)
            lay_out.setAlignment(QtCore.Qt.AlignCenter)
            lay_out.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(lay_out)
            self.table4.setCellWidget(rowPosition, 1, cell_widget)

        return 0

    def delFile1(self):
        select1_row = self.table1.selectedIndexes()
        p = self.table1.selectionModel()
        for i in select1_row:
            p = self.table1.selectedIndexes()[0]
            fname = self.table1.item(p.row(), 0).text()
            self.contents.pop(fname)
            self.table1.removeRow(p.row())

        return 0

    def delFile2(self):
        select2_row = self.table2.selectedIndexes()
        p = self.table2.selectionModel()
        for i in select2_row:
            p = self.table2.selectedIndexes()[0]
            fname = self.table2.item(p.row(), 0).text()
            self.contents.pop(fname)
            self.table2.removeRow(p.row())

        return 0

    def delFile3(self):
        select3_row = self.table3.selectedIndexes()
        p = self.table3.selectionModel()
        for i in select3_row:
            p = self.table3.selectedIndexes()[0]
            fname = self.table3.item(p.row(), 0).text()
            self.contents.pop(fname)
            self.table3.removeRow(p.row())

        return 0

    def delFile4(self):
        select4_row = self.table4.selectedIndexes()
        p = self.table4.selectionModel()
        for i in select4_row:
            p = self.table4.selectedIndexes()[0]
            fname = self.table4.item(p.row(), 0).text()
            self.contents.pop(fname)
            self.table4.removeRow(p.row())

        return 0

    def getDataList(self):
        data = OrderedDict()
        for tab in [self.table1, self.table2, self.table3, self.table4]:
            i = 0
            while i < tab.rowCount():
                fname = tab.item(i, 0).text()
                data[fname] = self.contents[fname]
                i += 1

        return data

    def convert(self):
        data = self.getDataList()
        c = FullConverter(data)
        c.check()
        if c.errcode != 0:
            PopupWindow(c.err)
        else:
            c.convert()
            c.setMark()
            outfile = c.concat()
            saveDialog = saveFDialog()
            copyfile(outfile, saveDialog.saveName)

class PopupWindow(QWidget):

    def __init__(self, message):
        super().__init__()
        self.title = '提示'
        self.left = 410
        self.top = 210
        self.width = 320
        self.height = 200
        self._message = message
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        QMessageBox.question(self, '提示', self._message, QMessageBox.Yes)

        self.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    prog = MainDialog(Dialog)
    Dialog.show()
    sys.exit(Dialog.exec_())
