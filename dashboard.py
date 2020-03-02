# Author: Trevor Knutson
# Created on: 03/02/2020
# Description: The application's dashboard with data visualizations and report statistics

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Dashboard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    # Define all widgets here to be displayed
    # This should be called in the init method
    def create_widgets(self):
        figure = Figure(figsize=(5, 5), dpi=100)
        axes = figure.add_subplot(1, 1, 1)
        axes.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.get_tk_widget().pack(expand=True)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        toolbar = NavigationToolbar2Tk(canvas, self)
        canvas._tkcanvas.pack(expand=True)


# Window setup and definition
root = tk.Tk()
root.geometry('1000x700')
root.title("Noridian Audit Application")
app = Dashboard(master=root)
app.mainloop()
