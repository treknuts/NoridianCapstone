# Author: Trevor Knutson
# Created on: 03/02/2020
# Description: The application's dashboard with data visualizations and review category statistics


from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas
from detailview import DetailPage
import dataVisualization as dv


class Dashboard(Frame):
    def __init__(self, parent):
        # App window definition
        # The idea behind the container and background is to be able to switch between pages.
        # The container allows for navigation to the review level details pages.
        # The background allows for navigation between pages using the navigation menu. If the background is not there
        # it grids the page you navigated to into the page you were navigating from. Kind of strange but this works.
        # Whatever is assigned to self.frame will be the frame displayed on the page.
        super().__init__(parent)
        self.parent = parent
        self.frame = None
        self.container = Frame(self.parent, width=self.winfo_x(), height=self.winfo_y())
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid(row=0, column=0, sticky=NSEW)
        self.background = Frame(self.container)
        self.background.grid(row=0, column=0, sticky=NSEW)

        # Retrieves the error objects from the
        self.data = dv.errors

        self.init_window()

    def init_window(self):
        # Top 5 overall errors
        top_five = dv.get_top_five_errors(self.data)

        # Category labels followed by their corresponding statistics
        self.create_category_label(0, 0, top_five[0][0])
        self.create_category_label(0, 1, top_five[1][0])
        self.create_category_label(0, 2, top_five[2][0])
        self.create_category_label(0, 3, top_five[3][0])
        self.create_category_label(0, 4, top_five[4][0])

        self.frame1 = self.create_frame(1, 0)
        self.category_stat(self.frame1, 1, 0, top_five[0][1])
        self.frame2 = self.create_frame(1, 1)
        self.category_stat(self.frame2, 1, 1, top_five[1][1])
        self.frame3 = self.create_frame(1, 2)
        self.category_stat(self.frame3, 1, 2, top_five[2][1])
        self.frame4 = self.create_frame(1, 3)
        self.category_stat(self.frame4, 1, 3, top_five[3][1])
        self.frame5 = self.create_frame(1, 4)
        self.category_stat(self.frame5, 1, 4, top_five[4][1])

        # Create scrollable canvas to put review category frames in
        canvas = Canvas(self.background)
        scroll = Scrollbar(self.background)
        self.categories_frame = Frame(canvas, width=600, height=100)
        self.categories_frame.grid(row=0, column=0, columnspan=5, sticky=NW, padx=10, pady=10)

        # Review type definitions
        self.create_review_category(0, "SUPERVISORY REVIEW")
        self.create_review_category(1, "MANAGER REVIEW")
        self.create_review_category(2, "DIRECTOR REVIEW")
        self.create_review_category(3, "Inter-office file review")
        self.create_review_category(4, "QUALITY REVIEW")

        # Create the canvas window
        canvas.create_window(0, 0, anchor=E, window=self.categories_frame)
        canvas.update_idletasks()
        canvas.configure(yscrollcommand=scroll.set, scrollregion=canvas.bbox(ALL), relief=SUNKEN, height=600, width=1800)
        scroll.config(command=canvas.yview)
        canvas.grid(column=0, row=2, columnspan=6)
        scroll.grid(column=6, row=2, rowspan=5, sticky=N + S + W)
        canvas.yview_moveto(0)

    def create_category_label(self, row, col, text):
        self.label1 = Label(self.background, text=text, anchor=CENTER)
        self.label1.config(width=10, font=("Courier", 20))
        self.label1.grid(sticky=NW, column=col, row=row, padx=5, pady=5)

    def create_frame(self, row, col):
        self.frame = Frame(self.background, bd=2, width=20, relief=SUNKEN)
        self.frame.grid(sticky=NW, column=col, row=row, columnspan=2, padx=10, pady=10)
        return self.frame

    def category_stat(self, frame, row, col, value):
        self.stat1 = Label(frame, text=value)
        self.stat1.config(width=6, height=3, font=("Courier", 44), fg='Red')
        self.stat1.grid(row=row, column=col)

    def create_review_category(self, row, value):
        self.review_cat = Frame(self.categories_frame, bd=2, relief=SUNKEN)
        self.review_cat.grid(columnspan=6, row=row, padx=10, pady=10)
        self.review = Label(self.review_cat, text=value, anchor=NW)
        title = self.review.cget("text")
        details_btn = Button(self.review_cat, fg="blue", text="View Details", command=lambda: self.show_frame(DetailPage,
                                                                                                   self.container,
                                                                                                   title))
        details_btn.grid(row=1, column=0, sticky=W)
        self.review.config(width=30, height=2, font=("Courier", 44))
        self.review.grid(sticky=NW, column=0, row=0, padx=5, pady=5)
        self.canvas = self.create_pie_chart(self.review_cat, title)
        self.canvas.draw()

    # Data returned from get_top_five_errors in the format [(name1, num1),...,(name5, num5)]
    # Chart labels are category names and sizes are the magnitude of the category
    # Get values via their respective indices
    def create_pie_chart(self, frame, review_level):
        fig = Figure(figsize=(3, 2), dpi=100)
        ax = fig.add_subplot(111)
        top_five = dv.get_top_five_errors(a=self.data, review_level=review_level)
        labels = []
        sizes = []
        for i in range(len(top_five)):
            labels.append(top_five[i][0])
            sizes.append(top_five[i][1])
        ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        canvas = FigureCanvas(fig, frame)
        canvas.get_tk_widget().grid(column=1, row=0)
        return canvas

    # Enables users' to switch the frame displayed within the container.
    def show_frame(self, class_name, cont, review_type):
        new_frame = class_name(cont, review_type)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.grid(row=0, column=0, sticky=NSEW)



if __name__ == '__main__':
    root = Tk()
    root.title("Noridian Capstone App")
    root.geometry("1825x875")
    root.configure(background='white')
    app = Dashboard(root)
    mainloop()
