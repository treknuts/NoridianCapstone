# Author: Trevor Knutson
# Created on: 04/17/2020
# Description: Detailed view for a given review level. These pages are the same as details general but the review
#              level is already refined.

from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas
from tkcalendar import DateEntry

import dataVisualization as dv


class DetailPage(Frame):
    def __init__(self, parent=None, review_level=None):
        super().__init__(parent)
        self.parent = parent
        self.review_level = review_level
        self.background = Frame(self.parent)
        self.background.grid(row=0, column=0, sticky=NSEW)
        self.init_window()

    def init_window(self):
        title = Label(self.background, text=self.review_level, width=35, height=1, font=("Courier", 32), anchor=NW)
        title.grid(column=0, row=0)

        def set_filter_options(error_name, date1, date2):
            if error_name is not None:
                print(get_error())
            if date1 is not None and date2 is not None:
                print(get_date(date1, date2))

        self.create_top_five(dv.errors, self.review_level)

        # Filter options
        filter_frame = LabelFrame(self.background, height=2, text="Filter Options", font=("Courier", 16))
        filter_frame.grid(row=1, column=1, ipadx=20, ipady=10, sticky=NSEW)

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

        def get_date(date1, date2):
            return "Start date: {}\nEnd date: {}".format(date1.get_date(), date2.get_date())

        # Filter by date
        date_label = LabelFrame(filter_frame, text="Filter by Date")
        date_label.grid(row=0, column=1, padx=5, pady=5)

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
                            command=lambda: set_filter_options(error_entry, start_date,
                                                               end_date)
                            )
        filter_btn.grid(row=1, column=1)

        self.create_top_five(dv.errors, self.review_level)
        self.create_graph()
        self.create_pie_chart(review_level=self.review_level)

    # List of top 5 reviewers
    def create_top_five(self, data, review_level):
        self.reviewer_frame = Frame(self.background)
        self.reviewer_frame.grid(row=1, column=0)
        reviewer_label = LabelFrame(self.reviewer_frame, text="Top 5 Reviewers", font=("Courier", 24))
        reviewer_label.grid(row=0, column=0)
        reviewers = dv.get_top_five_reviewers_by_type(data, review_level)
        top_reviewers = Listbox(reviewer_label, width=50, height=5, font=("Courier", 14))
        top_reviewers.grid(row=0, column=0)
        for r in reviewers:
            top_reviewers.insert(END, "{} -> {} points given".format(r[0], r[1]))


    def create_graph(self):
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
        self.canvas = FigureCanvas(fig, self.background)
        self.canvas.get_tk_widget().grid(column=1, row=2, sticky=E)
        return self.canvas

    def create_pie_chart(self, review_level=None):
        self.pie_frame = Frame(self.background)
        self.pie_frame.grid(row=2, column=0)
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
        canvas.get_tk_widget().grid(column=0, row=2, sticky=SE)


if __name__ == '__main__':
    root = Tk()
    root.title("Noridian Capstone App")
    root.geometry("1900x1000")
    root.configure(background='white')
    app = DetailPage(root, "Supervisory Review")
    mainloop()