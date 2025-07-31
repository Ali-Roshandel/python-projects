import sys

from regex.regex_practice import name_regex, email_address_regex

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QPushButton,
                             QWidget, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout,
                             QFormLayout, QStatusBar
                             )


class ContactForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contact Form")
        self.setGeometry(300, 300, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Form entity
        self.name_field = QLineEdit(self)
        self.subject_field = QLineEdit(self)
        self.email_field = QLineEdit(self)
        self.message_field = QTextEdit(self)

        # Form button
        self.send_button = QPushButton("Send")
        self.send_button.setIcon(QIcon.fromTheme("mail-send"))
        self.send_button.clicked.connect(self.send_message)

        self.clear_button = QPushButton("Clear")
        self.clear_button.setIcon(QIcon.fromTheme("edit-clear"))
        self.clear_button.clicked.connect(self.clear_form)

        self.setStyleSheet("""
            QPushButton {
                padding: 6px 10px;
                font-weight: bold;
            }
        """)

        # Form layout
        form_layout = QFormLayout()
        form_layout.addRow("Name", self.name_field)
        form_layout.addRow("Subject", self.subject_field)
        form_layout.addRow("Email", self.email_field)
        form_layout.addRow("Message", self.message_field)

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.send_button)
        button_layout.addWidget(self.clear_button)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.central_widget.setLayout(main_layout)

        # Status bar
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

    def send_message(self):
        name = self.name_field.text().strip()
        subject = self.subject_field.text().strip()
        email = self.email_field.text().strip()
        message = self.message_field.toPlainText().strip()

        if not name or not email or not message:
            QMessageBox.warning(self, "Missing Info", "Please fill all fields")
            self.status_bar.showMessage("Form Incomplete", 3000)
            return

        elif not name_regex(name):
            QMessageBox.critical(self, "Invalid Name", "Please enter a valid name")
            self.status_bar.showMessage("Invalid Name", 3000)
            self.name_field.clear()
            return

        elif not email_address_regex(email):
            QMessageBox.critical(self, "Invalid Email", "Please enter a valid email address")
            self.status_bar.showMessage("Invalid Email", 3000)
            self.email_field.clear()
            return

        else:
            if not subject:
                reply = QMessageBox.question(self, "No Subject", "Do you want to send message without subject?",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.No:
                    self.status_bar.showMessage("Enter subject", 3000)
                    return

        QMessageBox.information(self, "Message sent", "Message sent successfully")
        self.status_bar.showMessage("Message sent", 3000)
        self.clear_form()

    def clear_form(self):
        self.name_field.clear()
        self.subject_field.clear()
        self.email_field.clear()
        self.message_field.clear()
        self.status_bar.showMessage("Form cleared", 3000)


# Example
if __name__ == "__main__":
    app = QApplication(sys.argv)
    contact_form = ContactForm()
    contact_form.show()
    sys.exit(app.exec())
