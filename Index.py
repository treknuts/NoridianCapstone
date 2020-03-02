# Author: Tanner Nystrom
from tkinter import filedialog
from tkinter import *
import xlrd

root = Tk()

def __init__():
    #Set the window size to 1000 by 700
    root.geometry('1000x700')
    width = 1000
    height = 700
    root.title("Noridian Audit Application")
    #Sets the size of the button frame to 80 by 200
    f = Frame(root, height=80, width=200)
    f.pack_propagate(0)
    f.pack()


    #Create button with text "Browse" and action to method openFile
    b = Button(f, text="Browse", compound=CENTER, command=openFile)
    b.pack()

    mainloop()


def openFile():
    root.fileName = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))

    loc = root.fileName

    # opens the workbook
    wb = xlrd.open_workbook(loc)

    # saves the first sheet of the spreadsheet as sheet"
    sheet = wb.sheet_by_index(0)

    # creates an array to store all values
    cellsNumber = []
    cellsString = []
    # loop through every cell, add it to the array
    for i in range(0, sheet.nrows):
        for j in range(0, sheet.ncols):
            # sheet.cell_value calls the exact value (EX: 2.0) but sheet.cell calls value and type (EX: number: 2.0)
            if isinstance(sheet.cell_value(i, j), str):
                cellsString.append(sheet.cell_value(i, j))
            else:
                cellsNumber.append(int(sheet.cell_value(i, j)))

    # print every value in the array cells

    print("Numbers found in file " + str(cellsNumber))
    print("Strings found in file " + str(cellsString))

    cellsNumber.sort()
    cellsString.sort()
    print("================================================")
    print("Sorted Numbers found in file " + str(cellsNumber))
    print("Alphabetical Strings found in file " + str(cellsString))






__init__()
