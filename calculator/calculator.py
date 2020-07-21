#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2 import QtCore
# импортируем связанный py файл с нашим ui файлом
from design_calculator import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)


        # Соединим сигналы со слотами
        self.ui.b0.clicked.connect(self.pushed_button)
        self.ui.b1.clicked.connect(self.pushed_button)
        self.ui.b2.clicked.connect(self.pushed_button)
        self.ui.b3.clicked.connect(self.pushed_button)
        self.ui.b4.clicked.connect(self.pushed_button)
        self.ui.b5.clicked.connect(self.pushed_button)
        self.ui.b6.clicked.connect(self.pushed_button)
        self.ui.b7.clicked.connect(self.pushed_button)
        self.ui.b8.clicked.connect(self.pushed_button)
        self.ui.b9.clicked.connect(self.pushed_button)

        self.ui.bclear.clicked.connect(self.pushed_button)
        self.ui.bbackspace.clicked.connect(self.pushed_button)

        self.ui.bplus.clicked.connect(self.pushed_button)
        self.ui.bplus_minus.clicked.connect(self.pushed_button)
        self.ui.bmultiplication.clicked.connect(self.pushed_button)
        self.ui.bdivision.clicked.connect(self.pushed_button)
        self.ui.bcomma.clicked.connect(self.pushed_button)
        self.ui.bequal.clicked.connect(self.pushed_button)

        self.screen = ''
        self.plus_minus = True

    # функция при нажатии на кнопку
    def pushed_button(self):
        button = self.sender()
        self.screen += button.text()
        
        if button.text() == 'C':
            self.screen = ''
        elif button.text() == '<':
            self.screen = self.screen[:-2]
        elif button.text() == ',':
            self.screen = self.screen[:-1]+'.'
        elif button.text() == '+/-':
            # закончили здесь
            self.screen = ''
            if self.plus_minus:
                self.screen = '-'+self.screen
                self.plus_minus = False
            else:
                self.screen = self.screen
                self.plus_minus = True
        elif button.text() == '=':
            self.screen = str(eval(self.screen[:-1]))

        self.ui.line.setText(self.screen)


    
     

if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())
