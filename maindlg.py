# -*- coding: utf-8 -*-

# Copyright (C) 2018  RedLotus <ssfdust@gmail.com>
# Author: RedLotus <ssfdust@gmail.com>
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1197, 653)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1197, 653))
        Dialog.setMaximumSize(QtCore.QSize(1197, 653))
        Dialog.setStyleSheet("")
        self.table1 = QtWidgets.QTableWidget(Dialog)
        self.table1.setGeometry(QtCore.QRect(45, 72, 342, 230))
        self.table1.setStyleSheet("QHeaderView{\n"
"    background:#fffff8;\n"
"}\n"
"QTableWidgetItem {\n"
"    text-align:right;\n"
"}\n"
"QTableView QHeaderView::section {\n"
"    padding-left:24px;\n"
"}\n"
"QHeaderView::section::horizontal {\n"
"    color: #FCFCFC;\n"
"    width: 50px;\n"
"    height: 37px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    border: 0px;\n"
"}\n"
"QTableView{\n"
"    gridline-color: #fffff8;\n"
"}\n"
"QTableView::item{\n"
"    height:32px;\n"
"    border-bottom: 1px solid  #C6C6C6;\n"
"}\n"
"QHeaderView::section::vertical{\n"
"    text-align: right;\n"
"    width:20px;\n"
"    height:32px;\n"
"    background: #fffff8;\n"
"    border-style: none;\n"
"    border-bottom: 0.5px solid  #C6C6C6;\n"
"}")
        self.table1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table1.setShowGrid(False)
        self.table1.setObjectName("table1")
        self.table1.setColumnCount(3)
        self.table1.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.table1.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.table1.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.table1.setItem(0, 2, item)
        self.select1 = QtWidgets.QPushButton(Dialog)
        self.select1.setGeometry(QtCore.QRect(320, 80, 45, 24))
        self.select1.setStyleSheet("QPushButton {\n"
"border-style: inset;\n"
"background:rgba(252,252,252,1);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(228, 228, 228);\n"
"border-style: outset;\n"
"}")
        self.select1.setFlat(False)
        self.select1.setObjectName("select1")
        self.table3 = QtWidgets.QTableWidget(Dialog)
        self.table3.setGeometry(QtCore.QRect(787, 72, 342, 230))
        self.table3.setStyleSheet("QHeaderView{\n"
"    background:#fffff8;\n"
"}\n"
"QTableWidgetItem {\n"
"    text-align:right;\n"
"}\n"
"QTableView QHeaderView::section {\n"
"    padding-left:24px;\n"
"}\n"
"QHeaderView::section::horizontal {\n"
"    color: #FCFCFC;\n"
"    width: 50px;\n"
"    height: 37px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    border: 0px;\n"
"}\n"
"QTableView{\n"
"    gridline-color: #fffff8;\n"
"}\n"
"QTableView::item{\n"
"    height:32px;\n"
"    border-bottom: 1px solid  #C6C6C6;\n"
"}\n"
"QHeaderView::section::vertical{\n"
"    text-align: right;\n"
"    width:20px;\n"
"    height:32px;\n"
"    background: #fffff8;\n"
"    border-style: none;\n"
"    border-bottom: 0.5px solid  #C6C6C6;\n"
"}")
        self.table3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table3.setShowGrid(False)
        self.table3.setObjectName("table3")
        self.table3.setColumnCount(3)
        self.table3.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.table3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.table3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.table3.setItem(0, 2, item)
        self.table2 = QtWidgets.QTableWidget(Dialog)
        self.table2.setGeometry(QtCore.QRect(416, 72, 342, 230))
        self.table2.setStyleSheet("QHeaderView{\n"
"    background:#fffff8;\n"
"}\n"
"QTableWidgetItem {\n"
"    text-align:right;\n"
"}\n"
"QTableView QHeaderView::section {\n"
"    padding-left:24px;\n"
"}\n"
"QHeaderView::section::horizontal {\n"
"    color: #FCFCFC;\n"
"    width: 50px;\n"
"    height: 37px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    border: 0px;\n"
"}\n"
"QTableView{\n"
"    gridline-color: #fffff8;\n"
"}\n"
"QTableView::item{\n"
"    height:32px;\n"
"    border-bottom: 1px solid  #C6C6C6;\n"
"}\n"
"QHeaderView::section::vertical{\n"
"    text-align: right;\n"
"    width:20px;\n"
"    height:32px;\n"
"    background: #fffff8;\n"
"    border-style: none;\n"
"    border-bottom: 0.5px solid  #C6C6C6;\n"
"}")
        self.table2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table2.setShowGrid(False)
        self.table2.setObjectName("table2")
        self.table2.setColumnCount(3)
        self.table2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.table2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.table2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.table2.setItem(0, 2, item)
        self.select2 = QtWidgets.QPushButton(Dialog)
        self.select2.setGeometry(QtCore.QRect(691, 80, 45, 24))
        self.select2.setStyleSheet("QPushButton {\n"
"background:rgba(252,252,252,1);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(228, 228, 228);\n"
"border-style: outset;\n"
"}")
        self.select2.setObjectName("select2")
        self.table4 = QtWidgets.QTableWidget(Dialog)
        self.table4.setGeometry(QtCore.QRect(45, 351, 342, 230))
        self.table4.setStyleSheet("QHeaderView{\n"
"    background:#fffff8;\n"
"}\n"
"QTableView QHeaderView::section {\n"
"    padding-left:24px;\n"
"}\n"
"QHeaderView::section::horizontal {\n"
"    color: #FCFCFC;\n"
"    width: 50px;\n"
"    height: 37px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    border: 0px;\n"
"}\n"
"QTableView{\n"
"    gridline-color: #fffff8;\n"
"}\n"
"QTableView::item{\n"
"    height:32px;\n"
"    border-bottom: 1px solid  #C6C6C6;\n"
"}\n"
"QHeaderView::section::vertical{\n"
"    text-align: right;\n"
"    width:20px;\n"
"    height:32px;\n"
"    background: #fffff8;\n"
"    border-style: none;\n"
"    border-bottom: 0.5px solid  #C6C6C6;\n"
"}")
        self.table4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table4.setShowGrid(False)
        self.table4.setObjectName("table4")
        self.table4.setColumnCount(3)
        self.table4.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.table4.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.table4.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.table4.setItem(0, 2, item)
        self.select4 = QtWidgets.QPushButton(Dialog)
        self.select4.setGeometry(QtCore.QRect(320, 359, 45, 24))
        self.select4.setStyleSheet("QPushButton {\n"
"background:rgba(252,252,252,1);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(228, 228, 228);\n"
"border-style: outset;\n"
"}")
        self.select4.setObjectName("select4")
        self.pic1 = QtWidgets.QLabel(Dialog)
        self.pic1.setGeometry(QtCore.QRect(461, 394, 160, 187))
        self.pic1.setStyleSheet("QLabel {\n"
"    border: 1px solid #C6C6C6;\n"
"}")
        self.pic1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pic1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pic1.setLineWidth(1)
        self.pic1.setText("")
        self.pic1.setPixmap(QtGui.QPixmap("../../../Downloads/14131077857079_former_shot.jpg"))
        self.pic1.setAlignment(QtCore.Qt.AlignCenter)
        self.pic1.setObjectName("pic1")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(47, 47, 8, 19))
        self.label1.setStyleSheet("#label1 {\n"
"background-color: #000000;\n"
"}")
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(417, 47, 8, 19))
        self.label2.setStyleSheet("#label, #label2,#label3,#label4 {\n"
"background-color: #000000;\n"
"}")
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(791, 47, 8, 19))
        self.label3.setStyleSheet("#label, #label2,#label3,#label4 {\n"
"background-color: #000000;\n"
"}")
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(Dialog)
        self.label4.setGeometry(QtCore.QRect(46, 326, 8, 19))
        self.label4.setStyleSheet("#label, #label2,#label3,#label4 {\n"
"background-color: #000000;\n"
"}")
        self.label4.setText("")
        self.label4.setObjectName("label4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(66, 48, 32, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(437, 49, 31, 15))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(810, 48, 64, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(46, 73, 56, 37))
        self.label_4.setStyleSheet("QLabel {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    color: #FCFCFC;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(417, 73, 56, 37))
        self.label_5.setStyleSheet("QLabel {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    color: #FCFCFC;\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(788, 73, 56, 37))
        self.label_6.setStyleSheet("QLabel {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    color: #FCFCFC;\n"
"}")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(65, 328, 31, 15))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(46, 352, 56, 37))
        self.label_8.setStyleSheet("QLabel {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    color: #FCFCFC;\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.select3 = QtWidgets.QPushButton(Dialog)
        self.select3.setGeometry(QtCore.QRect(1070, 80, 45, 24))
        self.select3.setStyleSheet("QPushButton {\n"
"background:rgba(252,252,252,1);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(228, 228, 228);\n"
"border-style: outset;\n"
"}")
        self.select3.setObjectName("select3")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(422, 390, 32, 41))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(422, 430, 31, 41))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(422, 470, 31, 41))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(422, 510, 31, 41))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(416, 352, 46, 230))
        self.label_13.setStyleSheet("QLabel {\n"
"    border: 1px solid #C6C6C6;\n"
"}")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(461, 352, 160, 43))
        self.label_14.setStyleSheet("QLabel {\n"
"    border: 1px solid #C6C6C6;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    color: white;\n"
"}")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(620, 352, 160, 43))
        self.label_15.setStyleSheet("QLabel {\n"
"    border: 1px solid #C6C6C6;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    color: white;\n"
"}")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(938, 352, 160, 43))
        self.label_16.setStyleSheet("QLabel {\n"
"    border: 1px solid #C6C6C6;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    color: white;\n"
"}")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(779, 352, 160, 43))
        self.label_17.setStyleSheet("QLabel {\n"
"    border: 1px solid #C6C6C6;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(14, 193, 214, 255), stop:1 rgba(14, 161, 216, 255));\n"
"    color: white;\n"
"}")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.pic2 = QtWidgets.QLabel(Dialog)
        self.pic2.setGeometry(QtCore.QRect(620, 394, 160, 187))
        self.pic2.setStyleSheet("QLabel {\n"
"    border: 1px solid #C6C6C6;\n"
"}")
        self.pic2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pic2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pic2.setLineWidth(1)
        self.pic2.setText("")
        self.pic2.setPixmap(QtGui.QPixmap("../../../Downloads/14131077857079_former_shot.jpg"))
        self.pic2.setAlignment(QtCore.Qt.AlignCenter)
        self.pic2.setObjectName("pic2")
        self.pic3 = QtWidgets.QLabel(Dialog)
        self.pic3.setGeometry(QtCore.QRect(779, 394, 160, 187))
        self.pic3.setStyleSheet("QLabel {\n"
"    border: 1px solid #C6C6C6;\n"
"}")
        self.pic3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pic3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pic3.setLineWidth(1)
        self.pic3.setText("")
        self.pic3.setPixmap(QtGui.QPixmap("../../../Downloads/14131077857079_former_shot.jpg"))
        self.pic3.setAlignment(QtCore.Qt.AlignCenter)
        self.pic3.setObjectName("pic3")
        self.pic4 = QtWidgets.QLabel(Dialog)
        self.pic4.setGeometry(QtCore.QRect(938, 394, 160, 187))
        self.pic4.setStyleSheet("QLabel {\n"
"    border: 1px solid #C6C6C6;\n"
"}")
        self.pic4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pic4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pic4.setLineWidth(1)
        self.pic4.setText("")
        self.pic4.setPixmap(QtGui.QPixmap("../../../Downloads/14131077857079_former_shot.jpg"))
        self.pic4.setAlignment(QtCore.Qt.AlignCenter)
        self.pic4.setObjectName("pic4")
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(847, 601, 105, 39))
        self.ok_btn.setStyleSheet("QPushButton {\n"
"width:105px;\n"
"height:39px;\n"
"background:rgba(14,164,216,1);\n"
"color: white;\n"
"border: 0px;\n"
"}\n"
"QPushButton:pressed {\n"
"background:rgb(16, 196, 255);\n"
"}")
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(1019, 601, 105, 39))
        self.cancel_btn.setStyleSheet("QPushButton {\n"
"width:105px;\n"
"height:39px;\n"
"border: 0px;\n"
"background:rgba(177,177,177,1);\n"
"color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(189, 189, 189);\n"
"}")
        self.cancel_btn.setObjectName("cancel_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pdf文件转换器"))
        item = self.table1.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.table1.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "文件名"))
        item = self.table1.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "是否盖章"))
        __sortingEnabled = self.table1.isSortingEnabled()
        self.table1.setSortingEnabled(False)
        self.table1.setSortingEnabled(__sortingEnabled)
        self.select1.setText(_translate("Dialog", "选择"))
        item = self.table3.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.table3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "文件名"))
        item = self.table3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "是否盖章"))
        __sortingEnabled = self.table3.isSortingEnabled()
        self.table3.setSortingEnabled(False)
        self.table3.setSortingEnabled(__sortingEnabled)
        item = self.table2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.table2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "文件名"))
        item = self.table2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "是否盖章"))
        __sortingEnabled = self.table2.isSortingEnabled()
        self.table2.setSortingEnabled(False)
        self.table2.setSortingEnabled(__sortingEnabled)
        self.select2.setText(_translate("Dialog", "选择"))
        item = self.table4.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.table4.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "文件名"))
        item = self.table4.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "是否盖章"))
        __sortingEnabled = self.table4.isSortingEnabled()
        self.table4.setSortingEnabled(False)
        self.table4.setSortingEnabled(__sortingEnabled)
        self.select4.setText(_translate("Dialog", "选择"))
        self.label.setText(_translate("Dialog", "正文"))
        self.label_2.setText(_translate("Dialog", "附件"))
        self.label_3.setText(_translate("Dialog", "发文稿纸"))
        self.label_4.setText(_translate("Dialog", "序号"))
        self.label_5.setText(_translate("Dialog", "序号"))
        self.label_6.setText(_translate("Dialog", "序号"))
        self.label_7.setText(_translate("Dialog", "其他"))
        self.label_8.setText(_translate("Dialog", "序号"))
        self.select3.setText(_translate("Dialog", "选择"))
        self.label_9.setText(_translate("Dialog", "盖"))
        self.label_10.setText(_translate("Dialog", "章"))
        self.label_11.setText(_translate("Dialog", "预"))
        self.label_12.setText(_translate("Dialog", "览"))
        self.label_14.setText(_translate("Dialog", "正文"))
        self.label_15.setText(_translate("Dialog", "附件"))
        self.label_16.setText(_translate("Dialog", "其他"))
        self.label_17.setText(_translate("Dialog", "发文稿纸"))
        self.ok_btn.setText(_translate("Dialog", "确认"))
        self.cancel_btn.setText(_translate("Dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

