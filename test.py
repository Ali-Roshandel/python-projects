import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QMenuBar,
    QMenu, QMessageBox
)


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App with QMainWindow")
        self.setGeometry(100, 100, 400, 300)

        # 👇 ایجاد یک محتوای مرکزی (Central Widget)
        self.label = QLabel("Welcome to the App!", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        # 👇 منوبار
        menubar = self.menuBar()

        # 👇 منوی اصلی
        file_menu = menubar.addMenu("File")
        help_menu = menubar.addMenu("Help")

        # 👇 اکشن‌ها
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)

        # 👇 افزودن اکشن‌ها به منو
        file_menu.addAction(exit_action)
        help_menu.addAction(about_action)

        # 👇 نوار وضعیت
        self.statusBar().showMessage("Ready")

    def show_about(self):
        QMessageBox.information(self, "About", "This is a simple PyQt6 app!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
