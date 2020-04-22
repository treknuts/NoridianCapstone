# Author: Trevor Knutson
# Created on: 03/19/2020
# Description: A more detailed view than the dashboard. Filter options to refine search.

from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas


class DataVisualization(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.background = Frame(self.parent)
        self.background.grid(row=0, column=0, sticky=NSEW)
        self.init_window()

    def init_window(self):
        # List of top 5 reviewers giving out review points
        reviewer_frame = LabelFrame(self.background, text="Top 5 Reviewers", font=("Courier", 24))
        reviewer_frame.grid(row=0, column=0)
        top_reviewers = Listbox(reviewer_frame, font=("Courier", 18))
        top_reviewers.grid(row=0, column=0)
        reviewers = [["name1", 8], ["name2", 7], ["name3", 6], ["name4", 4], ["name5", 3]]
        for r in reviewers:
            top_reviewers.insert(END, "{}             {}".format(r[0], r[1]))

        # List of top 5 reviewers receiving review points
        auditor_frame = LabelFrame(self.background, text="Top 5 Auditors", font=("Courier", 24))
        auditor_frame.grid(row=1, column=0)
        top_auditors = Listbox(auditor_frame, font=("Courier", 18))
        top_auditors.grid(row=0, column=0)
        auditors = [["name1", 8], ["name2", 7], ["name3", 6], ["name4", 4], ["name5", 3]]
        for a in auditors:
            top_auditors.insert(END, "{}             {}".format(a[0], a[1]))

        # Filter options

        # Filter by error type
        def get_error(entry):
            print(error_entry.get())

        error_label = LabelFrame(self.background, text="Filter by a specific error")
        error_label.grid(row=0, column=1)

        error = StringVar()
        entry_label = Label(error_label, text="Error code: ")
        entry_label.grid(row=0, column=0)
        error_entry = Entry(error_label, textvariable=error)
        error_entry.grid(row=0, column=1)

        error_btn = Button(entry_label, text="Set Error", command=lambda: get_error(error_entry))
        error_btn.grid(row=1, column=0)

        # Filter by review level
        def get_review_level(combo):
            print(combo.get())

        review_label = LabelFrame(self.background, text="Filter by Review level")
        review_label.grid(row=1, column=1)

        review_levels = ["Supervisor Review", "Manager Review", "Director Review", "Inter-office Review", "Technical/Quality Assurance Review"]

        review_level_combo = Combobox(review_label)
        review_level_combo['values'] = review_levels
        review_level_combo.grid(row=0, column=1)

        review_btn = Button(review_label, text="Set Review Level", command=lambda: get_review_level(review_level_combo))
        review_btn.grid(row=1, column=1)

        # TODO: Get the data from the input options to filter the data and display it accordingly.

        def get_date(date1, date2):
            print("Start date {}".format(date1.get_date()))
            print("Start date {}".format(date2.get_date()))

        # Filter by date
        date_label = LabelFrame(self.background, text="Filter by Date")
        date_label.grid(row=2, column=1)

        start_label = Label(date_label, text="Start Date")
        start_label.grid(row=0, column=0)

        start_date = DateEntry(date_label, locale='en_US', date_pattern='MM/dd/yyyy')
        start_date.grid(row=0, column=1)

        end_label = Label(date_label, text="End Date")
        end_label.grid(row=1, column=0)

        end_date = DateEntry(date_label, locale='en_US', date_pattern='MM/dd/yyyy')
        end_date.grid(row=1, column=1)

        date_btn = Button(date_label, text="Set Dates", command=lambda: get_date(start_date, end_date))
        date_btn.grid(row=2, column=1)

        self.create_graph()

    def create_graph(self):
        fig = Figure(figsize=(10, 7), dpi=100)
        ax = fig.add_subplot(111)
        labels = ['01/01/20', '1/15/20', '1/31/20', '02/01/20']
        sizes = [52, 33, 42, 60]
        # explode = (0.1, 0, 0, 0)
        ax.plot(labels, sizes)

        canvas = FigureCanvas(fig, self.background)
        canvas.get_tk_widget().grid(column=2, row=0, rowspan=8, sticky=NE)
        return canvas


if __name__ == '__main__':
    root = Tk()
    root.title("Noridian Capstone App")
    root.geometry("1900x1000")
    root.configure(background='white')
    app = DataVisualization(root)
    mainloop()
