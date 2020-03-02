# Author: William Fleck
# Created on: 02/27/2020
# Description: Definition of the Error class

from datetime import datetime


class Error:
    def __init__(self, date, error_code):
        self.date = date
        self.error_code = error_code

    def get_date(self):
        return self.date

    def get_error_code(self):
        return self.error_code

    def to_string(self):
        return 'IOM violation {} on {}'.format(self.error_code, self.date)

    # The first method is to return error objects within a certain date range
    # First argument is array of error objects
    # Second argument is the start of date range
    # Third argument is end of date range
    # date format should be using example December 17, 2016 "datetime.datetime(2016, 17, 12)"
    @staticmethod
    def get_errors_by_date(a, d1, d2):
        errors_by_date = []

        for x in a:
            if d1 <= x.get_date() <= d2:
                errors_by_date.append(x)

        return errors_by_date

    @staticmethod
    def get_errors_by_error_type(a, e_type):
        errors_by_error_type = []
        for x in a:
            if x.get_error_code() == e_type:
                errors_by_error_type.append(x)
        return errors_by_error_type

    @staticmethod
    def get_errors_by_error_type_and_date(a, d1, d2, e_type):
        errors_by_error_type_and_date = []
        for x in a:
            if (d1 <= x.get_date() <= d2) and x.get_error_code() == e_type:
                errors_by_error_type_and_date.append(x)
        return errors_by_error_type_and_date


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

errors = [Error(datetime(2015, 4, 12), "60.8C1"),
          Error(datetime(2015, 5, 15), "60.8C1"),
          Error(datetime(2018, 6, 17), "60.8C2"),
          Error(datetime(2016, 7, 19), "60.8C3"),
          Error(datetime(2017, 8, 10), "60.8C4"),
          Error(datetime(2015, 9, 13), "60.8C5"),
          Error(datetime(2013, 1, 22), "60.8C6"),
          Error(datetime(2014, 4, 25), "60.8C7"),
          Error(datetime(2017, 3, 27), "60.8C8"),
          Error(datetime(2018, 5, 29), "60.8C9"),
          Error(datetime(2019, 6, 12), "60.8C10"),
          Error(datetime(2020, 7, 2), "60.8C11"),
          Error(datetime(2014, 7, 4), "60.8C12"),
          Error(datetime(2016, 3, 6), "60.8C13"),
          Error(datetime(2017, 9, 9), "60.8C14"),
          Error(datetime(2013, 10, 24), "60.8C15"),
          Error(datetime(2016, 12, 23), "60.8C16"),
          Error(datetime(2012, 11, 14), "60.8C17"),
          Error(datetime(2015, 2, 2), "60.8C18"),
          Error(datetime(2016, 3, 9), "60.8C1"),
          Error(datetime(2017, 4, 3), "60.8C2"),
          Error(datetime(2018, 5, 15), "60.8C3"),
          Error(datetime(2019, 6, 25), "60.8C4"),
          Error(datetime(2018, 7, 12), "60.8C5"),
          Error(datetime(2019, 8, 16), "60.8C6"),
          Error(datetime(2020, 9, 19), "60.8C7"),
          Error(datetime(2019, 10, 5), "60.8C8")]


# UNIT TEST def get_errors_by_date(a, d1, d2):
t1 = Error.get_errors_by_date(errors, datetime(2015, 1, 1), datetime(2019, 1, 1))
for x in t1:
    print(x.to_string())

# UNIT TEST def get_errors_by_error_type(a, e_type):
t2 = Error.get_errors_by_error_type(errors, '60.8C5')
for i in t2:
    print(i.to_string())

# UNIT TEST def get_errors_by_error_type_and_date(a, d1, d2, e_type):

