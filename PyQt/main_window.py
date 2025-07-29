import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel


class MainWindow(QMainWindow):
    def __init__(self, title, x, y, width, height):
        super().__init__()

        self.setWindowTitle(title)
        self.setGeometry(x, y, width, height)

        self.label = QLabel("Welcome to Main Window", self)
        self.label.setStyleSheet("color:green; font-size:17px; font-weight:bold")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        # Statusbar
        self.statusBar().showMessage("You are now logged in")

        # Menubar
        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")

        exit_item = QAction("Exit", self)
        exit_item.triggered.connect(self.close)
        file_menu.addAction(exit_item)

        # help menu
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def show_about(self):
        QMessageBox.information(self, "About", "This is a PyQt6 Qt Application created by Ali Roshandel")


# Example
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow("Main Window", 100, 100, 350, 150)
    main_window.show()
    sys.exit(app.exec())
