import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("coffee.sqlite")
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable("coffee_types")
        model.select()

        self.tableView.setModel(model)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Coffee()
    ui.show()
    sys.exit(app.exec_())