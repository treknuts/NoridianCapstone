# Author: Trevor Knutson
# Created on: 04/19/2020
# Description: A more detailed view than the dashboard. Filter options to refine search.

from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas
import dataVisualization as dv


# TODO: Line graph y-axis is plotting the wrong data. It needs to plot the amount of errors at the time on the x-axis

class DataVisualization(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background = Frame(self.parent)
        self.background.grid(row=0, column=0, sticky=NSEW)
        self.init_window()

    def init_window(self):

        # TODO: redraw the page once filter options are set
        def set_filter_options(error_name, review, date1, date2):
            if error_name is not None:
                print(get_error())
            if review is not None:
                print(get_review_level(review))
                self.reviewer_frame.after(100, self.reviewer_frame.destroy())
                create_top_five(dv.errors, get_review_level(review))
                self.pie_frame.after(100, self.pie_frame.destroy())
                self.create_pie_chart(get_review_level(review))
            elif review is None:
                # TODO: This is bugged. Doesn't redraw frames right
                self.reviewer_frame.after(100, self.reviewer_frame.destroy())
                create_top_five(dv.errors, None)
                self.pie_frame.after(100, self.pie_frame.destroy())
                self.create_pie_chart(None)
            if date1 is not None and date2 is not None:
                print(get_date(date1, date2))

        def create_top_five(data, review_level=None):
            self.reviewer_frame = Frame(self.background)
            self.reviewer_frame.grid(row=0, column=0)
            reviewer_label = LabelFrame(self.reviewer_frame, text="Top 5 Reviewers", font=("Courier", 24))
            reviewer_label.grid(row=0, column=0)
            if review_level is not None:
                reviewers = dv.get_top_five_reviewers_by_type(data, review_level)
            else:
                reviewers = dv.get_top_five_reviewers(data)
            top_reviewers = Listbox(reviewer_label, width=50, height=5, font=("Courier", 14))
            top_reviewers.grid(row=0, column=0)
            for r in reviewers:
                top_reviewers.insert(END, "{} -> {} points given".format(r[0], r[1]))

        create_top_five(dv.errors)

        # Filter options
        filter_frame = LabelFrame(self.background, height=2, text="Filter Options", font=("Courier", 16))
        filter_frame.grid(row=0, column=1, ipadx=20, ipady=10, sticky=NSEW)

        # Filter by error type
        def get_error():
            return error_entry.get()

        error_label = LabelFrame(filter_frame, text="Filter by a specific error")
        error_label.grid(row=0, column=0, padx=5, pady=5)

        error = StringVar()
        entry_label = Label(error_label, text="Error code: ")
        entry_label.grid(row=0, column=0)
        error_entry = Entry(error_label, textvariable=error)
        error_entry.grid(row=1, column=1)

        # Filter by review level
        def get_review_level(combo):
            return combo.get()

        review_label = LabelFrame(filter_frame, text="Filter by Review level")
        review_label.grid(row=0, column=1, padx=5, pady=5)

        review_levels = [None,
                         "SUPERVISORY REVIEW",
                         "MANAGER REVIEW",
                         "DIRECTOR REVIEW",
                         "Inter-office file review",
                         "QUALITY REVIEW"]

        review_level_combo = Combobox(review_label)
        review_level_combo['values'] = review_levels
        review_level_combo.grid(row=0, column=1)

        def get_date(date1, date2):
            return "Start date: {}\nEnd date: {}".format(date1.get_date(), date2.get_date())

        # Filter by date
        date_label = LabelFrame(filter_frame, text="Filter by Date")
        date_label.grid(row=0, column=2, padx=5, pady=5)

        start_label = Label(date_label, text="Start Date")
        start_label.grid(row=0, column=0)

        start_date = DateEntry(date_label, locale='en_US', date_pattern='MM/dd/yyyy')
        start_date.grid(row=0, column=1)
        # Initialize the date entry to be empty
        start_date.delete(0, END)

        end_label = Label(date_label, text="End Date")
        end_label.grid(row=1, column=0)

        end_date = DateEntry(date_label, locale='en_US', date_pattern='MM/dd/yyyy')
        end_date.grid(row=1, column=1)
        # Initialize the date entry to be empty
        end_date.delete(0, END)

        filter_btn = Button(filter_frame,
                            text="Set filter options",
                            command=lambda: set_filter_options(error_entry, review_level_combo, start_date, end_date)
                            )
        filter_btn.grid(row=1, column=1)

        self.create_graph()
        self.create_pie_chart()

    def create_graph(self):
        self.line_frame = Frame(self.background)
        self.line_frame.grid(row=1, column=1)
        fig = Figure(figsize=(9, 6), dpi=100)
        ax = fig.add_subplot(111)
        # Create an array of dates to find the oldest and newest dates

        data = dv.sort_by_date(dv.errors)
        labels = []
        sizes = []
        for k in data:
            labels.append(k[7])
            sizes.append(k[9])
        ax.plot(labels, sizes)
        ax.set_xticklabels(labels=labels, rotation=45)
        self.canvas = FigureCanvas(fig, self.line_frame)
        self.canvas.get_tk_widget().grid(column=0, row=0, rowspan=2, sticky=E)

    def create_pie_chart(self, review_level=None):
        self.pie_frame = Frame(self.background)
        self.pie_frame.grid(row=1, column=0)
        fig = Figure(figsize=(9, 6), dpi=100)
        ax = fig.add_subplot(111)
        if review_level is not None:
            top_five = dv.get_top_five_errors(a=dv.errors, review_level=review_level)
        else:
            top_five = dv.get_top_five_errors(a=dv.errors)
        labels = []
        sizes = []
        for i in range(len(top_five)):
            labels.append(top_five[i][0])
            sizes.append(top_five[i][1])
        ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        canvas = FigureCanvas(fig, self.pie_frame)
        canvas.get_tk_widget().grid(column=0, row=0, rowspan=2, sticky=SE)


if __name__ == '__main__':
    root = Tk()
    root.title("Noridian Capstone App")
    root.geometry("1900x1000")
    root.configure(background='white')
    app = DataVisualization(root)
    mainloop()
