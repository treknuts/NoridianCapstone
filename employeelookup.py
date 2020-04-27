from tkinter import *
import dataVisualization as dv


class EmployeeLookup(Frame):
    def __init__(self):
        self.parent = Tk()
        self.data = dv.errors
        employee = "Sarah Woe"
        self.employee_errors = dv.get_errors_by_name(self.data, employee)

        listbox = Listbox(self.parent, width=50, height=5, font=("Courier", 14))
        listbox.grid(row=0, column=0)

        for x in dv.get_errors_by_name(dv.errors, employee):
            listbox.insert(END, "{}, {}, {}".format(x[6], x[7], x[12]))

        mainloop()


if __name__ == '__main__':
    root = Tk()
    root.title("Employee Lookup")
    root.geometry("500x400")
    root.configure(background='white')
    app = EmployeeLookup(root)
    mainloop()
