import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel,
    QToolBar, QStatusBar, QMessageBox
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbar Example")
        self.setGeometry(100, 100, 400, 300)

        # ویجت مرکزی
        self.label = QLabel("Welcome to the Toolbar App!", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        # Toolbar
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        # اکشن خروج با آیکن
        exit_action = QAction(QIcon.fromTheme("application-exit"), "Exit", self)
        exit_action.setStatusTip("Exit the application")
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close_app)
        toolbar.addAction(exit_action)

        # اکشن درباره
        about_action = QAction(QIcon.fromTheme("help-about"), "About", self)
        about_action.setStatusTip("About the app")
        about_action.setShortcut("Ctrl+I")
        about_action.triggered.connect(self.show_about)
        toolbar.addAction(about_action)

        # نوار وضعیت پایین
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def close_app(self):
        reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.close()

    def show_about(self):
        QMessageBox.information(self, "About", "This app was built by Ali using PyQt6!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
