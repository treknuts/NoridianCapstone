# Author: Trevor Knutson
# Created on: 04/17/2020
# Description: Detailed view for a given review level. These pages are the same as details general but the review
#              level is already refined.

from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas


class DetailPage(Frame):
    def __init__(self, parent=None, review_level=None):
        super().__init__(parent)
        self.parent = parent
        self.review_level = review_level
        self.background = Frame(self.parent)
        self.background.grid(row=0, column=0, sticky=NSEW)
        self.init_window()


    def init_window(self):
        title = Label(self.background, text=self.review_level, width=35, height=3, font=("Courier", 44), anchor=NW)
        title.grid(column=0, row=0, columnspan=3)
        # List of top 5 reviewers
        reviewer_label = Label(self.background, text="Top 5 Reviewers", font=("Courier", 24))
        reviewer_label.grid(column=0, row=1)
        top_reviewers = Listbox(self.background, font=("Courier", 18))
        top_reviewers.grid(column=0, row=2, rowspan=3)
        reviewers = ["John Doe", "Jane Doe", "Bob Smith", "Mary Anderson", "Bill Williams"]
        for r in reviewers:
            top_reviewers.insert(END, r)

        auditor_label = Label(self.background, text="Top 5 Auditors", font=("Courier", 24))
        auditor_label.grid(column=0, row=5)
        top_auditors = Listbox(self.background, font=("Courier", 18))
        top_auditors.grid(column=0, row=6, rowspan=3)
        auditors = ["John Doe", "Jane Doe", "Bob Smith", "Mary Anderson", "Bill Williams"]
        for a in auditors:
            top_auditors.insert(END, a)

        self.create_graph()

    def create_graph(self):
        fig = Figure(figsize=(10, 8), dpi=100)
        ax = fig.add_subplot(111)
        labels = ['01/01/20', '1/15/20', '1/31/20', '02/01/20']
        sizes = [52, 33, 42, 60]
        # explode = (0.1, 0, 0, 0)
        ax.plot(labels, sizes)

        canvas = FigureCanvas(fig, self.background)
        canvas.get_tk_widget().grid(column=1, row=1, rowspan=8, sticky=NE)
        return canvas


if __name__ == '__main__':
    root = Tk()
    root.title("Noridian Capstone App")
    root.geometry("1900x1000")
    root.configure(background='white')
    app = DetailPage(root, "Supervisory Review")
    mainloop()