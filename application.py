import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import json


class MainWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.data = data

        x, y = 10, 10
        for elem in self.data:
            button = QPushButton(f'{elem["first_name"]} {elem["last_name"]} id: {elem["id"]}', self)
            button.resize(250, 20)
            button.move(x, y)
            y += 30
            button.clicked.connect(self.get_info)

    def get_info(self):
        sender = self.sender()
        id = sender.text().split()[3]
        for elem in data:
            if str(elem['id']) == id:
                print(elem)


app = QApplication(sys.argv)

with open('data.json') as json_file:
    data = json.load(json_file)

window = MainWindow(data)
window.show()

app.exec()
