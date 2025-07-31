import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QStatusBar, QToolBar


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
        # self.statusBar().showMessage("You are now logged in")
        status_bar = QStatusBar(self)
        self.setStatusBar(status_bar)

        # Menubar
        # self.create_menu_bar()

        # Toolbar
        self.create_tool_bar()

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

    def create_tool_bar(self):
        tool_bar = QToolBar(self)
        self.addToolBar(tool_bar)

        exit_item = self.add_to_tool_bar("Exit", "application-exit", "Exit Main Window",
                                         "Ctrl+Q", self.close_app)
        about_item = self.add_to_tool_bar("About", "help-about", "About Main Window",
                                          "Ctrl+I", self.show_about)
        refresh_item = self.add_to_tool_bar("Refresh", "view-refresh", "Refresh Main Window",
                                            "ctrl+R", self.refresh_window)

        tool_bar.addAction(exit_item)
        tool_bar.addAction(about_item)
        tool_bar.addAction(refresh_item)

    def add_to_tool_bar(self, title, icon, status_tip, shortcut, func):
        item = QAction(QIcon.fromTheme(icon), title, self)
        item.setStatusTip(status_tip)
        item.setShortcut(shortcut)
        item.triggered.connect(func)
        return item

    def show_about(self):
        QMessageBox.information(self, "About", "This is a PyQt6 Qt Application created by Ali Roshandel")
        self.label.setText("Welcome to Main Window")

    def close_app(self):
        reply = QMessageBox.question(self, "Exit", "Are you sure to exit",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.close()

    def refresh_window(self):
        self.label.setText("Refreshed!")


# Example
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow("Main Window", 100, 100, 350, 150)
    main_window.show()
    sys.exit(app.exec())
