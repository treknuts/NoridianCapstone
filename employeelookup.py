from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas
import dataVisualization as dv


class EmployeeLookup(Frame):
    def __init__(self, parent=None, data=None, employee=None):
        self.parent = parent
        self.data = data
        self.employee = data[0][6][8:]

        emp_label = Label(self.parent, text=self.employee, font=("Courier", 24))
        emp_label.grid(row=0, column=0)

        top_categories = Label(self.parent, text="{}'s Top 5 Categories".format(self.employee), font=("Courier", 18))
        top_categories.grid(row=1, column=0)

        line_label = Label(self.parent, text="Errors Over Time", font=("Courier", 18))
        line_label.grid(row=1, column=1)

        self.create_pie_chart(self.data)
        self.create_graph(self.data)

    def create_graph(self, data):
        self.line_frame = Frame(self.parent, height=6)
        self.line_frame.grid(row=2, column=1)
        fig = Figure(figsize=(6, 5), dpi=100)
        ax = fig.add_subplot(111)
        # Create an array of dates to find the oldest and newest dates
        dates = dv.sort_by_date(data)
        labels = dates.keys()
        sizes = []
        for k in labels:
            sizes.append(dates.get(k))
        ax.plot(labels, sizes)
        ax.set_xticklabels(labels=labels, rotation=45)
        fig.subplots_adjust(bottom=0.15)
        self.canvas = FigureCanvas(fig, self.line_frame)
        self.canvas.get_tk_widget().grid(column=0, row=0, sticky=E)

    def create_pie_chart(self, data, review=None):
        print("Creating pie chart...")
        self.pie_frame = Frame(self.parent)
        self.pie_frame.grid(row=2, column=0)
        fig = Figure(figsize=(6, 5), dpi=100)
        ax = fig.add_subplot(111)
        top_five = dv.get_top_five_errors(data, review_level=review)
        print("Top five: {}".format(top_five))
        labels = []
        sizes = []
        for i in range(len(top_five)):
            labels.append(top_five[i][0])
            sizes.append(top_five[i][1])
        ax.pie(sizes, labels=labels, autopct='%1.1f%%',
               shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        canvas = FigureCanvas(fig, self.pie_frame)
        canvas.get_tk_widget().grid(column=0, row=1)
        return canvas


if __name__ == '__main__':
    root = Tk()
    root.title("Employee Lookup")
    root.geometry("400x300")
    root.configure(background='white')
    app = EmployeeLookup(root)
    mainloop()
