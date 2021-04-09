# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proj_trav.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(370, 40, 551, 111))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(510, 120, 251, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bt_calc = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_calc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_calc.setStyleSheet("background-color: rgb(120, 147, 139);\n"
"font: 75 16pt \"Bahnschrift Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.bt_calc.setObjectName("bt_calc")
        self.verticalLayout.addWidget(self.bt_calc)
        self.bt_country = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_country.setEnabled(True)
        self.bt_country.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_country.setStyleSheet("background-color: rgb(120, 147, 139);\n"
"font: 75 16pt \"Bahnschrift Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.bt_country.setObjectName("bt_country")
        self.verticalLayout.addWidget(self.bt_country)
        self.bt_city = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_city.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_city.setStyleSheet("background-color: rgb(120, 147, 139);\n"
"font: 75 16pt \"Bahnschrift Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.bt_city.setObjectName("bt_city")
        self.verticalLayout.addWidget(self.bt_city)
        self.bt_cafe = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_cafe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_cafe.setStyleSheet("background-color: rgb(120, 147, 139);\n"
"font: 75 16pt \"Bahnschrift Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.bt_cafe.setObjectName("bt_cafe")
        self.verticalLayout.addWidget(self.bt_cafe)
        self.bt_sight = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_sight.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_sight.setStyleSheet("background-color: rgb(120, 147, 139);\n"
"font: 75 16pt \"Bahnschrift Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.bt_sight.setObjectName("bt_sight")
        self.verticalLayout.addWidget(self.bt_sight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Help/Trav"))
        self.bt_calc.setText(_translate("MainWindow", "Калькулятор стоимости"))
        self.bt_country.setText(_translate("MainWindow", "Поиск страны"))
        self.bt_city.setText(_translate("MainWindow", "Поиск города"))
        self.bt_cafe.setText(_translate("MainWindow", "Поиск кафе"))
        self.bt_sight.setText(_translate("MainWindow", "Поиск развлечений"))
