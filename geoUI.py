# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\python\geo\geoUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 764)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cities = QtWidgets.QTextEdit(self.centralwidget)
        self.cities.setObjectName("cities")
        self.verticalLayout.addWidget(self.cities)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.id = QtWidgets.QTextEdit(self.centralwidget)
        self.id.setObjectName("id")
        self.verticalLayout.addWidget(self.id)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.not_found = QtWidgets.QTextEdit(self.centralwidget)
        self.not_found.setMinimumSize(QtCore.QSize(0, 100))
        self.not_found.setMaximumSize(QtCore.QSize(16777215, 100))
        self.not_found.setObjectName("not_found")
        self.verticalLayout.addWidget(self.not_found)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.region = QtWidgets.QCheckBox(self.centralwidget)
        self.region.setObjectName("region")
        self.verticalLayout.addWidget(self.region)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cities:"))
        self.label_2.setText(_translate("MainWindow", "Id:"))
        self.label_3.setText(_translate("MainWindow", "Сities not found:"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.region.setText(_translate("MainWindow", "Москва или(и) Питер с областью"))
