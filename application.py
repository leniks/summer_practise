import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QScrollArea, QFormLayout, QGroupBox, QLabel, \
    QVBoxLayout, QLineEdit, QMainWindow
import json


class MainWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.resize(400, 800)

        formLayout = QFormLayout()
        groupBox = QGroupBox()

        labelList = []
        buttonList = []

        # x, y = 10, 10

        for elem in self.data:
            labelList.append(QLabel())
            button = QPushButton(f'{elem["first_name"]} {elem["last_name"]} id: {elem["id"]}', self)
            button.clicked.connect(self.get_info)
            buttonList.append(button)
            # button.resize(250, 20)
            # button.move(x, y)
            # y += 30
            formLayout.addRow(QLabel(), button)

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(800)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)

    def get_info(self):
        sender = self.sender()
        id = sender.text().split()[3]
        for elem in data:
            if str(elem['id']) == id:
                person = elem
                self.infowindow = InfoWindow(elem)
                self.infowindow.show()


class InfoWindow(QMainWindow):
    def __init__(self, elem):
        super().__init__()
        self.data = data
        self.resize(400, 400)

        self.textbox = QLineEdit()
        self.setCentralWidget(self.textbox)

        self.textbox.setText(str(elem['id']))


app = QApplication(sys.argv)

with open('data.json') as json_file:
    data = json.load(json_file)

window = MainWindow(data)
window.show()

app.exec()
