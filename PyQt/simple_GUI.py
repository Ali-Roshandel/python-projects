import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QLabel, QLineEdit, QCheckBox, QMessageBox
)


class LoginWindow(QWidget):
    """
    This is the main window of the application.
    """

    def __init__(self, title, x, y, width, height):
        super().__init__()

        self.welcome_window = None

        self.setWindowTitle(title)  # Set Title
        self.setGeometry(x, y, width, height)  # Set location and size

        self.label = QLabel("Welcome! Please login")  # Set label
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Move label to center
        self.label.setStyleSheet("""
            color:white;
            font-size:18px;
            font-weight:bold;
        """)

        # Username/Password entry
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Hiding password

        # Password checkbox
        self.show_pass_checkbox = QCheckBox("Show Password")
        self.show_pass_checkbox.setChecked(False)
        self.show_pass_checkbox.stateChanged.connect(self.show_password)

        self.button = QPushButton("Login")  # Set button
        self.button.setStyleSheet("""
            QPushButton {
                font-size:18px;
                font-family:Arial;
                padding:10px;
                border: 1px solid #333;
                border-radius:10px;
            }
            QPushButton:hover {
                color:green;
                background-color:#333;
            }
        """)
        self.button.clicked.connect(self.login)  # Connect button to the function

        # Vertical layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.show_pass_checkbox)

        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #222;")

    # Login function
    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        if username == "Ali" and password == "1234":
            # self.label.setText(f"Hello and Welcome {username}!")
            # self.label.setStyleSheet("color: green; font-size:14px; font-weight:bold")  # Change label color
            # self.setStyleSheet("background-color: black ;") # Turn the whole page black
            QMessageBox.information(self, "Success", "You are now logged in!")
            self.welcome_window = WelcomeWindow("Success", 100, 100,
                                                300, 150, username
                                                )
            self.welcome_window.show()
            self.close()
            # self.hide()
        elif not username or not password:
            # self.label.setText("Please enter both fields")
            # self.label.setStyleSheet("color: orange; font-size:14px; font-weight:bold")
            QMessageBox.warning(self, "Warning", "Please enter both fields")
        else:
            # self.label.setText("Invalid username or password")
            # self.label.setStyleSheet("color:red; font-size:14px; font-weight:bold")
            QMessageBox.critical(self, "Error", "Invalid username or password")

    # Show password checkbox function
    def show_password(self):
        if self.show_pass_checkbox.isChecked():
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    # Clear all fields
    def reset_fields(self):
        self.username_input.clear()
        self.password_input.clear()
        self.show_pass_checkbox.setChecked(False)
        self.label.setText("Welcome! Please login")


class WelcomeWindow(QWidget):
    def __init__(self, title, x, y, width, height, username):
        super().__init__()

        self.login_window = login_window

        self.setWindowTitle(title)
        self.setGeometry(x, y, width, height)

        # label for welcome
        self.label = QLabel(f"Welcome Back {username}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("color:green; font-size:18px; font-weight:bold;")

        # Logout button
        self.button = QPushButton("Logout")
        self.button.setStyleSheet("""
            QPushButton {
                color:white;
                font-size:18px;
                font-family:Arial;
                padding:10px;
                border: 1px solid #333;
                border-radius:10px;
            }
            QPushButton:hover {
                color:red;
                background-color:#333;
            }
        """)
        self.button.clicked.connect(self.logout)

        # Vertical layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def logout(self):
        reply = QMessageBox.question(self, "Confirm Logout", "Are you sure to logout?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                                     )

        if reply == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, "Success", "You are now logged out!")
            self.login_window.welcome_window.close()
            self.login_window.show()
            self.login_window.reset_fields()


# Example
app = QApplication(sys.argv)
login_window = LoginWindow("Login Form", 100, 100, 300, 200)
login_window.show()
sys.exit(app.exec())
