# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 119)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.btnGen = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnGen.setFont(font)
        self.btnGen.setObjectName("btnGen")
        self.gridLayout.addWidget(self.btnGen, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.btnVal = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnVal.setFont(font)
        self.btnVal.setObjectName("btnVal")
        self.gridLayout.addWidget(self.btnVal, 0, 3, 1, 1)
        self.inputCpf = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputCpf.setFont(font)
        self.inputCpf.setObjectName("inputCpf")
        self.gridLayout.addWidget(self.inputCpf, 0, 1, 1, 1)
        self.lineReturn = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineReturn.setFont(font)
        self.lineReturn.setText("")
        self.lineReturn.setAlignment(QtCore.Qt.AlignCenter)
        self.lineReturn.setReadOnly(True)
        self.lineReturn.setObjectName("lineReturn")
        self.gridLayout.addWidget(self.lineReturn, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerador / Validador de CPF"))
        self.label_2.setText(_translate("MainWindow", "Valida CPF:"))
        self.btnGen.setText(_translate("MainWindow", "Gerar"))
        self.label.setText(_translate("MainWindow", " Gera CPF:"))
        self.btnVal.setText(_translate("MainWindow", "Validar"))
