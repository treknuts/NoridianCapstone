# Author: Trevor Knutson
# Created on: 03/02/2020
# Description: The application's dashboard with data visualizations and report statistics

from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Dashboard(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('1000x700')
        self.master.title("Noridian Audit Application")
        self.top_frame = Frame(self.master)
        self.top_frame.pack()
        self.bottom_frame = Frame(self.master)
        self.bottom_frame.pack(side=BOTTOM)
        self.create_bargraph(self.top_frame)
        self.create_widgets(self.bottom_frame)

    # Define all widgets here to be displayed
    # This should be called in the init method
    def create_bargraph(self, frame):
        figure = Figure(figsize=(5, 5), dpi=100)
        axes = figure.add_subplot(1, 1, 1)

        data = [2, 9, 1, 7, 4]
        labels = ['error1', 'error2', 'error3', 'error4', 'error5']
        x_pos = [i for i, _ in enumerate(labels)]
        axes.bar(labels, data, color="brown")
        axes.set_title('Bar Graph')
        axes.plot()

        canvas = FigureCanvasTkAgg(figure, frame)
        canvas.get_tk_widget().pack(expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self)
        canvas._tkcanvas.pack(expand=True)


    def create_widgets(self, frame):
        self.quit = Button(frame, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack()


# Window setup and definition
root = Tk()
# root.geometry('1000x700')
# root.title("Noridian Audit Application")
app = Dashboard(master=root)
app.mainloop()
