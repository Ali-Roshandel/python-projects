from info_window import *

from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QCheckBox, QRadioButton


class EmployeeManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.validator = InfoWindow()

        # Main window features
        self.setWindowTitle("Employee Manager")
        self.setWindowIcon(QIcon("employee_icon.png"))
        self.setGeometry(300, 300, 1030, 450)

        # Central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Entity
        self.name_input = QLineEdit(self)
        self.email_input = QLineEdit(self)

        self.position_input = QComboBox(self)
        self.position_input.addItems(["Manager", "Marketing", "Accounting", "HR",
                                      "IT", "Finance", "Documentation", "Other"])

        self.active_checkbox = QCheckBox("Active")

        self.male_input = QRadioButton("Male")
        self.female_input = QRadioButton("Female")

        self.description_input = QTextEdit(self)

        # Buttons
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_to_table)

        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.edit_table)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_from_table)

        self.clear_button = QPushButton("Clear Table")
        self.clear_button.clicked.connect(self.clear_table)

        self.setStyleSheet(self.setStyleSheet("""
                    QPushButton {
                        padding: 6px 10px;
                        font-weight: bold;
                    }
                """))

        # Table
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Name", "Email", "Position", "Active", "Gender"])

        # Radio button layout
        self.radio_layout = QHBoxLayout()
        self.radio_layout.addWidget(self.male_input)
        self.radio_layout.addWidget(self.female_input)

        # Entity layout
        self.entity_layout = QFormLayout()
        self.entity_layout.addRow("Name:", self.name_input)
        self.entity_layout.addRow("Email:", self.email_input)
        self.entity_layout.addRow("Position:", self.position_input)
        self.entity_layout.addRow("Activity:", self.active_checkbox)
        self.entity_layout.addRow("Gender:", self.radio_layout)
        self.entity_layout.addRow("Description:", self.description_input)

        # Button layout
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.edit_button)
        self.button_layout.addWidget(self.delete_button)
        self.button_layout.addWidget(self.clear_button)

        # Table layout
        self.table_layout = QVBoxLayout()
        self.table_layout.addLayout(self.button_layout)
        self.table_layout.addWidget(self.table)

        # Main layout
        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.entity_layout)
        self.main_layout.addLayout(self.table_layout)

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

    # Create action for menubar
    def create_action(self, title, icon, status_tip, status_shortcut, func):
        item = QAction(QIcon.fromTheme(icon), title, self)
        item.setStatusTip(status_tip)
        item.setShortcut(status_shortcut)
        item.triggered.connect(func)
        return item

    def save_file(self):
        pass

    def load_file(self):
        pass

    def show_about(self):
        QMessageBox.about(self, "About", "This is an Employee Manager Application. "
                                         "This is the final project by Ali Roshandel.")

    def add_to_table(self):
        pass

    def edit_table(self):
        pass

    def delete_from_table(self):
        pass

    def clear_table(self):
        pass


# Run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = EmployeeManager()
    main_window.show()
    sys.exit(app.exec())
