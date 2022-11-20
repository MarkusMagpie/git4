import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from main1 import Ui_main

class Menu(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("coffee.sqlite")
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT * FROM coffee").fetchall()
        if result:
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


def except_hook(cls, exception, traceback):  # функция для лёгкого поиска ошибок
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':  # запуск программы
    app = QApplication(sys.argv)
    m = Menu()
    m.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())