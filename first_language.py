# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_language.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_first_language(object):
    def setupUi(self, first_language):
        first_language.setObjectName("first_language")
        first_language.resize(548, 355)
        self.verticalLayoutWidget = QtWidgets.QWidget(first_language)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 40, 160, 203))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.german = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.german.setObjectName("german")
        self.verticalLayout.addWidget(self.german)
        self.belorussian = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.belorussian.setObjectName("belorussian")
        self.verticalLayout.addWidget(self.belorussian)
        self.hungrian = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.hungrian.setObjectName("hungrian")
        self.verticalLayout.addWidget(self.hungrian)
        self.greek = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.greek.setObjectName("greek")
        self.verticalLayout.addWidget(self.greek)
        self.georgian = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.georgian.setObjectName("georgian")
        self.verticalLayout.addWidget(self.georgian)
        self.espaniol = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.espaniol.setObjectName("espaniol")
        self.verticalLayout.addWidget(self.espaniol)
        self.latvia = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.latvia.setObjectName("latvia")
        self.verticalLayout.addWidget(self.latvia)
        self.chezh = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chezh.setObjectName("chezh")
        self.verticalLayout.addWidget(self.chezh)
        self.estonian = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.estonian.setObjectName("estonian")
        self.verticalLayout.addWidget(self.estonian)
        self.bt_ok = QtWidgets.QPushButton(first_language)
        self.bt_ok.setGeometry(QtCore.QRect(220, 290, 75, 23))
        self.bt_ok.setObjectName("bt_ok")

        self.retranslateUi(first_language)
        QtCore.QMetaObject.connectSlotsByName(first_language)

    def retranslateUi(self, first_language):
        _translate = QtCore.QCoreApplication.translate
        first_language.setWindowTitle(_translate("first_language", "first_language"))
        self.german.setText(_translate("first_language", "Немецкий"))
        self.belorussian.setText(_translate("first_language", "Белорусский"))
        self.hungrian.setText(_translate("first_language", "Венгерский"))
        self.greek.setText(_translate("first_language", "Греческий"))
        self.georgian.setText(_translate("first_language", "Грузинский"))
        self.espaniol.setText(_translate("first_language", "Испанский"))
        self.latvia.setText(_translate("first_language", "Латышский"))
        self.chezh.setText(_translate("first_language", "Чешский"))
        self.estonian.setText(_translate("first_language", "Эстонский"))
        self.bt_ok.setText(_translate("first_language", "Ok"))
