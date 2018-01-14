# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JsonDiff(object):
    def setupUi(self, JsonDiff):
        JsonDiff.setObjectName("JsonDiff")
        JsonDiff.resize(753, 600)
        self.centralwidget = QtWidgets.QWidget(JsonDiff)
        self.centralwidget.setObjectName("centralwidget")
        self.text_edit_left = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_edit_left.setGeometry(QtCore.QRect(21, 45, 350, 500))
        self.text_edit_left.setObjectName("text_edit_left")
        self.text_edit_right = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_edit_right.setGeometry(QtCore.QRect(381, 45, 350, 500))
        self.text_edit_right.setObjectName("text_edit_right")
        self.path_edit_left = QtWidgets.QLineEdit(self.centralwidget)
        self.path_edit_left.setGeometry(QtCore.QRect(21, 18, 310, 20))
        self.path_edit_left.setObjectName("path_edit_left")
        self.path_edit_right = QtWidgets.QLineEdit(self.centralwidget)
        self.path_edit_right.setGeometry(QtCore.QRect(381, 18, 310, 20))
        self.path_edit_right.setObjectName("path_edit_right")
        self.file_button_left = QtWidgets.QPushButton(self.centralwidget)
        self.file_button_left.setGeometry(QtCore.QRect(339, 18, 31, 20))
        self.file_button_left.setObjectName("file_button_left")
        self.file_button_right = QtWidgets.QPushButton(self.centralwidget)
        self.file_button_right.setGeometry(QtCore.QRect(699, 18, 31, 20))
        self.file_button_right.setObjectName("file_button_right")
        JsonDiff.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JsonDiff)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 21))
        self.menubar.setObjectName("menubar")
        JsonDiff.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JsonDiff)
        self.statusbar.setObjectName("statusbar")
        JsonDiff.setStatusBar(self.statusbar)

        self.retranslateUi(JsonDiff)
        QtCore.QMetaObject.connectSlotsByName(JsonDiff)

    def retranslateUi(self, JsonDiff):
        _translate = QtCore.QCoreApplication.translate
        JsonDiff.setWindowTitle(_translate("JsonDiff", "MainWindow"))
        self.file_button_left.setText(_translate("JsonDiff", "..."))
        self.file_button_right.setText(_translate("JsonDiff", "..."))

