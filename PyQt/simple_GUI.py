import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit


class LoginWindow(QWidget):
    """
    This is the main window of the application.
    """

    def __init__(self, title, x, y, width, height):
        super().__init__()

        self.setWindowTitle(title)  # Set Title
        self.setGeometry(x, y, width, height)  # Set location and size

        self.label = QLabel("Welcome! Please login")  # Set label
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Move label to center
        self.label.setStyleSheet("""
            color:white;
            font-size:18px;
            font-weight:bold;
        """)

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

        # Username/Password entry
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Hiding password

        # Vertical layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    # Function
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "Ali" and password == "1234":
            self.label.setText(f"Hello and Welcome {username}!")
            self.label.setStyleSheet("color: green; font-size:14px")  # Change label color
            self.setStyleSheet("background-color: Blue;")
        else:
            self.label.setText("Invalid username or password")
            self.label.setStyleSheet("color:red; font-size:14px; font-weight:bold")


# Example
app = QApplication(sys.argv)
my_window = LoginWindow("Login Form", 100, 100, 300, 200)
my_window.show()
sys.exit(app.exec())
