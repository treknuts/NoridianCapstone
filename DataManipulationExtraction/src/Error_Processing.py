# Ignore red underline it works
import data_extraction
import datetime
from collections import Counter


# This method is used to parse dates to create correct date/time object
# This is format getting spliced "12/31/33"
def format_date(s):
    # This creates an array of the number is the date split by "/"
    n = s.split("/")
    month = int(n[0])
    day = int(n[1])
    year = int(n[2])

    return datetime.datetime(year, month, day)


# data_extraction.all_errors references the array of all the errors extracted in data_extraction.py class
# USE data_extraction.all_errors if you want an array of all the errors
errors = data_extraction.all_errors


# ERROR FORMAT
# [0] REVIEW TYPE, [1] PROVIDER NAME, [2] PROVIDER #, [3] FISCAL YEAR END, [4] 2ND LEVEL REVIEWER, [5] SUPERVISOR, [6] AUDITOR, [7] DATE REVIEWED, [8] WKPR REF, [9] POINT #, [10] REVIEW POINT, [11] DISPOSITION, INITIALS, DATE, [12] UDR/EXHIBIT STEP/IOM CHAP 8 REF
# ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann', 'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 12.0, 'Sample', '', '60.8C1']

# Method to return top 5 errors in database
def get_top_five_errors(a):
    error_types = []
    for x in a:
        if x[12] != "NA" and x[12] != "n/a" and x[12] != "":
            error_types.append(x[12])

    # Gets an array of top 5 errors with error type and frequency
    # It's an array of arrays
    # [("string", int), ("string", int), ("string", int), ("string", int), ("string", int)]
    # You need to import Counter class
    net = Counter(error_types).most_common(5)

    # Creates string that can display top five errors
    top_five = net[0][0] + ": " + str(net[0][1]) + "\n" + net[1][0] + ": " + str(net[1][1]) + "\n" + net[2][0] + ": " + str(net[2][1]) + "\n" + net[3][0] + ": " + str(net[3][1]) + "\n" + net[4][0] + ": " + str(net[4][1]) + "\n"

    # To return the top five errors in their array form, return net
    return top_five


# TEST AND OUTPUT FOR get_top_five_errors
test = get_top_five_errors(errors)
print("Top five errors UDR/Exhibit Step/IOM Chap 8 Ref overall:")
print(test)


# Returns top 5 errors from desk reviews (supervisor reviewing auditor)
def get_top_five_supervisor_errors(a):
    supervisor_errors = []
    for x in a:
        if x[0] == 'SUPERVISORY REVIEW':
            supervisor_errors.append(x)

    return get_top_five_errors(supervisor_errors)


# OUTPUT for get_top_five_supervisor_errors
test2 = get_top_five_supervisor_errors(errors)
print("Top five desk review UDR/Exhibit Step/IOM Chap 8 Ref errors:")
print(test2)


# Returns top 5 errors from manager (manager reviewing supervisor who reviewed auditor)
def get_top_five_manager_errors(a):
    manager_errors = []
    for x in a:
        if x[0] == 'MANAGER REVIEW':
            manager_errors.append(x)

    return get_top_five_errors(manager_errors)


# OUTPUT for get_top_five_supervisor_errors
test3 = get_top_five_manager_errors(errors)
print("Top five manager review UDR/Exhibit Step/IOM Chap 8 Ref errors:")
print(test3)


# Returns top 5 errors from director (director reviewing supervisor who reviewed auditor)
def get_top_five_manager_errors(a):
    director_errors = []
    for x in a:
        if x[0] == 'DIRECTOR REVIEW':
            director_errors.append(x[8])

    net = Counter(director_errors).most_common(5)
    top_five = net[0][0].strip() + ": " + str(net[0][1]) + "\n" + net[1][0].strip() + ": " + str(net[1][1]) + "\n" + net[2][0].strip() + ": " + str(net[2][1]) + "\n" + net[3][0].strip() + ": " + str(net[3][1]) + "\n" + net[4][0].strip() + ": " + str(net[4][1]) + "\n"

    return top_five


# OUTPUT for get_top_five_supervisor_errors
test4 = get_top_five_manager_errors(errors)
print("Top five director WKPR REF errors:")
print(test4)

# This returns the top 5 reviewers based on review points given
def get_top_five_reviewers(a):
    reviewers = []
    for x in a:
        if x[0] == "SUPERVISORY REVIEW":
            reviewers.append(x[5])
        if x[0] == "DIRECTOR REVIEW":
            reviewers.append(x[4])
        if x[0] == "MANAGER REVIEW":
            reviewers.append(x[4])
        if x[0] == "QUALITY REVIEW":
            reviewers.append(x[4])
        if x[0] == "Inter-office file review":
            reviewers.append(x[4])
    net = Counter(reviewers).most_common(5)
    top_five = net[0][0] + ": " + str(net[0][1]) + "\n" + net[1][0] + ": " + str(net[1][1]) + "\n" + net[2][0] + ": " + str(net[2][1]) + "\n" + net[3][0] + ": " + str(net[3][1]) + "\n" + net[4][0] + ": " + str(net[4][1]) + "\n"
    return top_five

# OUTPUT for get_top_5_reviewers
test5 = get_top_five_reviewers(errors)
print(test5)

# This method returns all of the error with a certain “UDR/Exhibit Step/IOM Chap 8 Ref” code
# Parameter "a" represents array of all errors (which are also arrays)
# Parameter e_type is the errors type (for example "60.8C2")
def get_errors_by_error_type(a, e_type):
    errors_by_e_type = []
    for x in a:
        # Checks if “UDR/Exhibit Step/IOM Chap 8 Ref” equals e_type
        if x[12] == e_type:
            errors_by_e_type.append(x)

    return errors_by_e_type


# UNIT TEST get_errors_by_error_type
t1 = get_errors_by_error_type(errors, "60.8C2")
for i in t1:
    print(i)

print("\n\n")


# This method returns all of the errors within a certain date range based on “DATE REVIEWED:”
# Parameter "a" represents array of all errors (which are also arrays)
# Parameter d1 and d2 are the dates you want to set as your bounds
def get_errors_by_review_date(a, d1, d2):
    errors_by_r_date = []
    for x in a:
        d = format_date(x[7])
        if d1 <= d <= d2:
            errors_by_r_date.append(x)

    return errors_by_r_date


# TEST get_errors_by_review_date
# datetime.datetime(year, month, day)
print("Test for getting errors by date:")
t2 = get_errors_by_review_date(errors, datetime.datetime(2020, 1, 2), datetime.datetime(2020, 3, 3))
for i in t2:
    print(i)

print("\n\n")


# This method returns all of the errors based on name
# just search for an individual)
def get_errors_by_name(a, name):
    errors_by_name = []
    for x in a:
        if (name in x[6]) or (name in x[5]) or (name in x[4]):
            errors_by_name.append(x)

    return errors_by_name


# TEST get_errors_by_name
print("Test for getting errors by name")
t3 = get_errors_by_name(errors, "Sarah Woe")
for i in t3:
    print(i)

print("\n\n")


# This method returns all of the errors based on review type
# Input should either be "SUPERVISORY REVIEW", "MANAGER REVIEW", "DIRECTOR REVIEW", "Inter-office file review", or "QUALITY REVIEW"
def get_errors_by_review_type(a, type):
    errors_by_type = []
    for x in a:
        if type == x[0]:
            errors_by_type.append(x)

    return errors_by_type

# TEST get_errors_by_review_type
print("Test for getting errors by review type")
t4 = get_errors_by_review_type(errors,"SUPERVISORY REVIEW")
for x in t4:
    print(x)





