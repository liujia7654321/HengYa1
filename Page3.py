# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from tkinter.filedialog import asksaveasfilename
import tkinter as tk
import csv

class Ui_Page3(object):
    def setupUi(self, Page3):
        Page3.setObjectName("Page3")
        Page3.resize(1221, 727)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/icon/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Page3.setWindowIcon(icon)
        self.pushButton_7 = QtWidgets.QPushButton(Page3)
        self.pushButton_7.setGeometry(QtCore.QRect(1080, 580, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(" QPushButton {\n"
"color: #333;\n"
"border: 2px solid #3465a4;\n"
"font:bold 14pt \"Arial\";\n"
"text-align:center;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #888a85);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #898a88);\n"
"}\n"
"\n"
" QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #8a8a89);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox = QtWidgets.QGroupBox(Page3)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 1061, 631))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 1041, 601))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(Page3)
        self.label.setGeometry(QtCore.QRect(470, 10, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_8 = QtWidgets.QPushButton(Page3)
        self.pushButton_8.setGeometry(QtCore.QRect(1080, 650, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(" QPushButton {\n"
"color: #333;\n"
"border: 2px solid #3465a4;\n"
"font:bold 14pt \"Arial\";\n"
"text-align:center;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #888a85);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #898a88);\n"
"}\n"
"\n"
" QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #8a8a89);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_2 = QtWidgets.QPushButton(Page3)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 510, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(" QPushButton {\n"
"color: #333;\n"
"border: 2px solid #3465a4;\n"
"font:bold 14pt \"Arial\";\n"
"text-align:center;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #888a85);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #898a88);\n"
"}\n"
"\n"
" QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #8a8a89);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Page3)
        self.pushButton_3.setGeometry(QtCore.QRect(1080, 440, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(" QPushButton {\n"
"color: #333;\n"
"border: 2px solid #3465a4;\n"
"font:bold 14pt \"Arial\";\n"
"text-align:center;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #888a85);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #898a88);\n"
"}\n"
"\n"
" QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.89, stop: 0 #fff, stop: 1 #8a8a89);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Page3)
        QtCore.QMetaObject.connectSlotsByName(Page3)

    def retranslateUi(self, Page3):
        _translate = QtCore.QCoreApplication.translate
        Page3.setWindowTitle(_translate("Page3", "压缩指数表"))
        self.pushButton_7.setText(_translate("Page3", "生成表格"))
        self.groupBox.setTitle(_translate("Page3", "实时数据列表"))
        self.label.setText(_translate("Page3", "恒压过滤数据处理软件V1.0"))
        self.pushButton_8.setText(_translate("Page3", "生成曲线"))
        self.pushButton_2.setText(_translate("Page3", "清 空"))
        self.pushButton_3.setText(_translate("Page3", "删除行"))


    def InitTableWidget(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        L = []
        L.append("斜率")
        L.append("截距")
        L.append("压差ΔP(Pa)")
        L.append("K(m³/m².s)")
        L.append("qe(m³/m²)")
        L.append("θe(s)")
        L.append("lgΔP")
        L.append("lgK")
        L.append("添加到曲线")
        self.tableWidget.setColumnCount(len(L))
        self.tableWidget.setHorizontalHeaderLabels(L)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 94)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 140)
        self.tableWidget.setColumnWidth(4, 140)

        self.tableWidget.setColumnWidth(5, 110)
        self.tableWidget.setColumnWidth(6, 110)
        self.tableWidget.setColumnWidth(7, 110)
        self.tableWidget.setColumnWidth(8, 108)

    def AddTableWidget(self, L=[]):
        num = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(num + 1)
        list = L
        try:
            for i in range(0, len(list)):
                newItem = QTableWidgetItem(str(list[i]))
                newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.tableWidget.setItem(num, i, newItem)
            self.check = QtWidgets.QTableWidgetItem()
            self.check.setCheckState(QtCore.Qt.Checked)
            self.tableWidget.setItem(num, len(list), self.check)
        except Exception as e:
            print(e)

    def init(self):

        # 导出csv按钮
        self.pushButton_7.clicked.connect(self.handleSave)
        # 删除行
        self.pushButton_3.clicked.connect(self.remove_row)
        # 清空
        self.pushButton_2.clicked.connect(self.InitTableWidget)


        self.InitTableWidget()

    def Page3SetWive(self):
        rowCnt = self.tableWidget.rowCount()
        colCnt = self.tableWidget.columnCount()
        xlist = []
        ylist = []
        if not rowCnt > 2:
            msgBox = QtWidgets.QMessageBox()
            msgBox.information(msgBox, "提示", "数据不足！")
            return
        for row in range(0, rowCnt):
            b = self.tableWidget.item(row,colCnt-1).checkState()
            if b :
                x = float(self.tableWidget.item(row, colCnt - 3).text())
                y = float(self.tableWidget.item(row, colCnt - 2).text())
                xlist.append(x)
                ylist.append(y)
        return xlist,ylist

    def remove_row(self):
        index = self.tableWidget.selectedRanges()  # 1
        try:
            index = index[0].bottomRow()
            self.tableWidget.removeRow(index)
        except :
            msgBox = QtWidgets.QMessageBox()
            msgBox.critical(msgBox, "提示", "未选中行！")



    def handleSave(self):
        root = tk.Tk()
        root.withdraw()
        filepath = asksaveasfilename()
        path = filepath + '.csv'
        if filepath:
            file = open(path, 'w', encoding='utf-8', newline='' "")
            writer = csv.writer(file)
            L = []
            L.append("序号")
            L.append("斜率")
            L.append("截距")
            L.append("压差ΔP(Pa)")
            L.append("K(m³/m².s)")
            L.append("qe(m³/m²)")
            L.append("θe(s)")
            L.append("lgΔP")
            L.append("lgK")
            writer.writerow(L)
            for row in range(self.tableWidget.rowCount()):
                rowdata = []
                rowdata.append(str(row+1))
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item is not None:
                        rowdata.append(item.text())
                    else:
                        rowdata.append('')
                writer.writerow(rowdata)
            file.close()