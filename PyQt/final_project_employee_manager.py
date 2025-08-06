from main_window_base import *
from PyQt.main_window_base import MainWindowBase


class EmployeeManager(MainWindowBase):
    def __init__(self):
        super().__init__("Employee Manager", "employee_icon.png", 300, 300, 1030, 450)

        # Central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Entry
        self.name_input = self.create_entry("line_edit")
        self.email_input = self.create_entry("line_edit")

        self.position_input = self.create_combobox(["Manager", "Marketing", "Accounting", "HR",
                                                    "IT", "Finance", "Documentation", "Other"])

        self.active_checkbox = self.create_checkbox("Active")

        self.gender_input = self.create_radio_button("Male", "Female", default="Male")

        self.description_input = self.create_entry("text_edit")

        # Buttons
        style = "padding: 6px 10px; font-weight: bold;"

        self.add_button = self.create_button("Add Employee", style=style, func=self.add_to_table)
        self.edit_button = self.create_button("Edit Employee", style=style, func=self.edit_table)
        self.delete_button = self.create_button("Delete Employee", style=style, func=self.delete_from_table)
        self.clear_button = self.create_button("Clear Table", style=style, func=self.clear_table)

        # Table
        labels = ["Name", "Email", "Position", "Active", "Gender", "Description"]
        self.table = self.create_table(6, labels=labels, no_editable=True)

        # Radio button layout
        self.radio_layout = QHBoxLayout()
        for button in self.gender_input:
            self.radio_layout.addWidget(button)

        # Entry layout
        entry_items = {"Name": self.name_input, "Email": self.email_input,
                 "Position": self.position_input, "Gender": self.radio_layout,
                 "Activity": self.active_checkbox, "Description": self.description_input}
        self.entry_layout = self.add_form_layout(entry_items)

        # Button layout
        button_items = [self.add_button, self.edit_button, self.delete_button, self.clear_button]
        self.button_layout = self.add_layout(layout_type="horizontal", widget_list=button_items)

        # Table and button layout
        self.table_and_button_layout = self.add_layout(layout_list=[self.button_layout], widget_list=[self.table])

        # Main layout
        main_items = [self.entry_layout, self.table_and_button_layout]
        self.main_layout = self.add_layout(layout_type="horizontal", layout_list=main_items)

        self.central_widget.setLayout(self.main_layout)

        # Status bar
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

        # Menubar
        self.create_menubar()

    def create_menubar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        # file_menu.addAction(self.create_action("Save", "document-save", "Save Employee Information",
        #                                        "Ctrl+S", )
        #                     )
        # file_menu.addAction(self.create_action("Load", "document-open", "Load Employee Information",
        #                                        "Ctrl+O", )
        #                     )
        file_menu.addAction(self.create_action("Exit", "application-exit", "Exit the App",
                                               "Ctrl+Q", self.close))

        help_menu = menubar.addMenu("Help")
        help_menu.addAction(self.create_action("About", "help-about", "About the App",
                                               "Ctrl+H", self.show_about)
                            )

    def form_validator(self, name, email):
        if not name or not email:
            QMessageBox.warning(self, "Missing Info", "Please fill all the fields")
            self.status_bar.showMessage("Incomplete Fields", 3000)
            return False

        if not name_regex(name):
            QMessageBox.critical(self, "Invalid Name", "Please enter a valid name")
            self.status_bar.showMessage("Invalid Name", 3000)
            self.name_input.clear()
            self.name_input.setFocus()
            return False

        if not email_address_regex(email):
            QMessageBox.critical(self, "Invalid Email", "Please enter a valid email")
            self.status_bar.showMessage("Invalid Email", 3000)
            self.email_input.clear()
            self.email_input.setFocus()
            return False

        if self.name_duplicate(name, skip_row=self.table.currentRow()):
            QMessageBox.critical(self, "Duplicate Name", "Name already exists")
            self.status_bar.showMessage("Duplicate Name", 3000)
            self.name_input.clear()
            self.name_input.setFocus()
            return False

        if self.email_duplicate(email, skip_row=self.table.currentRow()):
            QMessageBox.critical(self, "Duplicate Email", "Email already exists")
            self.status_bar.showMessage("Duplicate Email", 3000)
            self.email_input.clear()
            self.email_input.setFocus()
            return False

        return True

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

    def save_file(self):
        pass

    def load_file(self):
        pass

    def show_about(self):
        QMessageBox.about(self, "About", "This is an Employee Manager Application. "
                                         "This is the final project by Ali Roshandel.")

    def add_to_table(self):
        name = self.name_input.text().strip().lower()
        email = self.email_input.text().strip()
        position = self.position_input.currentText()
        active = "Yes" if self.active_checkbox.isChecked() else "No"
        gender = "Male" if self.gender_input[0].isChecked() else "Female"
        description = self.description_input.toPlainText()

        if self.form_validator(name, email):
            row = self.table.rowCount()
            self.table.insertRow(row)

            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(email))
            self.table.setItem(row, 2, QTableWidgetItem(position))
            self.table.setItem(row, 3, QTableWidgetItem(active))
            self.table.setItem(row, 4, QTableWidgetItem(gender))
            self.table.setItem(row, 5, QTableWidgetItem(description))

            self.status_bar.showMessage("Employee Added", 3000)
            QMessageBox.information(self, "Successful Add", f" Employee {name} is added successfully.")
            self.clear_fields()

    def edit_table(self):
        pass

    def delete_from_table(self):
        pass

    def clear_table(self):
        self.table.setRowCount(0)
        self.clear_fields()
        self.status_bar.showMessage("Cleared", 3000)

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.position_input.setCurrentIndex(0)
        self.active_checkbox.setChecked(False)
        self.gender_input[0].setChecked(True)


# Run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = EmployeeManager()
    main_window.show()
    sys.exit(app.exec())
