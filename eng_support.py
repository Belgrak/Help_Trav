# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eng_support.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_eng_support(object):
    def setupUi(self, eng_support):
        eng_support.setObjectName("eng_support")
        eng_support.resize(548, 355)
        self.verticalLayoutWidget = QtWidgets.QWidget(eng_support)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 40, 160, 203))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nice = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.nice.setObjectName("nice")
        self.verticalLayout.addWidget(self.nice)
        self.middle = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.middle.setObjectName("middle")
        self.verticalLayout.addWidget(self.middle)
        self.bad = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.bad.setObjectName("bad")
        self.verticalLayout.addWidget(self.bad)
        self.bt_ok = QtWidgets.QPushButton(eng_support)
        self.bt_ok.setGeometry(QtCore.QRect(220, 290, 75, 23))
        self.bt_ok.setObjectName("bt_ok")

        self.retranslateUi(eng_support)
        QtCore.QMetaObject.connectSlotsByName(eng_support)

    def retranslateUi(self, eng_support):
        _translate = QtCore.QCoreApplication.translate
        eng_support.setWindowTitle(_translate("eng_support", "Form"))
        self.nice.setText(_translate("eng_support", "Хорошо"))
        self.middle.setText(_translate("eng_support", "Средне"))
        self.bad.setText(_translate("eng_support", "Плохо"))
        self.bt_ok.setText(_translate("eng_support", "Ok"))
