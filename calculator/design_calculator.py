# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 511)
        MainWindow.setMinimumSize(QSize(300, 511))
        MainWindow.setMaximumSize(QSize(300, 511))
        icon = QIcon()
        icon.addFile(u"img/calculator.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow\n"
"{\n"
"	background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"\n"
"QPushButton\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding: 15px;\n"
"	font: 18pt \"MS PGothic\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: rgb(33, 148, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 281, 492))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.line = QLabel(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 242))
        self.line.setStyleSheet(u"font: 72pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.line.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.bequal = QPushButton(self.verticalLayoutWidget)
        self.bequal.setObjectName(u"bequal")

        self.gridLayout.addWidget(self.bequal, 5, 3, 1, 1)

        self.b4 = QPushButton(self.verticalLayoutWidget)
        self.b4.setObjectName(u"b4")

        self.gridLayout.addWidget(self.b4, 2, 0, 1, 1)

        self.bbackspace = QPushButton(self.verticalLayoutWidget)
        self.bbackspace.setObjectName(u"bbackspace")

        self.gridLayout.addWidget(self.bbackspace, 0, 2, 1, 1)

        self.bplus = QPushButton(self.verticalLayoutWidget)
        self.bplus.setObjectName(u"bplus")

        self.gridLayout.addWidget(self.bplus, 4, 3, 1, 1)

        self.b0 = QPushButton(self.verticalLayoutWidget)
        self.b0.setObjectName(u"b0")

        self.gridLayout.addWidget(self.b0, 5, 1, 1, 1)

        self.b7 = QPushButton(self.verticalLayoutWidget)
        self.b7.setObjectName(u"b7")

        self.gridLayout.addWidget(self.b7, 4, 0, 1, 1)

        self.b9 = QPushButton(self.verticalLayoutWidget)
        self.b9.setObjectName(u"b9")

        self.gridLayout.addWidget(self.b9, 4, 2, 1, 1)

        self.bmultiplication = QPushButton(self.verticalLayoutWidget)
        self.bmultiplication.setObjectName(u"bmultiplication")

        self.gridLayout.addWidget(self.bmultiplication, 1, 3, 1, 1)

        self.bcomma = QPushButton(self.verticalLayoutWidget)
        self.bcomma.setObjectName(u"bcomma")

        self.gridLayout.addWidget(self.bcomma, 5, 2, 1, 1)

        self.bminus = QPushButton(self.verticalLayoutWidget)
        self.bminus.setObjectName(u"bminus")

        self.gridLayout.addWidget(self.bminus, 2, 3, 1, 1)

        self.bclear = QPushButton(self.verticalLayoutWidget)
        self.bclear.setObjectName(u"bclear")

        self.gridLayout.addWidget(self.bclear, 0, 1, 1, 1)

        self.b2 = QPushButton(self.verticalLayoutWidget)
        self.b2.setObjectName(u"b2")

        self.gridLayout.addWidget(self.b2, 1, 1, 1, 1)

        self.b3 = QPushButton(self.verticalLayoutWidget)
        self.b3.setObjectName(u"b3")

        self.gridLayout.addWidget(self.b3, 1, 2, 1, 1)

        self.bplus_minus = QPushButton(self.verticalLayoutWidget)
        self.bplus_minus.setObjectName(u"bplus_minus")

        self.gridLayout.addWidget(self.bplus_minus, 5, 0, 1, 1)

        self.b8 = QPushButton(self.verticalLayoutWidget)
        self.b8.setObjectName(u"b8")

        self.gridLayout.addWidget(self.b8, 4, 1, 1, 1)

        self.b5 = QPushButton(self.verticalLayoutWidget)
        self.b5.setObjectName(u"b5")

        self.gridLayout.addWidget(self.b5, 2, 1, 1, 1)

        self.bdivision = QPushButton(self.verticalLayoutWidget)
        self.bdivision.setObjectName(u"bdivision")

        self.gridLayout.addWidget(self.bdivision, 0, 3, 1, 1)

        self.bclear2 = QPushButton(self.verticalLayoutWidget)
        self.bclear2.setObjectName(u"bclear2")

        self.gridLayout.addWidget(self.bclear2, 0, 0, 1, 1)

        self.b1 = QPushButton(self.verticalLayoutWidget)
        self.b1.setObjectName(u"b1")
        self.b1.setStyleSheet(u"")

        self.gridLayout.addWidget(self.b1, 1, 0, 1, 1)

        self.b6 = QPushButton(self.verticalLayoutWidget)
        self.b6.setObjectName(u"b6")

        self.gridLayout.addWidget(self.b6, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.line.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bequal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.b4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.bbackspace.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.bplus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.b0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.b7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.b9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.bmultiplication.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.bcomma.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.bminus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.bclear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.bplus_minus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.b8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.b5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.bdivision.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.bclear2.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.b6.setText(QCoreApplication.translate("MainWindow", u"6", None))
    # retranslateUi

