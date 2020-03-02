# Array to hold all error objects used to test code
import datetime


class Error:
    def __init__(self, contract_type, date, error_code):
        self.contractType = contract_type
        self.date = date
        self.errorCode = error_code

    def get_contract_type(self):
        return self.contractType

    def get_date(self):
        return self.date

    def get_error_code(self):
        return self.errorCode


# Array containing errors to be used for testing
# Errors are added below
errors = []

# Instantiating errors to add to "errors" array
# Argument list is: contract_type, date, error_code
# Contract types are long-term, medium-term, or short-term
# Error types are: 
# 60.8C1
# 60.8C2
# 60.8C3
# 60.8C4
# 60.8C5
# 60.8C6
# 60.8C7
# 60.8C8
# 60.8C9
# 60.8C10
# 60.8C11
# 60.8C12
# 60.8C13
# 60.8C14
# 60.8C15
# 60.8C16
# 60.8C17
# 60.8C18

errors = [("long-term", datetime.datetime(2015, 4, 12), "60.8C1"),
          (Error("long-term", datetime.datetime(2015, 5, 15), "60.8C1")),
          (Error("short-term", datetime.datetime(2018, 6, 17), "60.8C2")),
          (Error("short-term", datetime.datetime(2016, 7, 19), "60.8C3")),
          (Error("medium-term", datetime.datetime(2017, 8, 10), "60.8C4")),
          (Error("medium-term", datetime.datetime(2015, 9, 13), "60.8C5")),
          (Error("long-term", datetime.datetime(2013, 1, 22), "60.8C6")),
          (Error("long-term", datetime.datetime(2014, 4, 25), "60.8C7")),
          (Error("short-term", datetime.datetime(2017, 3, 27), "60.8C8")),
          (Error("short-term", datetime.datetime(2018, 5, 29), "60.8C9")),
          (Error("short-term", datetime.datetime(2019, 6, 12), "60.8C10")),
          (Error("short-term", datetime.datetime(2020, 7, 2), "60.8C11")),
          (Error("medium-term", datetime.datetime(2014, 7, 4), "60.8C12")),
          (Error("medium-term", datetime.datetime(2016, 3, 6), "60.8C13")),
          (Error("long-term", datetime.datetime(2017, 9, 9), "60.8C14")),
          (Error("short-term", datetime.datetime(2013, 10, 24), "60.8C15")),
          (Error("short-term", datetime.datetime(2016, 12, 23), "60.8C16")),
          (Error("medium-term", datetime.datetime(2012, 11, 14), "60.8C17")),
          (Error("medium-term", datetime.datetime(2015, 2, 2), "60.8C18")),
          (Error("long-term", datetime.datetime(2016, 3, 9), "60.8C1")),
          (Error("long-term", datetime.datetime(2017, 4, 3), "60.8C2")),
          (Error("short-term", datetime.datetime(2018, 5, 15), "60.8C3")),
          (Error("short-term", datetime.datetime(2019, 6, 25), "60.8C4")),
          (Error("short-term", datetime.datetime(2018, 7, 12), "60.8C5")),
          (Error("short-term", datetime.datetime(2019, 8, 16), "60.8C6")),
          (Error("medium-term", datetime.datetime(2020, 9, 19), "60.8C7")),
          (Error("medium-term", datetime.datetime(2019, 10, 5), "60.8C8"))]


# The first method is to return error objects within a certain date range
# First argument is array of error objects
# Second argument is the start of date range
# Third argument is end of date range
# date format should be using example December 17, 2016 "datetime.datetime(2016, 17, 12)"
def get_errors_by_date(a, d1, d2):
    errors_by_date = []

    for x in a:
        if d1 <= x.get_date() <= d2:
            errors_by_date.append(x)

    return errors_by_date


# This method will return all errors of a certain contract type
# Contract type should be either: "short-term", "medium-term", "long-term"
# First parameter is array of errors
# Second parameters is contract type
def get_errors_by_contract_type(a, c_type):
    errors_by_contract_type = []
    for x in a:
        if x.get_contract_type() == c_type:
            errors_by_contract_type.append(x)
    return errors_by_contract_type


def get_errors_by_error_type(a, e_type):
    errors_by_error_type = []
    for x in a:
        if x.get_error_code() == e_type:
            errors_by_error_type.append(x)
    return errors_by_error_type


# Returns array of errors based on error type and date
def get_errors_by_error_type_and_date(a, d1, d2, e_type):
    errors_by_error_type_and_date = []
    for x in a:
        if (d1 <= x.get_date() <= d2) and x.get_error_code() == e_type:
            errors_by_error_type_and_date.append(x)
    return errors_by_error_type_and_date


# Returns array of errors based on error type and contract type
def get_errors_by_contract_type_and_error_type(a, c_type, e_type):
    errors_by_contract_type_and_error_type = []
    for x in a:
        if x.get_contract_type == c_type and x.get_error_code() == e_type:
            errors_by_contract_type_and_error_type.append(x)
    return errors_by_contract_type_and_error_type


# Returns array of errors based on date and contract type
def get_errors_by_contract_type_and_date(a, d1, d2, c_type):
    errors_by_contract_type_and_date = []
    for x in a:
        if (d1 <= x.get_date() <= d2) and x.get_contract_type == c_type:
            errors_by_contract_type_and_date.append(x)
    return errors_by_contract_type_and_date


# Returns array of errors based on date, error, and contract type
def get_errors_by_contract_and_error_type_and_date(a, d1, d2, c_type, e_type):
    errors_all = []
    for x in a:
        if (d1 <= x.get_date() <= d2) and x.get_contract_type == c_type and x.get_error_code() == e_type:
            errors_all.append(x)
    return errors_all


# UNIT TEST def get_errors_by_date(a, d1, d2):
t1 = get_errors_by_date(errors, datetime.datetime(2015, 1, 1), datetime.datetime(2019, 1, 1))
for x in t1:
    print(x)

# UNIT TEST def get_errors_by_contract_type(a, c_type):


# UNIT TEST def get_errors_by_error_type(a, e_type):


# UNIT TEST def get_errors_by_error_type_and_date(a, d1, d2, e_type):


# UNIT TEST def get_errors_by_contract_type_and_error_type(a, c_type, e_type):


# UNIT TEST def get_errors_by_contract_type_and_error_type(a, c_type, e_type):


# UNIT TEST def get_errors_by_contract_type_and_date(a, d1, d2, c_type):


# UNIT TEST def get_errors_by_contract_and_error_type_and_date(a, d1, d2, c_type, e_type):
