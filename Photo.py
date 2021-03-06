# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Photo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class PhotoCatch(object):
    def setupUi(self, PhotoCatch):
        PhotoCatch.setObjectName("PhotoCatch")
        PhotoCatch.resize(850, 600)
        PhotoCatch.setMinimumSize(QtCore.QSize(850, 600))
        PhotoCatch.setMaximumSize(QtCore.QSize(850, 600))
        self.centralwidget = QtWidgets.QWidget(PhotoCatch)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.realized = QtWidgets.QPushButton(self.centralwidget)
        self.realized.setMinimumSize(QtCore.QSize(200, 50))
        self.realized.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.realized.setFont(font)
        self.realized.setObjectName("realized")
        self.gridLayout.addWidget(self.realized, 2, 0, 1, 1)
        self.hotkey = QtWidgets.QLineEdit(self.centralwidget)
        self.hotkey.setMinimumSize(QtCore.QSize(180, 50))
        self.hotkey.setMaximumSize(QtCore.QSize(180, 50))
        self.hotkey.setObjectName("hotkey")
        self.gridLayout.addWidget(self.hotkey, 4, 1, 1, 1)
        self.photoget = QtWidgets.QLabel(self.centralwidget)
        self.photoget.setMinimumSize(QtCore.QSize(200, 200))
        self.photoget.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.photoget.setFont(font)
        self.photoget.setAlignment(QtCore.Qt.AlignCenter)
        self.photoget.setObjectName("photoget")
        self.gridLayout.addWidget(self.photoget, 1, 0, 1, 1)
        self.reaction = QtWidgets.QPushButton(self.centralwidget)
        self.reaction.setMinimumSize(QtCore.QSize(200, 50))
        self.reaction.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.reaction.setFont(font)
        self.reaction.setObjectName("reaction")
        self.gridLayout.addWidget(self.reaction, 4, 0, 1, 1)
        self.catch_2 = QtWidgets.QPushButton(self.centralwidget)
        self.catch_2.setMinimumSize(QtCore.QSize(200, 50))
        self.catch_2.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.catch_2.setFont(font)
        self.catch_2.setObjectName("catch_2")
        self.gridLayout.addWidget(self.catch_2, 0, 0, 1, 1)
        self.TureGesture = QtWidgets.QLabel(self.centralwidget)
        self.TureGesture.setMinimumSize(QtCore.QSize(200, 50))
        self.TureGesture.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.TureGesture.setFont(font)
        self.TureGesture.setAlignment(QtCore.Qt.AlignCenter)
        self.TureGesture.setObjectName("TureGesture")
        self.gridLayout.addWidget(self.TureGesture, 3, 0, 1, 1)
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setMinimumSize(QtCore.QSize(200, 50))
        self.Back.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.Back.setFont(font)
        self.Back.setObjectName("Back")
        self.gridLayout.addWidget(self.Back, 4, 3, 1, 1)
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setMinimumSize(QtCore.QSize(500, 400))
        self.photo.setMaximumSize(QtCore.QSize(500, 400))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.photo.setFont(font)
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.gridLayout.addWidget(self.photo, 0, 1, 3, 1)
        self.hotkey2 = QtWidgets.QLineEdit(self.centralwidget)
        self.hotkey2.setMinimumSize(QtCore.QSize(180, 50))
        self.hotkey2.setMaximumSize(QtCore.QSize(180, 50))
        self.hotkey2.setObjectName("hotkey2")
        self.gridLayout.addWidget(self.hotkey2, 4, 2, 1, 1)
        PhotoCatch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PhotoCatch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        PhotoCatch.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PhotoCatch)
        self.statusbar.setObjectName("statusbar")
        PhotoCatch.setStatusBar(self.statusbar)

        self.retranslateUi(PhotoCatch)
        QtCore.QMetaObject.connectSlotsByName(PhotoCatch)

    def retranslateUi(self, PhotoCatch):
        _translate = QtCore.QCoreApplication.translate
        PhotoCatch.setWindowTitle(_translate("PhotoCatch", "MainWindow"))
        self.realized.setText(_translate("PhotoCatch", "重启"))
        self.photoget.setText(_translate("PhotoCatch", "获取图片"))
        self.reaction.setText(_translate("PhotoCatch", "绑定"))
        self.catch_2.setText(_translate("PhotoCatch", "捕获"))
        self.TureGesture.setText(_translate("PhotoCatch", "是否识别成功"))
        self.Back.setText(_translate("PhotoCatch", "退出"))
        self.photo.setText(_translate("PhotoCatch", "视频"))

