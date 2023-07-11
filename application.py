import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QScrollArea, QFormLayout, QGroupBox, QLabel, \
    QVBoxLayout, QLineEdit, QMainWindow
import json
from script import call


class MainWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.resize(400, 800)

        formLayout = QFormLayout()
        groupBox = QGroupBox()

        labelList = []
        buttonList = []

        for elem in self.data:
            labelList.append(QLabel())
            button = QPushButton(f'{elem["first_name"]} {elem["last_name"]} id: {elem["id"]}', self)
            button.clicked.connect(self.get_info)
            buttonList.append(button)
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
                self.infowindow = InfoWindow(elem)
                self.infowindow.show()


class InfoWindow(QMainWindow):
    def __init__(self, elem):
        super().__init__()
        self.data = data
        self.resize(400, 400)

        self.textbox = QLabel()
        self.setCentralWidget(self.textbox)

        for string in elem:
            # print(string, end=': ')
            # print(elem[string])
            self.textbox.setText(self.textbox.text() + f'{string}: {elem[string]}\n')


call(380060730)
app = QApplication(sys.argv)

with open('data.json') as json_file:
    data = json.load(json_file)

window = MainWindow(data)
window.show()

app.exec()
