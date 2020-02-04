# Author: Tanner Nystrom
import xlrd
# the "r" is needed at the beginning of the path so python reads it correct (not as a string)
# stores file location in loc
loc = r"D:\Projects\Python\Test.xlsx"

# opens the workbook
wb = xlrd.open_workbook(loc)

# saves the first sheet of the spreadsheet as sheet"
sheet = wb.sheet_by_index(0)

# creates an array to store all values
cells = []
# loop through every cell, add it to the array
for i in range(0, sheet.nrows):
    for j in range(0, sheet.ncols):
        # sheet.cell_value calls the exact value (EX: 2.0) but sheet.cell calls value and type (EX: number: 2.0)
        cells.append(int(sheet.cell_value(i, j)))

# print every value in the array cells
print(cells)
