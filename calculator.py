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
        self.ui.bclear.clicked.connect(self.clear)

    # функция при нажатии на кнопку
    def pushed_button(self):
        button = self.sender()
        btn = button.text()
        self.ui.line.setText(btn)

    def clear(self):
        self.ui.line.setText('')
     

if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())
