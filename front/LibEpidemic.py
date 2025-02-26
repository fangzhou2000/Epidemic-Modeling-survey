# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LibEpidemic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QInputDialog, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("LibEpidemic Simulator Tool Version0.1")
        MainWindow.resize(1200, 900)
        MainWindow.setAccessibleName("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 40, 1161, 561))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 10, 72, 15))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(790, 700, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 700, 181, 31))
        self.label_2.setObjectName("label_2")
        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(230, 640, 481, 161))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.url.setFont(font)
        self.url.setObjectName("url")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubarbar = QtWidgets.QMenuBar(MainWindow)
        self.menubarbar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubarbar.setObjectName("menubarbar")
        self.menu = QtWidgets.QMenu(self.menubarbar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubarbar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Model = QtWidgets.QAction(MainWindow)
        self.actionNew_Model.setObjectName("actionNew_Model")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen_Model = QtWidgets.QAction(MainWindow)
        self.actionOpen_Model.setObjectName("actionOpen_Model")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menu.addAction(self.actionNew_Model)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionOpen_Model)
        self.menu.addAction(self.actionQuit)
        self.menubarbar.addAction(self.menu.menuAction())

        #画箭头
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("LibEpidemic Simulator Tool Version0.1", "LibEpidemic Simulator Tool Version0.1"))
        self.label.setText(_translate("LibEpidemic Simulator Tool Version0.1", ""))
        self.pushButton.setText(_translate("LibEpidemic Simulator Tool Version0.1", "OK"))
        self.label_2.setText(_translate("LibEpidemic Simulator Tool Version0.1", "Label"))
        self.menubarbar.setAccessibleName(_translate("LibEpidemic Simulator Tool Version0.1", "New"))
        self.menu.setTitle(_translate("LibEpidemic Simulator Tool Version0.1", "File"))
        self.actionNew_Model.setText(_translate("LibEpidemic Simulator Tool Version0.1", "New Model"))
        self.actionSave.setText(_translate("LibEpidemic Simulator Tool Version0.1", "Save"))
        self.actionOpen_Model.setText(_translate("LibEpidemic Simulator Tool Version0.1", "Open Model"))
        self.actionQuit.setText(_translate("LibEpidemic Simulator Tool Version0.1", "Quit"))
