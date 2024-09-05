from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,  QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

Win = QWidget()
Win.setWindowTitle("Визначи переможця")
Win.move(100, 100)
Win.resize(400, 200)

button = QPushButton("Згенерувати")
text = QLabel("Натисніть щоб дізнатися переможця")
num = QLabel("?")

line = QVBoxLayout()
line.addWidget(text, alignment= Qt.AlignCenter)
line.addWidget(num, alignment= Qt.AlignCenter)
line.addWidget(button, alignment= Qt.AlignCenter)
Win.setLayout(line)

def show_num():
    number = randint(0, 99)
    num.setText(str(number))
    text.setText("Переможець:")

button.clicked.connect(show_num)

Win.show()
app.exec_()
