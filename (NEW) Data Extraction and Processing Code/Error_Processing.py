import datetime


# This method is used to parse dates to create correct date/time object
# This is format getting spliced "12/31/33"
def format_date(s):
    # This creates an array of the number is the date split by "/"
    n = s.split("/")
    month = int(n[0])
    day = int(n[1])
    year = int(n[2])

    return datetime.datetime(year, month, day)


# ARRAY FORMAT CONTAINING EXTRACTED DATA
# FIRST 6 PARAMETERS ARE CONSTANT FROM EACH SHEET
# LAST 5 PARAMETERS FROM EACH ROW
# {“PROVIDER NAME:”, “PROVIDER #:”, “FISCAL YEAR END:”,
# “REVIEWER:”, "3RD LEVEL RVWR", "2ND LEVEL RVWR",
# “IN-CHARGE:”, “DATE REVIEWED:”, “WKPR REF”,
# “POINT #”, “REVIEW POINT”, “DISPOSITION, INITIALS, DATE”,
# “UDR/Exhibit Step/IOM Chap 8 Ref”}

# SAMPLE DATA
error1 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/2/2035', 'LDR', 1.0, 'Addendum initial step 1 is referencing the phone log, but I am not seeing it in the Corr tab.', 'Phone log is added. XX 1/2/2035', '60.8C11']
error2 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/2/2035', 'L-A2', 2.0, 'This needs to be set up as a workpaper.  There is a template for it.  The adjustments have changed a little bit since this was done.  See note below about the NPR.', 'WP has been updated. XX 1/2/2035', '60.8C4']
error3 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/2/2035', 'L-C4', 3.0, "The AP listed on the WP don't match the SOI.", 'AP numbers are corrected on L-C4. XX 1/2/2035', '60.8C11']
error4 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/2/2035', 'L-E1', 4.0, 'On the LDR this step is listed as being done as AP#8 and the x-ref to L-E1 is not lieted.   Also the WP Ref needs to be added to the top left of the WP.  The Adj Ref needs to be added also.  Note that the AAR is not in the file.', 'WP L-E1 and L has been updated.XX 1/2/2035', '60.8C11']
error5 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/2/2035', 'SOPA', 'Note', 'Please fill out the Summary of Passed Adjustments.', 'Done. XX 1/2/2035', 'n/a']



error6 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', 'Director', 'Supervisor, Manager', '1/5/2035', 'Exit ', 1.0, "Exit document has 12/31/16 instead of 12/31/18.    Did Provider ever reply?  Please add a note if they ever replied or not.  It's not clear if we were planning to combine the pre-exit and exit conference.  The Provider should have the right for both pre-exit and exit.  Please keep this in mind for future.  ", "Date has been corrected on pg 22. Provider never respond my emails and phone call so, pre-exits and exits were performed together. Will note for future Audit to performed pre-exit and exit separately. No response from provider as of today's date. XX 1/5/2035", 'NA']
error7 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', 'Director', 'Supervisor, Manager', '1/5/2035', 'IME/GME', 'Note', 'Please make sure all the issues addressed in the JE OY 5 QASP are covered in this audit.', 'OY-5 QASP findings appear related to resident rotations.  A PFNY has been written to review elective rotaions in 6/30/2017.  XX 1/5/2035', 'NA']
error8 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', 'Director', 'Supervisor, Manager', '1/5/2035', 'BD Audit  ', 2.0, 'Sec 14 - BD Listings should have PBP or Prepared by Provider. ', 'PBP added in 14-03-2a and 14-03-3a. XX 1/5/2035', 'NA']
error9 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', 'Director', 'Supervisor, Manager', '1/5/2035', 'DSH Listing ', 3.0, '15-07-01 Source: Documents submitted by provider upon request   We should include the name of the document in the source.', 'Name of the documents added in source. XX 1/5/2035', 'NA']
error10 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', 'Director', 'Supervisor, Manager', '1/5/2035', 'BD Scope', 'Note', "AP 10 - Please include the type of BD that were scoped for review (Medicare regular BD and/or Medicare Crossover BD).  The WP's and BD Audit Program also don’t clearly state which type of BD were scoped. If regular BD were scoped, we should request for the BD Policy for the Perm File. ", 'AP 10 in SOI has been updated as crossover IP and crossover OP bad debts. XX 1/5/2035', 'NA']



error11 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', "Manager's Name", "Supervisor's Name", "Auditor's Name", '1/4/2035', 'L-G1', 1.0, "Foot, or re-calculate, the bad debt totals on the provider's listings to verify the totals are calcualted correctly.  There have been times when the provider's calculations or formulas are not correct.  (Note, the easiest way to do this is through the Excel bad debt listing file where you can highlight all the amounts and see the total in the lower right corner of the Excel document).  Use the f tickmark to indicate you footed the totals.\n", 'Calculated by Auditors and f tickmarks added in WP. XX 1/4/2035', 'PRM-I, Chap 3']
error12 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', "Manager's Name", "Supervisor's Name", "Auditor's Name", '1/4/2035', 'Module K', 'Note', 'Please update the remark on the Module K to indicate whether any issues were noted.', 'Comment Updated. XX 1/4/2035', '60.8C12']
error13 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', "Manager's Name", "Supervisor's Name", "Auditor's Name", '1/4/2035', 13.0, 2.0, 'The Exhibit 13 Index shows section 12 being scoped, but there are no section 13-12 workpapers in the file.  Please update workpaper 13 or add the workpapers.\n', 'Workpaper has been updated. XX 1/4/2035', '60.8C17']
error14 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', "Manager's Name", "Supervisor's Name", "Auditor's Name", '1/4/2035', '13-16', 3.0, "There are multiple steps on 13-16 and all reference workpaper 13-16-01.  The work performed on 13-16-01 doesn't appear to address every step on 13-16.  Please add comments to 13-16 steps clarify it was verified and how.\n", 'Comment added on some of the steps. XX 1/4/2035', '60.8C12']
error15 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', "Manager's Name", "Supervisor's Name", "Auditor's Name", '1/4/2035', '13-08-5d', 'Note', "The email evidence included in this workpaper is testimonial evidence by the provider.  Testimonial evidence is not as strong as documented evidence.  Is there any documented evidence that can be used to substantiate the provider's testimonial evidence (e.g., time studies, rotation schedule, contracts/agreements, etc.)?\n", 'Auditors added a note on pg 1.XX 1/4/2035', '']
error16 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', "Manager's Name", "Supervisor's Name", "Auditor's Name", '1/4/2035', '15-07-4a', 4.0, "Where is the RAT-STATs sample documentation for this workpaper?\n\nThere were 40 out of 481 errors, so I calculate the error rate to be 8%.  Why wasn't that extrapolated?\n", 'Listings were reviewed at 100%. XX 1/4/2035', '']



error17 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/3/2035', 'Audit Index', 5.0, 'Sign-off as the preparer in the WPM binder.', 'Signed off. XX 1/3/2035', '--']
error18 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/3/2035', '01', 6.0, 'Add a workpaper reference, initials and date the upper right-hand corner of the lead sheet.', 'WP updated with all the information. XX 1/3/2035', '60.8C2']
error19 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/3/2035', '01', 7.0, 'Add the audit program to this workpaper.', 'Added.XX 1/3/2035', '60.8C13']
error20 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/3/2035', '01-1-1', 8.0, 'Initial and date the upper right-hand corner of the workpaper.', 'Added. XX 1/3/2035', '60.8C2']
error21 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/3/2035', '01-1-1', 9.0, 'A blank form for the entrance conference is attached to the workpaper.  There should be a completed form documenting the entrance conference.  Add the completed form to the workpaper.', 'WP updated with all the information. XX 1/3/2035', '60.8C12']
error22 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/3/2035', 'AAR', 10.0, 'Ref. #25.  The adjustment to W/S E-4 shows a workpaper reference of 15-15-01.  This should be 13-15-01.', 'Corrected. XX 1/3/2035', 70.4]
error23 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/3/2035', '14-03', 11.0, 'The provider name, city, provider number and FYE are incorrect in the heading.', 'Corrected. XX 1/3/2035', '60.8C1']
error24 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/3/2035', '14-03-3a      Pg. 2', 12.0, 'The anticipated rate of occurance for the sample was 5%.  Since the error rate is below the anticipated rate of occurance, only the errors in the sample should be disallowed.  There would be no extrapolation.', 'WP has been corrected. XX 1/3/2035', 60.6]
error25 = ['ABC Hospital', 'XX-XXXX', '12/31/2033', 'No 3rd level review.', 'No 2nd level review.', "Supervisor's Name", "Auditor's Name", '1/3/2035', '15-07-01', 13.0, 'Each listing should have a subtotal.  The subtotals should total the number of days being claimed by the provider.  Add subtotals to each section of days.', 'Subtotal has been added on pg 96,99, 127 and 128. XX 1/3/2035', '60.8C12']

errors = [error1, error2, error3, error4, error5, error6, error7, error8, error9, error10, error11, error12, error13, error14, error15, error16, error17, error18, error19, error20, error21, error22, error23, error24, error25]


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


# UNIT TEST get_errors_by_review_date
t2 = get_errors_by_review_date(errors, datetime.datetime(2010, 5, 5), datetime.datetime(2050, 5, 5))
for i in t2:
    print(i)
