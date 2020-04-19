import xlrd

# Opens "Desk Review" file in Python then "Sheet1" containing data to be extracted
# Cell A5: "SUPERVISORY REVIEW"
# Cell C10: Supervisor's name
# Cell C11: Auditor's name
desk_r_w = xlrd.open_workbook("Desk Review.xlsx")
supervisory_review = desk_r_w.sheet_by_index(1)

# Opens "Director" file in Python then "Sheet1" containing data to be extracted
# Cell A5: "DIRECTOR REVIEW"
# Cell C10: Director's name
# Cell C11: Supervisor's name
# Cell C12: Auditor's name
director_r_w = xlrd.open_workbook("Director.xlsx")
director_review = director_r_w.sheet_by_index(1)

# Opens "Manager" file in Python then "Sheet1" containing data to be extracted
# Cell A5: "MANAGER REVIEW"
# Cell C10: Manager's name
# Cell C11: Supervisor's name
# Cell C12: Auditor's name
manager_r_w = xlrd.open_workbook("Manager.xlsx")
manager_review = manager_r_w.sheet_by_index(1)

# Opens "Quality Review" file in Python then "Sheet1" containing data to be extracted
# Cell A5: "QUALITY REVIEW"
# Cell C10: Quality Reviewer's Name
# Cell C11: Supervisor's Name
# Cell C12: Auditor's name
quality_r_w = xlrd.open_workbook("Quality Review.xlsx")
quality_review = quality_r_w.sheet_by_index(1)

# Opens "Interoffice Review" file in Python then "Sheet1" containing data to be extracted
# Cell A5: "Inter-office file review"
# Cell C10: Supervisor on opposite contract
# Cell C11: Supervisors's name
# Cell C12: Auditor's name
interoffice_r_w = xlrd.open_workbook("Interoffice File Review.xlsx")
interoffice_review = interoffice_r_w.sheet_by_index(1)

# Supervisor Reviews
s_wb_1 = xlrd.open_workbook("S1.xlsx")
s_ws_1 = s_wb_1.sheet_by_index(1)
s_wb_2 = xlrd.open_workbook("S2.xlsx")
s_ws_2 = s_wb_2.sheet_by_index(1)
s_wb_3 = xlrd.open_workbook("S3.xlsx")
s_ws_3 = s_wb_3.sheet_by_index(1)
s_wb_4 = xlrd.open_workbook("S4.xlsx")
s_ws_4 = s_wb_4.sheet_by_index(1)
s_wb_5 = xlrd.open_workbook("S5.xlsx")
s_ws_5 = s_wb_5.sheet_by_index(1)

# Manager Reviews
m_wb_1 = xlrd.open_workbook("M1.xlsx")
m_ws_1 = m_wb_1.sheet_by_index(1)
m_wb_2 = xlrd.open_workbook("M2.xlsx")
m_ws_2 = m_wb_2.sheet_by_index(1)
m_wb_3 = xlrd.open_workbook("M3.xlsx")
m_ws_3 = m_wb_3.sheet_by_index(1)
m_wb_4 = xlrd.open_workbook("M4.xlsx")
m_ws_4 = m_wb_4.sheet_by_index(1)
m_wb_5 = xlrd.open_workbook("M5.xlsx")
m_ws_5 = m_wb_5.sheet_by_index(1)

# Director Reviews
d_wb_1 = xlrd.open_workbook("D1.xlsx")
d_ws_1 = d_wb_1.sheet_by_index(1)
d_wb_2 = xlrd.open_workbook("D2.xlsx")
d_ws_2 = d_wb_2.sheet_by_index(1)
d_wb_3 = xlrd.open_workbook("D3.xlsx")
d_ws_3 = d_wb_3.sheet_by_index(1)
d_wb_4 = xlrd.open_workbook("D4.xlsx")
d_ws_4 = d_wb_4.sheet_by_index(1)
d_wb_5 = xlrd.open_workbook("D5.xlsx")
d_ws_5 = d_wb_5.sheet_by_index(1)

# Quality Reviews
q_wb_1 = xlrd.open_workbook("Q1.xlsx")
q_ws_1 = q_wb_1.sheet_by_index(1)
q_wb_2 = xlrd.open_workbook("Q2.xlsx")
q_ws_2 = q_wb_2.sheet_by_index(1)
q_wb_3 = xlrd.open_workbook("Q3.xlsx")
q_ws_3 = q_wb_3.sheet_by_index(1)
q_wb_4 = xlrd.open_workbook("Q4.xlsx")
q_ws_4 = q_wb_4.sheet_by_index(1)
q_wb_5 = xlrd.open_workbook("Q5.xlsx")
q_ws_5 = q_wb_5.sheet_by_index(1)

# Interoffice Review
i_wb_1 = xlrd.open_workbook("I1.xlsx")
i_ws_1 = i_wb_1.sheet_by_index(1)
i_wb_2 = xlrd.open_workbook("I2.xlsx")
i_ws_2 = i_wb_2.sheet_by_index(1)
i_wb_3 = xlrd.open_workbook("I3.xlsx")
i_ws_3 = i_wb_3.sheet_by_index(1)
i_wb_4 = xlrd.open_workbook("I4.xlsx")
i_ws_4 = i_wb_4.sheet_by_index(1)
i_wb_5 = xlrd.open_workbook("I5.xlsx")
i_ws_5 = i_wb_5.sheet_by_index(1)


# Method to check if row has values
def row_has_values(ws, row_num):
    # Checks if first five cells are empty. If they are, returns false otherwise returns true
    if ws.cell(row_num, 0).value == xlrd.empty_cell.value and ws.cell(row_num, 1).value == xlrd.empty_cell.value and ws.cell(row_num, 2).value == xlrd.empty_cell.value and ws.cell(row_num, 3).value == xlrd.empty_cell.value and ws.cell(row_num, 4).value == xlrd.empty_cell.value:
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


# The parameters for this method include ws: Excel sheet you want to extract data from, wb: Excel file you're
# extracting data from.
def get_error_arrays(ws, wb):
    # Gets first 6 attributes that are added to each error object
    # Includes provider name, provider #, fiscal year end, reviewer, in-charge, date reviewed
    # .cell(row, column)
    # Value of 1st row and 1st column is (0, 0)
    review_type = ws.cell(4, 0).value
    provider_name = ws.cell(6, 2).value
    provider_number = ws.cell(7, 2).value
    # This code returns the "FISCAL YEAR END" field in the correct format
    fyet = xlrd.xldate_as_tuple(ws.cell(8, 2).value, wb.datemode)
    fiscal_year_end = str(fyet[1]) + "/" + str(fyet[2]) + "/" + str(fyet[0])


    second_level_reviewer = ""
    reviewer = ""
    in_charge = ""
    date_reviewed = ""

    # "SUPERVISORY REVIEW" Extraction
    # Cell A5 (4, 0): "SUPERVISORY REVIEW"
    # Cell C10 (9, 2): Supervisor's name
    # Cell C11: Auditor's name
    if ws.cell(4, 0).value.strip() == "SUPERVISORY REVIEW":
        second_level_reviewer = ""
        reviewer = "Supervisor: " + ws.cell(9, 2).value
        in_charge = "Auditor: " + ws.cell(10, 2).value

        # This code returns the "DATE REVIEWED" field in the correct format in cell (11, 2)
        drt = xlrd.xldate_as_tuple(ws.cell(11, 2).value, wb.datemode)
        date_reviewed = str(drt[1]) + "/" + str(drt[2]) + "/" + str(drt[0])

    # "DIRECTOR REVIEW" Extraction
    # Cell A5: "DIRECTOR REVIEW"
    # Cell C10: Director's name
    # Cell C11: Supervisor's name
    # Cell C12: Auditor's name
    if ws.cell(4, 0).value.strip() == "DIRECTOR REVIEW":
        second_level_reviewer = "Director: " + ws.cell(9, 2).value
        reviewer = "Supervisor: " + ws.cell(10, 2).value
        in_charge = "Auditor: " + ws.cell(11, 2).value

        # This code returns the "DATE REVIEWED" field in the correct format
        drt = xlrd.xldate_as_tuple(ws.cell(12, 2).value, wb.datemode)
        date_reviewed = str(drt[1]) + "/" + str(drt[2]) + "/" + str(drt[0])

    # "MANAGER REVIEW" Extraction
    # Cell A5: "MANAGER REVIEW"
    # Cell C10: Manager's name
    # Cell C11: Supervisor's name
    # Cell C12: Auditor's name
    if ws.cell(4, 0).value.strip() == "MANAGER REVIEW":
        second_level_reviewer = "Manager: " + ws.cell(9, 2).value
        reviewer = "Supervisor: " + ws.cell(10, 2).value
        in_charge = "Auditor: " + ws.cell(11, 2).value

        # This code returns the "DATE REVIEWED" field in the correct format
        drt = xlrd.xldate_as_tuple(ws.cell(12, 2).value, wb.datemode)
        date_reviewed = str(drt[1]) + "/" + str(drt[2]) + "/" + str(drt[0])

    # "QUALITY REVIEW" Extraction
    # Cell A5: "QUALITY REVIEW"
    # Cell C10: Quality Reviewer's Name
    # Cell C11: Supervisor's Name
    # Cell C12: Auditor's name
    if ws.cell(4, 0).value.strip() == "QUALITY REVIEW":
        second_level_reviewer = "Quality Reviewer: " + ws.cell(9, 2).value
        reviewer = "Supervisor: " + ws.cell(10, 2).value
        in_charge = "Auditor: " + ws.cell(11, 2).value

        # This code returns the "DATE REVIEWED" field in the correct format
        drt = xlrd.xldate_as_tuple(ws.cell(12, 2).value, wb.datemode)
        date_reviewed = str(drt[1]) + "/" + str(drt[2]) + "/" + str(drt[0])

    # "Inter-office file review" Extraction
    # Cell A5: "Inter-office file review"
    # Cell C10: Supervisor on opposite contract
    # Cell C11: Supervisors's name
    # Cell C12: Auditor's name
    if ws.cell(4, 0).value.strip() == "Inter-office file review":
        second_level_reviewer = "Supervisor: " + ws.cell(9, 2).value
        reviewer = "Supervisor: " + ws.cell(10, 2).value
        in_charge = "Auditor: " + ws.cell(11, 2).value

        # This code returns the "DATE REVIEWED" field in the correct format
        drt = xlrd.xldate_as_tuple(ws.cell(12, 2).value, wb.datemode)
        date_reviewed = str(drt[1]) + "/" + str(drt[2]) + "/" + str(drt[0])

    # This array will hold all of the errors from the sheet
    # It will be an array of arrays
    all_errors = []

    # Start row for "SUPERVISORY REVIEW".
    start_row = 15

    # Start row for director, manager, quality, and inter-office reviews
    if ws.cell(15, 0).value == "REF":
        start_row = 16

    i = start_row
    if i < ws.nrows:
        while row_has_values(ws, i):
            new_err_obj = return_row_array(ws, i)
            # This while loop extracts data from reviews that have white space in between the rows
            if i < ws.nrows-1:
                while ((ws.cell(i + 1, 1).value == xlrd.empty_cell.value) and (ws.cell(i + 1, 2).value != xlrd.empty_cell.value)) or ((ws.cell(i + 1, 1).value == xlrd.empty_cell.value) and (ws.cell(i + 2, 2).value != xlrd.empty_cell.value)):
                    # If there is other content in the WKPR REF cells below in the same review point, add
                    if ws.cell(i + 1, 0).value != xlrd.empty_cell.value:
                        new_err_obj[0] = new_err_obj[0] + ", " + ws.cell(i + 1, 0).value
                    # If review point is continued directly in the cell below, execute this.
                    if ws.cell(i + 1, 2) != xlrd.empty_cell.value:
                        new_err_obj[2] = new_err_obj[2] + " " + ws.cell(i + 1, 2).value
                        i += 1
                    # If review point is continued one cell below, execute this.
                    # The inner if checks if the value in column 3 is actually part of a new error object. If it it, it doesn't
                    # execute it.
                    else:
                        if ws.cell(i + 2, 2) != xlrd.empty_cell.value and ws.cell(i + 2, 0) == xlrd.empty_cell.value:
                            new_err_obj[2] = new_err_obj[2] + ws.cell(i + 2, 2).value
                            i += 2

            # This will be appended to the start of every error object in a sheet
            error_start = [review_type, provider_name, provider_number, fiscal_year_end, second_level_reviewer,
                       reviewer, in_charge, date_reviewed]

            # This adds the values in the row to the important values from the sheet
            for x in new_err_obj:
                error_start.append(x)

            # This adds new error array to
            all_errors.append(error_start)

            i += 1
            if i == ws.nrows:
                break
    return all_errors

# array to store all errors
all_errors = []

# get_error_arrays supervisor reviews
s1 = get_error_arrays(s_ws_1, s_wb_1)
#for x in s1:
#    print(x)
s2 = get_error_arrays(s_ws_2, s_wb_2)
#for x in s2:
#    print(x)
s3 = get_error_arrays(s_ws_3, s_wb_3)
#for x in s3:
#    print(x)
s4 = get_error_arrays(s_ws_4, s_wb_4)
#for x in s4:
#    print(x)
s5 = get_error_arrays(s_ws_5, s_wb_5)
#for x in s5:
#    print(x)

#print("\n\n")

# get_error_arrays manager reviews
m1 = get_error_arrays(m_ws_1, m_wb_1)
#for x in m1:
#    print(x)
m2 = get_error_arrays(m_ws_2, m_wb_2)
#for x in m2:
#    print(x)
m3 = get_error_arrays(m_ws_3, m_wb_3)
#for x in m3:
#    print(x)
m4 = get_error_arrays(m_ws_4, m_wb_4)
#for x in m4:
#    print(x)
m5 = get_error_arrays(m_ws_5, m_wb_5)
#for x in m5:
#    print(x)

#print("\n\n")

# get_error_arrays director reviews
d1 = get_error_arrays(d_ws_1, d_wb_1)
#for x in d1:
#    print(x)
d2 = get_error_arrays(d_ws_2, d_wb_2)
#for x in d2:
#    print(x)
d3 = get_error_arrays(d_ws_3, d_wb_3)
#for x in d3:
#    print(x)
d4 = get_error_arrays(d_ws_4, d_wb_4)
#for x in d4:
#    print(x)
d5 = get_error_arrays(d_ws_5, d_wb_5)
#for x in d5:
#    print(x)

#print("\n\n")

# Interoffice reviews
i1 = get_error_arrays(i_ws_1, i_wb_1)
#for x in i1:
#    print(x)
i2 = get_error_arrays(i_ws_2, i_wb_2)
#for x in i2:
#    print(x)
i3 = get_error_arrays(i_ws_3, i_wb_3)
#for x in i3:
#    print(x)
i4 = get_error_arrays(i_ws_4, i_wb_4)
#for x in i4:
#    print(x)
i5 = get_error_arrays(i_ws_5, i_wb_5)
#for x in i5:
#    print(x)

#print("\n\n")

# Quality get_error_arrays
q1 = get_error_arrays(q_ws_1, q_wb_1)
#for x in q1:
#    print(x)
q2 = get_error_arrays(q_ws_2, q_wb_2)
#for x in q2:
#    print(x)
q3 = get_error_arrays(q_ws_3, q_wb_3)
#for x in q3:
#    print(x)
q4 = get_error_arrays(q_ws_4, q_wb_4)
#for x in q4:
#   print(x)
q5 = get_error_arrays(q_ws_5, q_wb_5)
# for x in q5:
#    print(x)

#print("\n\n")

all_errors = s1 + s2 + s3 + s4 + s5 + m1 + m2 + m3 + m4 + m5 + d1 + d2 + d3 + d4 + d5 + i1 + i2 + i3 + i4 + i5 + q1 + q2 + q3 + q4 + q5
for x in all_errors:
    print(str(x) + ",")
