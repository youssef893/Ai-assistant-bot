import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QFont
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLineEdit
from bot import main


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")

        self.setWindowTitle('Poems Generator')
        self.resize(500, 720)

        # Create the text label
        self.label = QLabel("Hello Sir, How Can i Help you??", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Times', 20))
        self.label.setStyleSheet("background-color: black; color: white")

        # Create the Generate button
        self.send_button = QPushButton('Send', self)
        self.send_button.setFont(QFont('Times', 15))
        self.send_button.setStyleSheet("background-color: black; color:white")
        self.send_button.clicked.connect(self.send)

        # create text editor
        self.textbox = QLineEdit(self)
        self.textbox.setFont(QFont("Times", 15))
        self.textbox.setStyleSheet("background-color: black; color:white")
        self.textbox.returnPressed.connect(self.send_button.click)

        # create loading
        self.loading_label = QLabel(self)
        self.loading_label.setStyleSheet("background-color: black;")
        self.movie = QMovie("giphy.gif")
        self.loading_label.setMovie(self.movie)
        self.loading_label.show()

        # create the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.loading_label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.send_button)
        self.setLayout(layout)
        self.movie.start()

    def send(self):
        self.movie.stop()
        self.loading_label.hide()
        message = self.textbox.text()
        self.textbox.setText('')

        response = main(message)

        if str(response) == 'True':
            self.label.setText("Maybe this name is wrong or abbreviation, \n"
                               "try to write the correct name or choose it from the computer")
        elif str(response) == 'False':
            self.label.setText(message)
        else:
            self.label.setText(response)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
