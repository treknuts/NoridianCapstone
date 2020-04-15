# Author: Trevor Knutson
# Created on: 03/02/2020
# Description: The application's dashboard with data visualizations and review category statistics

# TODO: Create a navigation bar that allows users to navigate between Dashboard, File-upload, and Detail views (may
#  not be implemented in this file as the navbar should be globally consistent)


from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas


class Dashboard(Frame):
    def __init__(self, master=None):
        # App window definition
        # master will be set to 'root' defined in the main method
        super().__init__(master)
        self.master = master
        self.init_window()

    def init_window(self):
        # Canvas and Frame for the window
        # self.container_canvas = Canvas(self.master)
        # self.window_frame = Frame(self.container_canvas)

        # Category labels followed by their corresponding statistics
        self.create_category_label(0, 0, "60.8C11")
        self.create_category_label(0, 1, "60.8C3")
        self.create_category_label(0, 2, "60.8C9")
        self.create_category_label(0, 3, "60.8C13")
        self.create_category_label(0, 4, "60.8C4")
        self.frame1 = self.create_frame(1, 0)
        self.category_stat(self.frame1, 1, 0, 52)
        self.frame2 = self.create_frame(1, 1)

        self.category_stat(self.frame2, 1, 1, 33)
        self.frame3 = self.create_frame(1, 2)
        self.category_stat(self.frame3, 1, 2, 25)
        self.frame4 = self.create_frame(1, 3)
        self.category_stat(self.frame4, 1, 3, 17)
        self.frame5 = self.create_frame(1, 4)
        self.category_stat(self.frame5, 1, 4, 11)

        # Create scrollable canvas to put review category frames in
        canvas = Canvas(self.master)
        scroll = Scrollbar(self.master)
        self.categories_frame = Frame(canvas, width=600, height=100)
        self.categories_frame.grid(row=0, column=0, columnspan=5, sticky=NW, padx=10, pady=10)

        # Review type definitions
        self.review_type1 = self.create_review_category(0)
        self.review_type_info(self.review_type1, "Supervisor Review")
        self.review_type2 = self.create_review_category(1)
        self.review_type_info(self.review_type2, "Manager Review")
        self.review_type2 = self.create_review_category(2)
        self.review_type_info(self.review_type2, "Director Review")
        self.review_type3 = self.create_review_category(3)
        self.review_type_info(self.review_type3, "Inner Office Review")
        self.review_type4 = self.create_review_category(4)
        self.review_type_info(self.review_type4, "Technical/Quality Assurance Review")

        # Create the canvas window
        canvas.create_window(0, 0, anchor=E, window=self.categories_frame)
        canvas.update_idletasks()
        canvas.configure(yscrollcommand=scroll.set, scrollregion=canvas.bbox(ALL), relief=SUNKEN, height=600, width=1800)
        scroll.config(command=canvas.yview)
        canvas.grid(column=0, row=2, columnspan=6)
        scroll.grid(column=6, row=2, rowspan=5, sticky=N + S + W)

    def create_category_label(self, row, col, text):
        self.label1 = Label(self.master, text=text, anchor=CENTER)
        self.label1.config(width=10, font=("Courier", 20))
        self.label1.grid(sticky=NW, column=col, row=row, padx=5, pady=5)

    def create_frame(self, row, col):
        self.frame = Frame(self.master, bd=2, width=20, relief=SUNKEN)
        self.frame.grid(sticky=NW, column=col, row=row, columnspan=2, padx=10, pady=10)
        return self.frame

    def category_stat(self, frame, row, col, value):
        self.stat1 = Label(frame, text=value)
        self.stat1.config(width=6, height=3, font=("Courier", 44), fg='Red')
        self.stat1.grid(row=row, column=col)

    def create_review_category(self, row):
        self.review_cat = Frame(self.categories_frame, bd=2, relief=SUNKEN)
        self.review_cat.grid(columnspan=6, row=row, padx=10, pady=10)
        return self.review_cat

    def review_type_info(self, frame, value):
        # Review type heading
        self.review = Label(frame, text=value, anchor=NW)
        self.review.config(width=35, height=3, font=("Courier", 44))
        self.review.grid(sticky=NW, column=0, row=0, padx=5, pady=5)
        self.canvas = self.create_pie_chart(frame)
        self.canvas.draw()

    # This currently has data hardcoded in for demonstration purposes
    # The final method will likely pass the labels and sizes as parameters
    # Explode will change too depending on which category has the highest value
    def create_pie_chart(self, frame):
        fig = Figure(figsize=(4, 4), dpi=100)
        ax = fig.add_subplot(111)
        labels = ['60.8C11', '60.8C3', '60.8C9', '60.8C13']
        sizes = [52, 33, 25, 10]
        explode = (0.1, 0, 0, 0)  # only "explode" the slice with largest value
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        canvas = FigureCanvas(fig, frame)
        canvas.get_tk_widget().grid(column=1, row=0)
        return canvas


if __name__ == '__main__':
    root = Tk()
    root.title("Noridian Capstone App")
    root.geometry("1900x1000")
    root.configure(background='white')
    app = Dashboard(root)
    mainloop()
