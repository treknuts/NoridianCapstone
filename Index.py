# Author: Tanner Nystrom
from tkinter import filedialog
from tkinter import *
# import xlrd

root = Tk()


def __init__():
    # Set the window size to 1000 by 700
    root.geometry('1000x700')
    width = 1000
    height = 700
    root.title("Noridian Audit Application")
    # Sets the size of the button frame to 80 by 200
    f = Frame(root, height=80, width=200)
    f.pack_propagate(0)
    f.pack()

    # Create button with text "Browse" and action to method openFile
    b = Button(f, text="Browse", compound=CENTER, command=open_file)
    b.pack()

    mainloop()


def open_file():
    root.fileName = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))

    loc = root.fileName

    # opens the workbook
    wb = xlrd.open_workbook(loc)

    # saves the first sheet of the spreadsheet as sheet"
    sheet = wb.sheet_by_index(0)

    # creates an array to store all values
    cells_number = []
    cells_string = []
    # loop through every cell, add it to the array
    for i in range(0, sheet.nrows):
        for j in range(0, sheet.ncols):
            # sheet.cell_value calls the exact value (EX: 2.0) but sheet.cell calls value and type (EX: number: 2.0)
            if isinstance(sheet.cell_value(i, j), str):
                cells_string.append(sheet.cell_value(i, j))
            else:
                cells_number.append(int(sheet.cell_value(i, j)))

    # print every value in the array cells

    print("Numbers found in file " + str(cells_number))
    print("Strings found in file " + str(cells_string))

    cells_number.sort()
    cells_string.sort()
    print("================================================")
    print("Sorted Numbers found in file " + str(cells_number))
    print("Alphabetical Strings found in file " + str(cells_string))


__init__()
