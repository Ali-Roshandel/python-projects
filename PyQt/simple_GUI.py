import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class MainWindow(QWidget):
    """
    This is the main window of the application.
    """
    def __init__(self, title , x, y, width, height):
        super().__init__()

        self.setWindowTitle(title)
        self.setGeometry(x, y, width, height)

        self.label = QLabel("My Label")
        self.button = QPushButton("My Button")

        self.button.clicked.connect(self.change_text)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


    def change_text(self):
        self.label.setText("Clicked")



# Example
app = QApplication(sys.argv)
my_window = MainWindow("My First Window", 100, 100, 300, 300)
my_window.show()
sys.exit(app.exec())


