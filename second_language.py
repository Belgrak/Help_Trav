# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_language.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_second_language(object):
    def setupUi(self, second_language):
        second_language.setObjectName("second_language")
        second_language.resize(548, 355)
        self.verticalLayoutWidget = QtWidgets.QWidget(second_language)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 40, 160, 203))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.russian = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.russian.setObjectName("russian")
        self.verticalLayout.addWidget(self.russian)
        self.null_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.null_2.setObjectName("null_2")
        self.verticalLayout.addWidget(self.null_2)
        self.turkish = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.turkish.setObjectName("turkish")
        self.verticalLayout.addWidget(self.turkish)
        self.bt_ok = QtWidgets.QPushButton(second_language)
        self.bt_ok.setGeometry(QtCore.QRect(220, 290, 75, 23))
        self.bt_ok.setObjectName("bt_ok")

        self.retranslateUi(second_language)
        QtCore.QMetaObject.connectSlotsByName(second_language)

    def retranslateUi(self, second_language):
        _translate = QtCore.QCoreApplication.translate
        second_language.setWindowTitle(_translate("second_language", "Form"))
        self.russian.setText(_translate("second_language", "Русский"))
        self.null_2.setText(_translate("second_language", "Отсутствует"))
        self.turkish.setText(_translate("second_language", "Турецкий"))
        self.bt_ok.setText(_translate("second_language", "Ok"))
