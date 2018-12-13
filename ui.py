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
from demo import Ui_Dialog
from time import sleep

import os

class ProcessDialog(QWidget):
    """进度条对话框
    """

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
    """保存对话框

    选择文件后，选择文件在self.fileName属性
    """

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
        # 使用原生对话框
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, self.title, "合成.pdf",
                                                  filters, options=options)
        if fileName:
            if fileName.endswith('.pdf'):
                self.saveName = fileName
            else:
                self.saveName = fileName + '.pdf'

class openFDialog(QWidget):
    """打开文件对话框

    """

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
            filters = ("All Support Files (*.doc *.docx *.pdf *.xls *.xlsx);;"
                       "Microsoft Office Word (*.doc *.docx);;"
                       "Microsoft Office Excel (*.xls *.xlsx);;"
                       "pdf Files (*.pdf);;"
                       )
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, self.title, "",
                                                  filters, options=options)
        if fileName:
            self.fileName = fileName
        elif self._filename == '' or self._filename is None:
            pass

class MainDialog(Ui_Dialog):
    """主对话框
    """
    def __init__(self, dialog):
        """设置slot连接

        contents为字典类型，字典key为文件名，
        字典value为一个保存两个元素的数组，第
        一个元素保存的为文件路径，第二个元素
        保存的为印章文件。
        如果没有印章文件则以数字0代替。
        """
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        self.select1.clicked.connect(self.openFile1)
        self.table1.cellClicked.connect(self.showPic1)
        self.select2.clicked.connect(self.openFile2)
        self.table2.cellClicked.connect(self.showPic2)
        self.select3.clicked.connect(self.openFile3)
        self.table3.cellClicked.connect(self.showPic3)
        self.select4.clicked.connect(self.openFile4)
        self.table4.cellClicked.connect(self.showPic4)
        self.table1.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.table2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.table3.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.table4.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.ok_btn.clicked.connect(self.convert)
        self.cancel_btn.clicked.connect(exit)
        self.contents = {}
        self.picfilters = "图像文件(*.jpg *.jpeg *.png *.bmp)"

    def setPic(self, table, pic):
        """针对特定表格设定印章图案
        """
        tablename = table.objectName()
        picobj = getattr(self, "pic{}".format(tablename.replace('table', '')))
        picobj.setPixmap(QPixmap(pic))

    def handleClicked1(self, item):
        """处理打勾事件

        打勾后，弹出打开文件对话框，选择印章图案
        ，更换印章图片，并将contents部分图片修改
        为替换的图片。
        """
        # 获取发送信号的控件
        chCliked = self.table1.sender()
        # 根据其父类Widget的layout
        # 才能获取正确QPoint
        layout = chCliked.parent().layout()
        posWidget = chCliked.parent().pos()
        # 根据QPoint获取行号
        rowIndex = self.table1.indexAt(posWidget).row()
        # 获取对象
        nameItem = self.table1.item(rowIndex, 0)
        fname = nameItem.text()
        btn = layout.itemAt(1).widget()
        # 处理是打勾还是去掉打勾
        if item:
            openPicHandler = openFDialog(filters=self.picfilters)
            # 如果文件被选择，则进行处理
            if hasattr(openPicHandler, 'fileName'):
                self.contents[fname][1] = openPicHandler.fileName
                self.setPic(self.table1, openPicHandler.fileName)
                btn.show()
            else:
                chCliked.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.contents[fname][1] = 0
            btn.hide()

    def handleClicked2(self, item):
        """TODO:
            合并为一个
        """
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
                self.setPic(self.table2, openPicHandler.fileName)
                btn.show()
            else:
                chCliked.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.contents[fname][1] = 0
            btn.hide()

    def handleClicked3(self, item):
        """TODO:
            合并为一个
        """
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
                self.setPic(self.table3, openPicHandler.fileName)
                btn.show()
            else:
                chCliked.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.contents[fname][1] = 0
            btn.hide()

    def handleClicked4(self, item):
        """TODO:
            合并为一个
        """
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
                self.setPic(self.table4, openPicHandler.fileName)
                btn.show()
            else:
                chCliked.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.contents[fname][1] = 0
            btn.hide()

    def selPic1(self):
        """修改图片
        """
        # 获取被点击的图片
        chCliked = self.table1.sender()
        # 获取Widget的位置
        posWidget = chCliked.parent().pos()
        rowIndex = self.table1.indexAt(posWidget).row()
        # 获取名称
        nameItem = self.table1.item(rowIndex, 0)
        fname = nameItem.text()
        openPicHandler = openFDialog(filters=self.picfilters)
        # 判断修改
        if hasattr(openPicHandler, 'fileName'):
            self.contents[fname][1] = openPicHandler.fileName
            self.setPic(self.table1, openPicHandler.fileName)

    def selPic2(self):
        """TODO:
            合并为一个
        """
        chCliked = self.table2.sender()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table2.indexAt(posWidget).row()
        nameItem = self.table2.item(rowIndex, 0)
        fname = nameItem.text()
        openPicHandler = openFDialog(filters=self.picfilters)
        if hasattr(openPicHandler, 'fileName'):
            self.contents[fname][1] = openPicHandler.fileName
            self.setPic(self.table2, openPicHandler.fileName)

    def selPic3(self):
        """TODO:
            合并为一个
        """
        chCliked = self.table3.sender()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table3.indexAt(posWidget).row()
        nameItem = self.table3.item(rowIndex, 0)
        fname = nameItem.text()
        openPicHandler = openFDialog(filters=self.picfilters)
        if hasattr(openPicHandler, 'fileName'):
            self.contents[fname][1] = openPicHandler.fileName
            self.setPic(self.table3, openPicHandler.fileName)

    def selPic4(self):
        """TODO:
            合并为一个
        """
        chCliked = self.table4.sender()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table4.indexAt(posWidget).row()
        nameItem = self.table4.item(rowIndex, 0)
        fname = nameItem.text()
        openPicHandler = openFDialog(filters=self.picfilters)
        if hasattr(openPicHandler, 'fileName'):
            self.contents[fname][1] = openPicHandler.fileName
            self.setPic(self.table3, openPicHandler.fileName)

    def showPic1(self, row, col):
        """处理cellClicked事件

            如果点击cell，则根据行列，
            设置预览的印章
        """
        # 过滤掉用户点击其他cell导致错误
        if col > 0:
            return 1
        # 获取元素
        item = self.table1.item(row, col)
        try:
            fname = item.text()
            pic = self.contents[fname][1]
            if isinstance(pic, str):
                self.setPic(self.table1, pic)
        except Exception:
            pass

    def showPic2(self, row, col):
        """TODO:
            合并为一个
        """
        if col > 0:
            return 1
        try:
            item = self.table2.item(row, col)
            fname = item.text()
            pic = self.contents[fname][1]
            if isinstance(pic, str):
                self.setPic(self.table2, pic)
        except Exception:
            pass

    def showPic3(self, row, col):
        """TODO:
            合并为一个
        """
        if col > 0:
            return 1
        try:
            item = self.table3.item(row, col)
            fname = item.text()
            pic = self.contents[fname][1]
            if isinstance(pic, str):
                self.setPic(self.table3, pic)
        except Exception:
            pass

    def showPic4(self, row, col):
        """TODO:
            合并为一个
        """
        if col > 0:
            return 1
        try:
            item = self.table4.item(row, col)
            fname = item.text()
            pic = self.contents[fname][1]
            if isinstance(pic, str):
                self.setPic(self.table4, pic)
        except Exception:
            pass

    def openFile1(self):
        """处理选择按钮点击事件

        文件被选中后，将会依次在新的一行中插入文字，
        勾选框，修改按钮（默认隐藏）以及删除按钮。
        """
        # 构建打开对话框
        openFileHandler = openFDialog('')
        # 处理备选文件
        if hasattr(openFileHandler, 'fileName'):
            # 获取默认名称
            fname = os.path.basename(openFileHandler.fileName)
            # 过滤重名文件
            # Tip: 能否允许重名文件
            if fname in self.contents:
                openFileHandler.hide()
                PopupWindow("选择文件已存在")

                return 1 

            # 将文件插入contents中，默认无印章图片
            self.contents[fname] = [openFileHandler.fileName, 0]
            # 获取总行数
            rowPosition = self.table1.rowCount()
            # 对第一行作特殊处理，因为第一行初始为空行
            # 所以在插入第一行时采用的是填充，而不是插
            # 入新行，从第二行开始插入新行。
            if rowPosition == 1:
                text = self.table1.item(0, 0)
                if text is None or text.text() == '':
                    rowPosition = 0
                else:
                    self.table1.insertRow(rowPosition)
            else:
                self.table1.insertRow(rowPosition)
            # 绘制第一个文字部分控件的内容
            item = QtWidgets.QTableWidgetItem()
            item.setText(fname)
            item.setToolTip(fname)
            # 设置居中
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            # 禁止编辑
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.table1.setItem(rowPosition, 0, item)

            # 绘制第二个cell部分内容
            cell_widget = QWidget()
            # 初始化checkbox
            chk_bx = QCheckBox()
            chk_bx.clicked.connect(self.handleClicked1)
            chk_bx.setCheckState(QtCore.Qt.Unchecked)
            # 初始化button
            btn = QtWidgets.QPushButton()
            btn.setText('修改')
            btn.clicked.connect(self.selPic1)
            btn.hide()
            # 初始化Layout，以设置居中选项
            lay_out = QHBoxLayout(cell_widget)
            lay_out.addWidget(chk_bx)
            lay_out.addWidget(btn)
            lay_out.setAlignment(QtCore.Qt.AlignCenter)
            lay_out.setContentsMargins(0, 0, 0, 0)
            # 为Widget添加layout
            cell_widget.setLayout(lay_out)
            self.table1.setCellWidget(rowPosition, 1, cell_widget)

            # 为第三部分添加删除按钮
            cell_widget = QWidget()
            btn = QtWidgets.QPushButton()
            # 绘制删除按钮
            btn.setText('删除')
            btn.setStyleSheet("""
                QPushButton {
                    width:45px;
                    height:22px;
                    color: white;
                    background:rgba(215,73,73,1);
                    border-radius:3px;
                }
                QPushButton:pressed {
                    width:45px;
                    height:22px;
                    background:#ef8787;
                    border-radius:3px;
                }
                              """)
            btn.clicked.connect(self.delFile1)
            # 设置layout
            lay_out = QHBoxLayout(cell_widget)
            lay_out.addWidget(btn)
            lay_out.setAlignment(QtCore.Qt.AlignCenter)
            lay_out.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(lay_out)
            self.table1.setCellWidget(rowPosition, 2, cell_widget)

        return 0

    def openFile2(self):
        """TODO合并为一个
        """
        openFileHandler = openFDialog('')
        if hasattr(openFileHandler, 'fileName'):
            fname = os.path.basename(openFileHandler.fileName)
            if fname in self.contents:
                openFileHandler.hide()
                PopupWindow("选择文件已存在")

                return 1 

            self.contents[fname] = [openFileHandler.fileName, 0]
            rowPosition = self.table2.rowCount()
            if rowPosition == 1:
                text = self.table2.item(0, 0)
                if text is None or text.text() == '':
                    rowPosition = 0
                else:
                    self.table2.insertRow(rowPosition)
            else:
                self.table2.insertRow(rowPosition)
            item = QtWidgets.QTableWidgetItem()
            item.setText(fname)
            item.setToolTip(fname)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
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

            cell_widget = QWidget()
            btn = QtWidgets.QPushButton()
            btn.setText('删除')
            btn.setStyleSheet("""
                QPushButton {
                    width:45px;
                    height:22px;
                    color: white;
                    background:rgba(215,73,73,1);
                    border-radius:3px;
                }
                QPushButton:pressed {
                    width:45px;
                    height:22px;
                    background:#ef8787;
                    border-radius:3px;
                }
                              """)
            btn.clicked.connect(self.delFile2)
            lay_out = QHBoxLayout(cell_widget)
            lay_out.addWidget(btn)
            lay_out.setAlignment(QtCore.Qt.AlignCenter)
            lay_out.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(lay_out)
            self.table2.setCellWidget(rowPosition, 2, cell_widget)

        return 0

    def openFile3(self):
        """TODO合并为一个
        """
        openFileHandler = openFDialog('')
        if hasattr(openFileHandler, 'fileName'):
            fname = os.path.basename(openFileHandler.fileName)
            if fname in self.contents:
                openFileHandler.hide()
                PopupWindow("选择文件已存在")

                return 1 

            self.contents[fname] = [openFileHandler.fileName, 0]
            rowPosition = self.table3.rowCount()
            if rowPosition == 1:
                text = self.table3.item(0, 0)
                if text is None or text.text() == '':
                    rowPosition = 0
                else:
                    self.table3.insertRow(rowPosition)
            else:
                self.table3.insertRow(rowPosition)
            item = QtWidgets.QTableWidgetItem()
            item.setText(fname)
            item.setToolTip(fname)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
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

            cell_widget = QWidget()
            btn = QtWidgets.QPushButton()
            btn.setText('删除')
            btn.setStyleSheet("""
                QPushButton {
                    width:45px;
                    height:22px;
                    color: white;
                    background:rgba(215,73,73,1);
                    border-radius:3px;
                }
                QPushButton:pressed {
                    width:45px;
                    height:22px;
                    background:#ef8787;
                    border-radius:3px;
                }
                              """)
            btn.clicked.connect(self.delFile3)
            lay_out = QHBoxLayout(cell_widget)
            lay_out.addWidget(btn)
            lay_out.setAlignment(QtCore.Qt.AlignCenter)
            lay_out.setContentsMargins(18, 0, 0, 0)
            cell_widget.setLayout(lay_out)
            self.table3.setCellWidget(rowPosition, 2, cell_widget)

        return 0

    def openFile4(self):
        """TODO合并为一个
        """
        openFileHandler = openFDialog('')
        if hasattr(openFileHandler, 'fileName'):
            fname = os.path.basename(openFileHandler.fileName)
            if fname in self.contents:
                openFileHandler.hide()
                PopupWindow("选择文件已存在")

                return 1 

            self.contents[fname] = [openFileHandler.fileName, 0]
            rowPosition = self.table4.rowCount()
            if rowPosition == 1:
                text = self.table4.item(0, 0)
                if text is None or text.text() == '':
                    rowPosition = 0
                else:
                    self.table4.insertRow(rowPosition)
            else:
                self.table4.insertRow(rowPosition)
            item = QtWidgets.QTableWidgetItem()
            item.setText(fname)
            item.setToolTip(fname)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
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

            cell_widget = QWidget()
            btn = QtWidgets.QPushButton()
            btn.setText('删除')
            btn.setStyleSheet("""
                QPushButton {
                    width:45px;
                    height:22px;
                    color: white;
                    background:rgba(215,73,73,1);
                    border-radius:3px;
                }
                QPushButton:pressed {
                    width:45px;
                    height:22px;
                    background:#ef8787;
                    border-radius:3px;
                }
                              """)
            btn.clicked.connect(self.delFile4)
            lay_out = QHBoxLayout(cell_widget)
            lay_out.addWidget(btn)
            lay_out.setAlignment(QtCore.Qt.AlignCenter)
            lay_out.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(lay_out)
            self.table4.setCellWidget(rowPosition, 2, cell_widget)

        return 0

    def delFile1(self):
        chCliked = self.table1.sender()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table1.indexAt(posWidget).row()
        rowCount = self.table1.rowCount()
        fname = self.table1.item(rowIndex, 0).text()
        self.contents.pop(fname)
        if rowCount == 1:
            self.table1.setItem(0, 0, None)
            self.table1.setCellWidget(0, 1, None)
            self.table1.setCellWidget(0, 2, None)
        else:
            self.table1.removeRow(rowIndex)

        return 0

    def delFile2(self):
        chCliked = self.table2.sender()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table2.indexAt(posWidget).row()
        rowCount = self.table2.rowCount()
        fname = self.table2.item(rowIndex, 0).text()
        self.contents.pop(fname)
        if rowCount == 1:
            self.table2.setItem(0, 0, None)
            self.table2.setCellWidget(0, 1, None)
            self.table2.setCellWidget(0, 2, None)
        else:
            self.table2.removeRow(rowIndex)

        return 0

    def delFile3(self):
        chCliked = self.table3.sender()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table3.indexAt(posWidget).row()
        rowCount = self.table3.rowCount()
        fname = self.table3.item(rowIndex, 0).text()
        self.contents.pop(fname)
        if rowCount == 1:
            self.table3.setItem(0, 0, None)
            self.table3.setCellWidget(0, 1, None)
            self.table3.setCellWidget(0, 2, None)
        else:
            self.table3.removeRow(rowIndex)

        return 0

    def delFile4(self):
        chCliked = self.table4.sender()
        posWidget = chCliked.parent().pos()
        rowIndex = self.table4.indexAt(posWidget).row()
        rowCount = self.table4.rowCount()
        fname = self.table4.item(rowIndex, 0).text()
        self.contents.pop(fname)
        if rowCount == 1:
            self.table4.setItem(0, 0, None)
            self.table4.setCellWidget(0, 1, None)
            self.table4.setCellWidget(0, 2, None)
        else:
            self.table4.removeRow(rowIndex)

        return 0

    def getDataList(self):
        data = OrderedDict()
        for tab in [self.table1, self.table2, self.table3, self.table4]:
            i = 0
            while i < tab.rowCount():
                item = tab.item(i, 0)
                if item is None or item.text() == '':
                    i += 1
                    continue
                fname = tab.item(i, 0).text()
                data[fname] = self.contents[fname]
                i += 1

        return data

    def convert(self):
        data = self.getDataList()
        c = FullConverter(data)
        c.run_thread()
        while c.outfile is None and c.errcode == 0:
            sleep(1)
            print(c.state, c.prgbar_val, c.prgbar_max)
        saveDialog = saveFDialog()
        copyfile(c.outfile, saveDialog.saveName)

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
