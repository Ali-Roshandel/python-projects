import sys
import os

import pandas as pd

from PyQt6.QtGui import QIcon, QAction

from regex.regex_practice import *

from PyQt6.QtWidgets import (QApplication, QWidget, QFormLayout, QMessageBox, QPushButton,
                             QStatusBar, QHBoxLayout, QVBoxLayout, QLineEdit,
                             QTextEdit, QTableWidget, QTableWidgetItem, QComboBox,
                             QMainWindow, QCheckBox, QLabel, QRadioButton
                             )


class MainWindowBase(QMainWindow):
    def __init__(self, title, icon=None, x=200, y=200, width=350, height=250):
        super().__init__()

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.setGeometry(x, y, width, height)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

    def create_label(self, title, align=None, style=None):
        label = QLabel(self, title)
        label.setAlignment(align)
        label.setStyleSheet(style)

        return label

    def create_entry(self, entry_type="line_edit", read_only=False, holder_text=None, hide_pass=False):
        if entry_type == "line_edit":
            entry = QLineEdit()
        elif entry_type == "text_edit":
            entry = QTextEdit()
        else:
            raise NotImplementedError

        entry.setReadOnly(read_only)
        entry.setPlaceholderText(holder_text)
        entry.setEchoMode(QLineEdit.EchoMode.Password) if hide_pass else None

        return entry

    @staticmethod
    def create_button(title, icon=None, style=None, func=None):
        button = QPushButton(title)
        button.setStyleSheet(style)
        if icon:
            button.setIcon(icon)
        if func:
            button.clicked.connect(func)

        return button

    @staticmethod
    def create_checkbox(title, state=False, func=None):
        checkbox = QCheckBox(title)
        checkbox.setChecked(state)
        if func:
            checkbox.stateChanged.connect(func)

        return checkbox

    @staticmethod
    def create_combobox(items):
        combobox = QComboBox()
        combobox.addItems(items)
        combobox.setCurrentIndex(0)

        return combobox

    @staticmethod
    def create_radio_button(*titles, default=None):
        buttons = []
        for title in titles:
            button = QRadioButton(title)
            if title == default:
                button.setChecked(True)
            buttons.append(button)

        return buttons

    def create_table(self, n_column=2, labels=None, func=None, no_editable=False):
        table = QTableWidget(self)
        table.setColumnCount(n_column)
        table.setHorizontalHeaderLabels(labels)
        if func is not None:
            table.cellClicked.connect(func)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers) if no_editable else None

        return table

    def create_action(self, title, icon, status_tip, status_shortcut, func=None):
        item = QAction(QIcon.fromTheme(icon), title, self)
        item.setStatusTip(status_tip)
        item.setShortcut(status_shortcut)
        if func:
            item.triggered.connect(func)

        return item

    @staticmethod
    def add_row_to_table(table, row, *fields):
        table.insertRow(row)

        for i, field in enumerate(fields):
            table.setItem(row, i, QTableWidgetItem(field))

    @staticmethod
    def edit_row_from_table(table, *fields):
        row = table.currentRow()

        for i, field in enumerate(fields):
            table.setItem(row, i, QTableWidgetItem(field))

    @staticmethod
    def get_data_from_table(table, row):
        items = []
        for column in range(table.columnCount()):
            items.append(table.item(row, column).text())

        return items

    def save_to_csv(self, table, filename, col_names):
        data_list = []
        employee = {}
        for row in range(table.rowCount()):
            for idx, col in enumerate(col_names):
                employee[col] = self.get_data_from_table(table, row)[idx]

            data_list.append(employee)

        df = pd.DataFrame.from_records(data_list, columns=col_names)
        df.to_csv(f"{filename}.csv", index=False)

    @staticmethod
    def load_from_file_to_table(file_path, table):
        df = pd.read_csv(file_path)
        table.setRowCount(len(df))

        for row in range(len(df)):
            for column in range(table.columnCount()):
                table.setItem(row, column, QTableWidgetItem(str(df.iloc[row, column])))

    @staticmethod
    def add_form_layout(widgets):
        form_layout = QFormLayout()
        for title, widget in widgets.items():
            form_layout.addRow(title, widget)

        return form_layout

    @staticmethod
    def add_layout(layout_type="vertical", widget_list=None, layout_list=None):
        if layout_type == "vertical":
            layout = QVBoxLayout()
        elif layout_type == "horizontal":
            layout = QHBoxLayout()
        else:
            raise NotImplementedError

        if widget_list:
            for widget in widget_list:
                layout.addWidget(widget)

        if layout_list:
            for layouts in layout_list:
                layout.addLayout(layouts)

        return layout

    @staticmethod
    def duplicate_in_table(table, column, text, skip_row=None):
        for row in range(table.rowCount()):
            if skip_row is not None and skip_row == row:
                continue
            if table.item(row, column).text() == text:
                return True
        return False

    @staticmethod
    def check_fields(*fields):
        for field in fields:
            if not field:
                return False
        return True

    @staticmethod
    def entry_validator(validator_type, text):
        if validator_type == "name":
            return name_regex(text)
        elif validator_type == "email":
            return email_address_regex(text)
        elif validator_type == "national_id":
            return national_code_regex(text)
        elif validator_type == "address":
            return address_regex(text)
        elif validator_type == "phone_number":
            return phone_number_regex(text)
        else:
            raise NotImplementedError

    def yes_no_question(self, title, message):
        return QMessageBox.question(self, title, message,
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
