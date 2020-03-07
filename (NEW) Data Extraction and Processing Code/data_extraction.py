import xlrd

# Opens "Desk Review" file in Python then "Sheet1" containing data to be extracted
desk_r_w = xlrd.open_workbook("Desk Review.xlsx")
desk_review = desk_r_w.sheet_by_index(1)

# Opens "Director Review" file in Python then "Sheet1" containing data to be extracted
director_r_w = xlrd.open_workbook("Director Review.xlsx")
director_review = director_r_w.sheet_by_index(1)

# Opens "Manager Review" file in Python then "Sheet1" containing data to be extracted
manager_r_w = xlrd.open_workbook("Manager Review.xlsx")
manager_review = manager_r_w.sheet_by_index(1)

# Opens "Supervisor Review" file in Python then "Sheet1" containing data to be extracted
supervisor_r_w = xlrd.open_workbook("Supervisor Review.xlsx")
supervisor_review = supervisor_r_w.sheet_by_index(1)


# Method to check if row has values
def row_has_values(ws, row_num):
    # Checks if first five cells are empty. If they are, returns false otherwise returns true
    if ws.cell(row_num, 0).value == xlrd.empty_cell.value and ws.cell(row_num,
                                                                      1).value == xlrd.empty_cell.value and ws.cell(
            row_num, 2).value == xlrd.empty_cell.value and ws.cell(row_num,
                                                                   3).value == xlrd.empty_cell.value and ws.cell(
            row_num, 4).value == xlrd.empty_cell.value:
        return False
    else:
        return True


# Method to return array of values in each row
def return_row_array(ws, row_num):
    row_array = []
    # Loops through first five cells of each row and creates an array
    for x in range(4):
        row_array.append(ws.cell(row_num, x).value)
    row_array.append(ws.cell(row_num, 5).value)

    return row_array


def get_error_arrays(ws, wb):
    # Gets first 6 attributes that are added to each error object
    # Includes provider name, provider #, fiscal year end, reviewer, in-charge, date reviewed
    # .cell(row, column)
    # Value of 1st row and 1st column is (0, 0)
    provider_name = ws.cell(6, 2).value
    provider_number = ws.cell(7, 2).value
    # This code returns the "FISCAL YEAR END" field in the correct format
    fyet = xlrd.xldate_as_tuple(ws.cell(8, 2).value, wb.datemode)
    fiscal_year_end = str(fyet[1]) + "/" + str(fyet[2]) + "/" + str(fyet[0])

    reviewer = ""
    second_level_reviewer = ""
    third_level_reviewer = ""
    in_charge = ""
    date_reviewed = ""

    if ws.cell(9, 0).value.strip() == "REVIEWER:":
        reviewer = ws.cell(9, 2).value
        in_charge = ws.cell(10, 2).value

        # This code returns the "DATE REVIEWED" field in the correct format
        drt = xlrd.xldate_as_tuple(ws.cell(11, 2).value, wb.datemode)
        date_reviewed = str(drt[1]) + "/" + str(drt[2]) + "/" + str(drt[0])

        second_level_reviewer = "No 2nd level review."
        third_level_reviewer = "No 3rd level review."

    if ws.cell(9, 0).value.strip() == "2ND LEVEL RVWR:":
        second_level_reviewer = ws.cell(9, 2).value
        reviewer = ws.cell(10, 2).value
        in_charge = ws.cell(11, 2).value

        # This code returns the "DATE REVIEWED" field in the correct format
        drt = xlrd.xldate_as_tuple(ws.cell(12, 2).value, wb.datemode)
        date_reviewed = str(drt[1]) + "/" + str(drt[2]) + "/" + str(drt[0])

        third_level_reviewer = "No 3rd level review."

    if ws.cell(9, 0).value.strip() == "3RD LEVEL RVWR:":
        third_level_reviewer = ws.cell(9, 2).value
        second_level_reviewer = ws.cell(10, 2).value
        reviewer = ws.cell(11, 2).value
        in_charge = ws.cell(12, 2).value

        # This code returns the "DATE REVIEWED" field in the correct format
        drt = xlrd.xldate_as_tuple(ws.cell(13, 2).value, wb.datemode)
        date_reviewed = str(drt[1]) + "/" + str(drt[2]) + "/" + str(drt[0])

    # This array will hold all of the errors from the sheet
    # It will be an array of arrays
    all_errors = []

    start_row = 15

    if ws.cell(15, 0).value == "REF":
        start_row = 16

    if ws.cell(16, 0).value == "REF":
        start_row = 17

    i = start_row
    while row_has_values(ws, i):
        new_err_obj = return_row_array(ws, i)

        # This will be appended to the start of every error object in a sheet
        error_start = [provider_name, provider_number, fiscal_year_end, third_level_reviewer, second_level_reviewer,
                       reviewer, in_charge, date_reviewed]

        # This adds the values in the row to the important values from the sheet
        for x in new_err_obj:
            error_start.append(x)

        # This adds new error array to
        all_errors.append(error_start)

        i += 1

    return all_errors


# UNIT TEST for get_error_arrays
t1 = get_error_arrays(desk_review, desk_r_w)
for x in t1:
    print(x)

print("\n\n")

t2 = get_error_arrays(director_review, director_r_w)
for x in t2:
    print(x)

print("\n\n")

t3 = get_error_arrays(manager_review, manager_r_w)
for x in t3:
    print(x)

print("\n\n")

t4 = get_error_arrays(supervisor_review, supervisor_r_w)
for x in t4:
    print(x)

print("\n\n")
