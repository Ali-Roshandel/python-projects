from main_window_base import *


class EmployeeManager(MainWindowBase):
    def __init__(self):
        super().__init__("Employee Manager", "employee_icon.png", 300, 300, 1030, 450)

        # Entry
        self.name_input = self.create_entry("line_edit")
        self.email_input = self.create_entry("line_edit")

        combo_items = ["Manager", "Marketing", "Accounting", "HR", "IT", "Finance", "Documentation", "Other"]
        self.position_input = self.create_combobox(combo_items)

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
        self.table = self.create_table(6, labels=labels, no_editable=True, func=self.load_from_table)

        # Radio button layout
        self.radio_layout = self.add_layout("horizontal", widget_list=self.gender_input)

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

        # Menubar
        self.create_menubar()

    def create_menubar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        file_menu.addAction(self.create_action("Save", "document-save", "Save Employee Information",
                                               "Ctrl+S", )
                            )
        file_menu.addAction(self.create_action("Load", "document-open", "Load Employee Information",
                                               "Ctrl+O", )
                            )
        file_menu.addAction(self.create_action("Exit", "application-exit", "Exit the App",
                                               "Ctrl+Q", self.close))

        help_menu = menubar.addMenu("Help")
        help_menu.addAction(self.create_action("About", "help-about", "About the App",
                                               "Ctrl+H", self.show_about)
                            )

    def form_validator(self, name, email):
        if not self.check_fields(name, email):
            QMessageBox.warning(self, "Missing Info", "Please fill all the fields")
            self.status_bar.showMessage("Incomplete Fields", 3000)
            return False

        if not self.entry_validator("name", name):
            QMessageBox.critical(self, "Invalid Name", "Please enter a valid name")
            self.status_bar.showMessage("Invalid Name", 3000)
            self.name_input.clear()
            self.name_input.setFocus()
            return False

        if not self.entry_validator("email", email):
            QMessageBox.critical(self, "Invalid Email", "Please enter a valid email")
            self.status_bar.showMessage("Invalid Email", 3000)
            self.email_input.clear()
            self.email_input.setFocus()
            return False

        if self.duplicate_in_table(self.table, 0, name, self.table.currentRow()):
            QMessageBox.critical(self, "Duplicate Name", "Name already exists")
            self.status_bar.showMessage("Duplicate Name", 3000)
            self.name_input.clear()
            self.name_input.setFocus()
            return False

        if self.duplicate_in_table(self.table, 1, email, self.table.currentRow()):
            QMessageBox.critical(self, "Duplicate Email", "Email already exists")
            self.status_bar.showMessage("Duplicate Email", 3000)
            self.email_input.clear()
            self.email_input.setFocus()
            return False

        return True

    def save_file(self):
        pass

    def load_file(self):
        pass

    def show_about(self):
        QMessageBox.about(self, "About", "This is an Employee Manager Application. "
                                         "This is the final project by Ali Roshandel.")

    def get_data(self):
        name = self.name_input.text().strip().lower()
        email = self.email_input.text().strip()
        position = self.position_input.currentText()
        active = "Yes" if self.active_checkbox.isChecked() else "No"
        gender = "Male" if self.gender_input[0].isChecked() else "Female"
        description = self.description_input.toPlainText()
        return name, email, position, active, gender, description

    def load_from_table(self, row):
        name, email, position, active, gender, description = self.get_data_from_table(self.table, row)

        self.name_input.setText(name)
        self.email_input.setText(email)
        self.position_input.setCurrentText(position)
        self.active_checkbox.setChecked(True if active == "Yes" else False)
        self.gender_input[0].setChecked(True) if gender == "Male" else self.gender_input[1].setChecked(True)
        self.description_input.setText(description)

    def add_to_table(self):
        name, email, position, active, gender, description = self.get_data()

        if self.form_validator(name, email):
            self.add_row_to_table(self.table, name, email, position, active, gender, description)

            self.status_bar.showMessage("Employee Added", 3000)
            QMessageBox.information(self, "Successful Add", f" Employee {name} is added successfully.")
            self.clear_fields()

    def edit_table(self):
        name, email, position, active, gender, description = self.get_data()

        if self.form_validator(name, email):
            self.edit_row_from_table(self.table, name, email, position, active, gender, description)

            QMessageBox.information(self, "Successful Edit", " Information has been updated.")
            self.status_bar.showMessage("Updated", 3000)
            self.clear_fields()

    def delete_from_table(self):
        row = self.table.currentRow()

        if row < 0:
            QMessageBox.critical(self, "Error", "Please select a row")
        else:
            reply = self.yes_no_question("Remove Employee", "Do you want to remove this employee?")
            if reply == QMessageBox.StandardButton.Yes:
                self.table.removeRow(row)

                QMessageBox.information(self, "Info Removed", "Info has been removed.")
                self.status_bar.showMessage("Info Removed", 3000)

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
        self.description_input.clear()


# Run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = EmployeeManager()
    main_window.show()
    sys.exit(app.exec())
