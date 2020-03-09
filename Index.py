# Author: Tanner Nystrom
from tkinter import filedialog
from tkinter import *
import xlrd
import datetime

root = Tk()



def __init__():
    setupWindow()


def setupWindow():
    #Set the window size to 1000 by 700
    root.geometry('1000x700')
    root.configure(background='turquoise')
    width = 1000
    height = 700
    root.title("Noridian Audit Application")

    browseButton = Button(root, text="Import Files", width=15, height=2, command=openFile).place(x=850, y=350)


    mainloop()


def openFile():
    root.fileName = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))

    loc = root.fileName

    # opens the workbook
    wb = xlrd.open_workbook(loc)

    # saves the first sheet of the spreadsheet as sheet"
    sheet = wb.sheet_by_index(0)

    getMainData(sheet)

    initialValues(sheet)

def initialValues(sheet):
    providedName = sheet.cell_value(6,2)
    providedNumber = sheet.cell_value(7, 2)
    yearEnd = (sheet.cell_value(8, 2))
    reviewer = sheet.cell_value(9, 2)
    inCharge = sheet.cell_value(10, 2)
    dateReviewed = sheet.cell_value(11,2)



    print(providedName)
    print(providedNumber)
    print(yearEnd)
    print(reviewer)
    print(inCharge)
    print(dateReviewed)



def getMainData(sheet):
    totalArray = []

    for j in range(15, sheet.nrows):
        row = []
        for i in range(0, 5):
            if not (sheet.cell_value(j,i) == ""):
                value = sheet.cell_value(j, i)
                row.append(value)
        if not len(row) == 0:
            totalArray.append(row)


    print(totalArray)

    return totalArray





__init__()
