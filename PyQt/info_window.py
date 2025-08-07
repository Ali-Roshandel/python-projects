import sys

from regex.regex_practice import name_regex, email_address_regex

from PyQt6.QtWidgets import (QApplication, QWidget, QFormLayout, QMessageBox, QPushButton,
                             QStatusBar, QHBoxLayout, QVBoxLayout, QLineEdit,
                             QTextEdit, QTableWidget, QTableWidgetItem, QComboBox, QMainWindow
                             )


class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Info Window")
        self.setGeometry(200, 200, 450, 550)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Info entity
        self.input_name = QLineEdit(self)
        self.input_email = QLineEdit(self)

        self.input_job = QComboBox(self)
        self.input_job.addItems(["Student", "Web designer", "Professor", "Programmer", "Other"])

        self.input_message = QTextEdit(self)

        # Info button
        self.add_to_table_button = QPushButton("Add To Table")
        self.add_to_table_button.clicked.connect(self.add_to_table)

        self.clear_table_button = QPushButton("Clear Table")
        self.clear_table_button.clicked.connect(self.clear_table)

        self.edit_button = QPushButton("Edit Info")
        self.edit_button.clicked.connect(self.edit_info)

        self.remove_button = QPushButton("Remove Info")
        self.remove_button.clicked.connect(self.remove_info)

        self.setStyleSheet("""
                    QPushButton {
                        padding: 6px 10px;
                        font-weight: bold;
                    }
                """)

        # Info table
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Email", "Job", "Message"])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.cellClicked.connect(self.load_to_form)

        # Entity layout
        entity_layout = QFormLayout()
        entity_layout.addRow("Name", self.input_name)
        entity_layout.addRow("Email", self.input_email)
        entity_layout.addRow("Job", self.input_job)
        entity_layout.addRow("Message", self.input_message)

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_to_table_button)
        button_layout.addWidget(self.clear_table_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.remove_button)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(entity_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.table)

        self.central_widget.setLayout(main_layout)

        # Status bar
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

    def form_validator(self, name=None, email=None, message=" "):
        if not name or not email or not message:
            QMessageBox.warning(self, "Missing Info", "Please fill all the fields")
            self.status_bar.showMessage("Incomplete Fields", 3000)
            return False

        if not name_regex(name):
            QMessageBox.critical(self, "Invalid Name", "Please enter a valid name")
            self.status_bar.showMessage("Invalid Name", 3000)
            self.input_name.clear()
            self.input_name.setFocus()
            return False

        if not email_address_regex(email):
            QMessageBox.critical(self, "Invalid Email", "Please enter a valid email")
            self.status_bar.showMessage("Invalid Email", 3000)
            self.input_email.clear()
            self.input_email.setFocus()
            return False

        if self.name_duplicate(name, skip_row=self.table.currentRow()):
            QMessageBox.critical(self, "Duplicate Name", "Name already exists")
            self.status_bar.showMessage("Duplicate Name", 3000)
            self.input_name.clear()
            self.input_name.setFocus()
            return False

        if self.email_duplicate(email, skip_row=self.table.currentRow()):
            QMessageBox.critical(self, "Duplicate Email", "Email already exists")
            self.status_bar.showMessage("Duplicate Email", 3000)
            self.input_email.clear()
            self.input_email.setFocus()
            return False

        return True

    def add_to_table(self):
        name = self.input_name.text().strip().lower()
        email = self.input_email.text().strip()
        job = self.input_job.currentText()
        message = self.input_message.toPlainText()

        if self.form_validator(name, email, message):
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            self.table.setItem(row_position, 0, QTableWidgetItem(name))
            self.table.setItem(row_position, 1, QTableWidgetItem(email))
            self.table.setItem(row_position, 2, QTableWidgetItem(job))
            self.table.setItem(row_position, 3, QTableWidgetItem(message))

            self.status_bar.showMessage("Completed", 3000)
            QMessageBox.information(self, "Successful Add", f" Dear {name} your information has been added to table.")
            self.clear_fields()

    def load_to_form(self, row):
        name = self.table.item(row, 0).text()
        email = self.table.item(row, 1).text()
        job = self.table.item(row, 2).text()
        message = self.table.item(row, 3).text()

        self.input_name.setText(name)
        self.input_email.setText(email)
        self.input_job.setCurrentText(job)
        self.input_message.setText(message)

    def edit_info(self):
        name = self.input_name.text().strip().lower()
        email = self.input_email.text()
        job = self.input_job.currentText()
        message = self.input_message.toPlainText()

        if self.form_validator(name, email, message):
            row = self.table.currentRow()
            self.table.item(row, 0).setText(name)
            self.table.item(row, 1).setText(email)
            self.table.item(row, 2).setText(job)
            self.table.item(row, 3).setText(message)

            QMessageBox.information(self, "Successful Edit", " Information has been updated.")
            self.status_bar.showMessage("Updated", 3000)
            self.clear_fields()

    def remove_info(self):
        row = self.table.currentRow()

        if row < 0:
            QMessageBox.critical(self, "Error", "Please select a row")
        else:
            reply = QMessageBox.question(self, "Remove Record", "Are you sure to remove the record?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.table.removeRow(row)

                QMessageBox.information(self, "Info Removed", "Info has been removed.")
                self.status_bar.showMessage("Info Removed", 3000)
                self.clear_fields()

    def email_duplicate(self, email, skip_row=None):
        for row in range(self.table.rowCount()):
            if skip_row is not None and skip_row == row:
                continue
            if self.table.item(row, 1).text() == email:
                return True
        return False

    def name_duplicate(self, name, skip_row=None):
        for row in range(self.table.rowCount()):
            if skip_row is not None and skip_row == row:
                continue
            if self.table.item(row, 0).text() == name:
                return True
        return False

    def clear_fields(self):
        self.input_name.clear()
        self.input_email.clear()
        self.input_job.setCurrentText("Student")
        self.input_message.clear()

    def clear_table(self):
        self.table.setRowCount(0)
        self.clear_fields()
        self.status_bar.showMessage("Cleared", 3000)


# Example
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InfoWindow()
    window.show()
    sys.exit(app.exec())
