

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.layout = QGridLayout()
        self.title = QLabel('<h1>Bar Graph Demo</h1>', parent=self)
        self.graph = PlotCanvas(self, width=5, height=4)
        self.graph.move(0, 0)
        button = QPushButton('Push me!', self)
        button.clicked.connect(self.on_click)

        self.layout.addWidget(button, 3, 3)
        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.graph, 1, 0)

        self.show()

    @pyqtSlot()
    def on_click(self):
        show_dialog()


def show_dialog():
    message = QMessageBox()
    message.setIcon(QMessageBox.Information)
    message.setText('<h3>You pushed the button!</h3>')
    message.setWindowTitle('Pop up message example')
    message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    retval = message.exec_()
    print("value of pressed message box button:", retval)


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = [2, 9, 1, 7, 4]
        labels = ['error1', 'error2', 'error3', 'error4', 'error5']
        x_pos = [i for i, _ in enumerate(labels)]
        ax = self.figure.add_subplot(1, 1, 1)
        ax.bar(labels, data, color="brown")
        ax.set_title('Bar Graph')
        self.draw()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.setLayout(window.layout)
    window.setGeometry(50, 50, 1000, 600)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

