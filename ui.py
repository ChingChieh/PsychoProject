# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(900, 16777215))
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QFrame(self.centralwidget)
        self.top.setStyleSheet("QFrame{ background-color : black}\n"
"")
        self.top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.verticalLayout.addWidget(self.top)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left = QtWidgets.QFrame(self.centralwidget)
        self.left.setStyleSheet("QFrame{ background-color : #FEBE4F}\n"
"")
        self.left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.left)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.src_1 = QtWidgets.QLabel(self.left)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.src_1.setFont(font)
        self.src_1.setStyleSheet("color : black;")
        self.src_1.setAlignment(QtCore.Qt.AlignCenter)
        self.src_1.setObjectName("src_1")
        self.horizontalLayout_6.addWidget(self.src_1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pos_1 = QtWidgets.QLabel(self.left)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pos_1.setFont(font)
        self.pos_1.setAutoFillBackground(False)
        self.pos_1.setStyleSheet("color : black;")
        self.pos_1.setAlignment(QtCore.Qt.AlignCenter)
        self.pos_1.setObjectName("pos_1")
        self.horizontalLayout_2.addWidget(self.pos_1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.left)
        self.mid = QtWidgets.QFrame(self.centralwidget)
        self.mid.setStyleSheet("QFrame{ background-color : #00B8B8}\n"
"")
        self.mid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mid.setObjectName("mid")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.mid)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem8)
        self.src_2 = QtWidgets.QLabel(self.mid)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.src_2.setFont(font)
        self.src_2.setStyleSheet("color : black;")
        self.src_2.setAlignment(QtCore.Qt.AlignCenter)
        self.src_2.setObjectName("src_2")
        self.horizontalLayout_16.addWidget(self.src_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.pos_2 = QtWidgets.QLabel(self.mid)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pos_2.setFont(font)
        self.pos_2.setAutoFillBackground(False)
        self.pos_2.setStyleSheet("color : black;")
        self.pos_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pos_2.setObjectName("pos_2")
        self.horizontalLayout_3.addWidget(self.pos_2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 2)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 1)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.mid)
        self.right = QtWidgets.QFrame(self.centralwidget)
        self.right.setStyleSheet("QFrame{ background-color : #FF6E6E}\n"
"")
        self.right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right.setObjectName("right")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.right)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem14)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem15)
        self.src_3 = QtWidgets.QLabel(self.right)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.src_3.setFont(font)
        self.src_3.setStyleSheet("color : black;")
        self.src_3.setAlignment(QtCore.Qt.AlignCenter)
        self.src_3.setObjectName("src_3")
        self.horizontalLayout_17.addWidget(self.src_3)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem16)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem17)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem18)
        self.pos_3 = QtWidgets.QLabel(self.right)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pos_3.setFont(font)
        self.pos_3.setAutoFillBackground(False)
        self.pos_3.setStyleSheet("color : black;")
        self.pos_3.setAlignment(QtCore.Qt.AlignCenter)
        self.pos_3.setObjectName("pos_3")
        self.horizontalLayout_4.addWidget(self.pos_3)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem19)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem20)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 2)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 1)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addWidget(self.right)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 8)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.src_1.setText(_translate("MainWindow", "0"))
        self.pos_1.setText(_translate("MainWindow", "ID : 1"))
        self.src_2.setText(_translate("MainWindow", "0"))
        self.pos_2.setText(_translate("MainWindow", "ID : 2"))
        self.src_3.setText(_translate("MainWindow", "0"))
        self.pos_3.setText(_translate("MainWindow", "ID : 3"))


