import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QWidget


# Create the Application
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('GUI Test')
window.setGeometry(500, 500, 700, 350)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

layout = QVBoxLayout()

item = QLineEdit('Some Input', parent=window)
button = QPushButton('Some Button', parent=window)

layout.addWidget(helloMsg)
layout.addWidget(item)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
