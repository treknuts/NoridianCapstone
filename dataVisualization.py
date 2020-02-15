import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5.QtWidgets import *


class GraphWithQtDemo(QWidget):
    def __init__(self, parent = None):
        super(GraphWithQtDemo, self).__init__(parent)
        self.layout = QGridLayout()
        self.title = QLabel('<h1>Graph Demo</h1>', parent=self)
        self.m = PlotCanvas(self, width=5, height=4)
        self.m.move(0, 0)

        self.button = QPushButton('PyQt5 button', self)
        self.button.setToolTip('This s an example button')
        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.m, 1, 0)
        self.layout.addWidget(self.button, 3, 3)

        self.show()


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
        data = np.random.randint(1, 21, (5, 5))
        ax = self.figure.add_subplot(1, 1, 1)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()


def main():
    app = QApplication(sys.argv)
    window = GraphWithQtDemo()
    window.setLayout(window.layout)
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

