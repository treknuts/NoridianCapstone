# Ignore red underline it works
# from pathlib import Path
# dataFolder = Path("DataManipulationExtraction\src")
# from DataManipulationExtraction.src import *
# import DataManipulationExtraction.src.data_extraction
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


# SAMPLE DATA
errors = [
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Jared Noun', 'Auditor: Bob Low',
     '1/2/2020', 'LDR', 1.0,
     'Addendum initial step 1 is referencing the phone log, but I am not seeing it in the Corr tab.',
     'Phone log is added. XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Jared Noun', 'Auditor: Bob Low',
     '1/2/2020', 'L-A2', 2.0,
     'This needs to be set up as a workpaper.  There is a template for it.  The adjustments have changed a little bit since this was done.  See note below about the NPR.',
     'WP has been updated. XX 1/2/2035', '60.8C4'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Jared Noun', 'Auditor: Bob Low',
     '1/2/2020', 'L-C4', 3.0, "The AP listed on the WP don't match the SOI.",
     'AP numbers are corrected on L-C4. XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Jared Noun', 'Auditor: Bob Low',
     '1/2/2020', 'L-E1', 4.0,
     'On the LDR this step is listed as being done as AP#8 and the x-ref to L-E1 is not lieted.   Also the WP Ref needs to be added to the top left of the WP.  The Adj Ref needs to be added also.  Note that the AAR is not in the file.',
     'WP L-E1 and L has been updated.XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Jared Noun', 'Auditor: Bob Low',
     '1/2/2020', 'SOPA', 'Note', 'Please fill out the Summary of Passed Adjustments.', 'Done. XX 1/2/2035', 'n/a'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Jared Noun', 'Auditor: Bob Low',
     '1/2/2020', 'Sample', 5.0, 'Sample', 'Sample', '60.8C5'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Jared Noun', 'Auditor: Bob Low',
     '1/2/2020', 'Sample', 6.0, 'Sample', 'Sample', '60.8C5'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Jared Noun', 'Auditor: Bob Low',
     '1/2/2020', 'Sample', 7.0, 'Sample', 'Sample', '60.8C5'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Jared Noun', 'Auditor: Bob Low',
     '1/2/2020', 'Sample', 8.0, 'Sample', 'Sample', '60.8C5'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Jared Noun', 'Auditor: Bob Low',
     '1/2/2020', 'Sample', 9.0, 'Sample', 'Sample', '60.8C5'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Keisha Graw', 'Auditor: Sarah Woe',
     '2/2/2020', 'LDR', 1.0,
     'Addendum initial step 1 is referencing the phone log, but I am not seeing it in the Corr tab.',
     'Phone log is added. XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Keisha Graw', 'Auditor: Sarah Woe',
     '2/2/2020', 'L-A2', 2.0,
     'This needs to be set up as a workpaper.  There is a template for it.  The adjustments have changed a little bit since this was done.  See note below about the NPR.',
     'WP has been updated. XX 1/2/2035', '60.8C4'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Keisha Graw', 'Auditor: Sarah Woe',
     '2/2/2020', 'L-C4', 3.0, "The AP listed on the WP don't match the SOI.",
     'AP numbers are corrected on L-C4. XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Keisha Graw', 'Auditor: Sarah Woe',
     '2/2/2020', 'L-E1', 4.0,
     'On the LDR this step is listed as being done as AP#8 and the x-ref to L-E1 is not lieted.   Also the WP Ref needs to be added to the top left of the WP.  The Adj Ref needs to be added also.  Note that the AAR is not in the file.',
     'WP L-E1 and L has been updated.XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Keisha Graw', 'Auditor: Sarah Woe',
     '2/2/2020', 'SOPA', 'Note', 'Please fill out the Summary of Passed Adjustments.', 'Done. XX 1/2/2035', 'n/a'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Keisha Graw', 'Auditor: Sarah Woe',
     '2/2/2020', 'Sample', 5.0, 'Sample', 'Sample', '60.8C10'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Keisha Graw', 'Auditor: Sarah Woe',
     '2/2/2020', 'Sample', 6.0, 'Sample', 'Sample', '60.8C10'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Keisha Graw', 'Auditor: Sarah Woe',
     '2/2/2020', 'Sample', 7.0, 'Sample', 'Sample', '60.8C10'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Keisha Graw', 'Auditor: Sarah Woe',
     '2/2/2020', 'Sample', 8.0, 'Sample', 'Sample', '60.8C10'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Keisha Graw', 'Auditor: Sarah Woe',
     '2/2/2020', 'Sample', 9.0, 'Sample', 'Sample', '60.8C10'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/2/2020', 'LDR', 1.0,
     'Addendum initial step 1 is referencing the phone log, but I am not seeing it in the Corr tab.',
     'Phone log is added. XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/2/2020', 'L-A2', 2.0,
     'This needs to be set up as a workpaper.  There is a template for it.  The adjustments have changed a little bit since this was done.  See note below about the NPR.',
     'WP has been updated. XX 1/2/2035', '60.8C4'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/2/2020', 'L-C4', 3.0, "The AP listed on the WP don't match the SOI.",
     'AP numbers are corrected on L-C4. XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/2/2020', 'L-E1', 4.0,
     'On the LDR this step is listed as being done as AP#8 and the x-ref to L-E1 is not lieted.   Also the WP Ref needs to be added to the top left of the WP.  The Adj Ref needs to be added also.  Note that the AAR is not in the file.',
     'WP L-E1 and L has been updated.XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/2/2020', 'SOPA', 'Note', 'Please fill out the Summary of Passed Adjustments.',
     'Done. XX 1/2/2035', 'n/a'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/2/2020', 'Sample', 5.0, 'Sample', 'Sample', '60.8C12'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/2/2020', 'Sample', 6.0, 'Sample', 'Sample', '60.8C12'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/2/2020', 'Sample', 7.0, 'Sample', 'Sample', '60.8C12'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/2/2020', 'Sample', 8.0, 'Sample', 'Sample', '60.8C12'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/2/2020', 'Sample', 9.0, 'Sample', 'Sample', '60.8C12'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Rob Taft', 'Auditor: John Dew',
     '4/2/2020', 'LDR', 1.0,
     'Addendum initial step 1 is referencing the phone log, but I am not seeing it in the Corr tab.',
     'Phone log is added. XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Rob Taft', 'Auditor: John Dew',
     '4/2/2020', 'L-A2', 2.0,
     'This needs to be set up as a workpaper.  There is a template for it.  The adjustments have changed a little bit since this was done.  See note below about the NPR.',
     'WP has been updated. XX 1/2/2035', '60.8C4'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Rob Taft', 'Auditor: John Dew',
     '4/2/2020', 'L-C4', 3.0, "The AP listed on the WP don't match the SOI.",
     'AP numbers are corrected on L-C4. XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Rob Taft', 'Auditor: John Dew',
     '4/2/2020', 'L-E1', 4.0,
     'On the LDR this step is listed as being done as AP#8 and the x-ref to L-E1 is not lieted.   Also the WP Ref needs to be added to the top left of the WP.  The Adj Ref needs to be added also.  Note that the AAR is not in the file.',
     'WP L-E1 and L has been updated.XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Rob Taft', 'Auditor: John Dew',
     '4/2/2020', 'SOPA', 'Note', 'Please fill out the Summary of Passed Adjustments.', 'Done. XX 1/2/2035', 'n/a'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Rob Taft', 'Auditor: John Dew',
     '4/2/2020', 'Sample', 5.0, 'Sample', 'Sample', '60.8C16'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Rob Taft', 'Auditor: John Dew',
     '4/2/2020', 'Sample', 6.0, 'Sample', 'Sample', '60.8C16'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Rob Taft', 'Auditor: John Dew',
     '4/2/2020', 'Sample', 7.0, 'Sample', 'Sample', '60.8C16'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Rob Taft', 'Auditor: John Dew',
     '4/2/2020', 'Sample', 8.0, 'Sample', 'Sample', '60.8C16'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Rob Taft', 'Auditor: John Dew',
     '4/2/2020', 'Sample', 9.0, 'Sample', 'Sample', '60.8C16'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Abe Conner', 'Auditor: Misha King',
     '5/2/2020', 'LDR', 1.0,
     'Addendum initial step 1 is referencing the phone log, but I am not seeing it in the Corr tab.',
     'Phone log is added. XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Abe Conner', 'Auditor: Misha King',
     '5/2/2020', 'L-A2', 2.0,
     'This needs to be set up as a workpaper.  There is a template for it.  The adjustments have changed a little bit since this was done.  See note below about the NPR.',
     'WP has been updated. XX 1/2/2035', '60.8C4'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Abe Conner', 'Auditor: Misha King',
     '5/2/2020', 'L-C4', 3.0, "The AP listed on the WP don't match the SOI.",
     'AP numbers are corrected on L-C4. XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Abe Conner', 'Auditor: Misha King',
     '5/2/2020', 'L-E1', 4.0,
     'On the LDR this step is listed as being done as AP#8 and the x-ref to L-E1 is not lieted.   Also the WP Ref needs to be added to the top left of the WP.  The Adj Ref needs to be added also.  Note that the AAR is not in the file.',
     'WP L-E1 and L has been updated.XX 1/2/2035', '60.8C11'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Abe Conner', 'Auditor: Misha King',
     '5/2/2020', 'SOPA', 'Note', 'Please fill out the Summary of Passed Adjustments.', 'Done. XX 1/2/2035', 'n/a'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Abe Conner', 'Auditor: Misha King',
     '5/2/2020', 'Sample', 5.0, 'Sample', 'Sample', '60.8C13'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Abe Conner', 'Auditor: Misha King',
     '5/2/2020', 'Sample', 6.0, 'Sample', 'Sample', '60.8C13'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Abe Conner', 'Auditor: Misha King',
     '5/2/2020', 'Sample', 7.0, 'Sample', 'Sample', '60.8C13'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Abe Conner', 'Auditor: Misha King',
     '5/2/2020', 'Sample', 8.0, 'Sample', 'Sample', '60.8C13'],
    ['SUPERVISORY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', '', 'Supervisor: Abe Conner', 'Auditor: Misha King',
     '5/2/2020', 'Sample', 9.0, 'Sample', 'Sample', '60.8C13'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Helen Joe', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/4/2020', 'L-G1', 1.0,
     "Foot, or re-calculate, the bad debt totals on the provider's listings to verify the totals are calcualted correctly.  There have been times when the provider's calculations or formulas are not correct.  (Note, the easiest way to do this is through the Excel bad debt listing file where you can highlight all the amounts and see the total in the lower right corner of the Excel document).  Use the f tickmark to indicate you footed the totals.\n",
     'Calculated by Auditors and f tickmarks added in WP. XX 1/4/2035', 'PRM-I, Chap 3'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Helen Joe', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/4/2020', 'Module K', 'Note',
     'Please update the remark on the Module K to indicate whether any issues were noted.',
     'Comment Updated. XX 1/4/2035', '60.8C12'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Helen Joe', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/4/2020', 13.0, 2.0,
     'The Exhibit 13 Index shows section 12 being scoped, but there are no section 13-12 workpapers in the file.  Please update workpaper 13 or add the workpapers.\n',
     'Workpaper has been updated. XX 1/4/2035', '60.8C17'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Helen Joe', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/4/2020', '13-16', 3.0,
     "There are multiple steps on 13-16 and all reference workpaper 13-16-01.  The work performed on 13-16-01 doesn't appear to address every step on 13-16.  Please add comments to 13-16 steps clarify it was verified and how.\n",
     'Comment added on some of the steps. XX 1/4/2035', '60.8C12'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Helen Joe', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/4/2020', '13-08-5d', 'Note',
     "The email evidence included in this workpaper is testimonial evidence by the provider.  Testimonial evidence is not as strong as documented evidence.  Is there any documented evidence that can be used to substantiate the provider's testimonial evidence (e.g., time studies, rotation schedule, contracts/agreements, etc.)?\n",
     'Auditors added a note on pg 1.XX 1/4/2035', ''],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Helen Joe', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/4/2020', '15-07-4a', 4.0,
     "Where is the RAT-STATs sample documentation for this workpaper?\n\nThere were 40 out of 481 errors, so I calculate the error rate to be 8%.  Why wasn't that extrapolated?\n",
     'Listings were reviewed at 100%. XX 1/4/2035', ''],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Helen Joe', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/4/2020', 'Sample', 5.0, 'Sample', 'Sample', '60.8C5'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Helen Joe', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/4/2020', 'Sample', 6.0, 'Sample', 'Sample', '60.8C5'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Helen Joe', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/4/2020', 'Sample', 7.0, 'Sample', 'Sample', '60.8C5'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Helen Joe', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/4/2020', 'Sample', 8.0, 'Sample', 'Sample', '60.8C5'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Helen Joe', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/4/2020', 'Sample', 9.0, 'Sample', 'Sample', '60.8C5'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Sisa Smith', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/4/2020', 'L-G1', 1.0,
     "Foot, or re-calculate, the bad debt totals on the provider's listings to verify the totals are calcualted correctly.  There have been times when the provider's calculations or formulas are not correct.  (Note, the easiest way to do this is through the Excel bad debt listing file where you can highlight all the amounts and see the total in the lower right corner of the Excel document).  Use the f tickmark to indicate you footed the totals.\n",
     'Calculated by Auditors and f tickmarks added in WP. XX 1/4/2035', 'PRM-I, Chap 3'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Sisa Smith', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/4/2020', 'Module K', 'Note',
     'Please update the remark on the Module K to indicate whether any issues were noted.',
     'Comment Updated. XX 1/4/2035', '60.8C12'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Sisa Smith', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/4/2020', 13.0, 2.0,
     'The Exhibit 13 Index shows section 12 being scoped, but there are no section 13-12 workpapers in the file.  Please update workpaper 13 or add the workpapers.\n',
     'Workpaper has been updated. XX 1/4/2035', '60.8C17'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Sisa Smith', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/4/2020', '13-16', 3.0,
     "There are multiple steps on 13-16 and all reference workpaper 13-16-01.  The work performed on 13-16-01 doesn't appear to address every step on 13-16.  Please add comments to 13-16 steps clarify it was verified and how.\n",
     'Comment added on some of the steps. XX 1/4/2035', '60.8C12'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Sisa Smith', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/4/2020', '13-08-5d', 'Note',
     "The email evidence included in this workpaper is testimonial evidence by the provider.  Testimonial evidence is not as strong as documented evidence.  Is there any documented evidence that can be used to substantiate the provider's testimonial evidence (e.g., time studies, rotation schedule, contracts/agreements, etc.)?\n",
     'Auditors added a note on pg 1.XX 1/4/2035', ''],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Sisa Smith', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/4/2020', '15-07-4a', 4.0,
     "Where is the RAT-STATs sample documentation for this workpaper?\n\nThere were 40 out of 481 errors, so I calculate the error rate to be 8%.  Why wasn't that extrapolated?\n",
     'Listings were reviewed at 100%. XX 1/4/2035', ''],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Sisa Smith', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/4/2020', 'Sample', 5.0, 'Sample', 'Sample', '60.8C10'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Sisa Smith', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/4/2020', 'Sample', 6.0, 'Sample', 'Sample', '60.8C10'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Sisa Smith', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/4/2020', 'Sample', 7.0, 'Sample', 'Sample', '60.8C10'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Sisa Smith', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/4/2020', 'Sample', 8.0, 'Sample', 'Sample', '60.8C10'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Sisa Smith', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/4/2020', 'Sample', 9.0, 'Sample', 'Sample', '60.8C10'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Bobbie Cran', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/4/2020', 'L-G1', 1.0,
     "Foot, or re-calculate, the bad debt totals on the provider's listings to verify the totals are calcualted correctly.  There have been times when the provider's calculations or formulas are not correct.  (Note, the easiest way to do this is through the Excel bad debt listing file where you can highlight all the amounts and see the total in the lower right corner of the Excel document).  Use the f tickmark to indicate you footed the totals.\n",
     'Calculated by Auditors and f tickmarks added in WP. XX 1/4/2035', 'PRM-I, Chap 3'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Bobbie Cran', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/4/2020', 'Module K', 'Note',
     'Please update the remark on the Module K to indicate whether any issues were noted.',
     'Comment Updated. XX 1/4/2035', '60.8C12'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Bobbie Cran', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/4/2020', 13.0, 2.0,
     'The Exhibit 13 Index shows section 12 being scoped, but there are no section 13-12 workpapers in the file.  Please update workpaper 13 or add the workpapers.\n',
     'Workpaper has been updated. XX 1/4/2035', '60.8C17'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Bobbie Cran', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/4/2020', '13-16', 3.0,
     "There are multiple steps on 13-16 and all reference workpaper 13-16-01.  The work performed on 13-16-01 doesn't appear to address every step on 13-16.  Please add comments to 13-16 steps clarify it was verified and how.\n",
     'Comment added on some of the steps. XX 1/4/2035', '60.8C12'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Bobbie Cran', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/4/2020', '13-08-5d', 'Note',
     "The email evidence included in this workpaper is testimonial evidence by the provider.  Testimonial evidence is not as strong as documented evidence.  Is there any documented evidence that can be used to substantiate the provider's testimonial evidence (e.g., time studies, rotation schedule, contracts/agreements, etc.)?\n",
     'Auditors added a note on pg 1.XX 1/4/2035', ''],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Bobbie Cran', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/4/2020', '15-07-4a', 4.0,
     "Where is the RAT-STATs sample documentation for this workpaper?\n\nThere were 40 out of 481 errors, so I calculate the error rate to be 8%.  Why wasn't that extrapolated?\n",
     'Listings were reviewed at 100%. XX 1/4/2035', ''],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Bobbie Cran', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/4/2020', 'Sample', 5.0, 'Sample', 'Sample', '60.8C3'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Bobbie Cran', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/4/2020', 'Sample', 6.0, 'Sample', 'Sample', '60.8C3'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Bobbie Cran', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/4/2020', 'Sample', 7.0, 'Sample', 'Sample', '60.8C3'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Bobbie Cran', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/4/2020', 'Sample', 8.0, 'Sample', 'Sample', '60.8C3'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Bobbie Cran', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/4/2020', 'Sample', 9.0, 'Sample', 'Sample', '60.8C3'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Lowe James', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/4/2020', 'L-G1', 1.0,
     "Foot, or re-calculate, the bad debt totals on the provider's listings to verify the totals are calcualted correctly.  There have been times when the provider's calculations or formulas are not correct.  (Note, the easiest way to do this is through the Excel bad debt listing file where you can highlight all the amounts and see the total in the lower right corner of the Excel document).  Use the f tickmark to indicate you footed the totals.\n",
     'Calculated by Auditors and f tickmarks added in WP. XX 1/4/2035', 'PRM-I, Chap 3'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Lowe James', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/4/2020', 'Module K', 'Note',
     'Please update the remark on the Module K to indicate whether any issues were noted.',
     'Comment Updated. XX 1/4/2035', '60.8C12'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Lowe James', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/4/2020', 13.0, 2.0,
     'The Exhibit 13 Index shows section 12 being scoped, but there are no section 13-12 workpapers in the file.  Please update workpaper 13 or add the workpapers.\n',
     'Workpaper has been updated. XX 1/4/2035', '60.8C17'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Lowe James', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/4/2020', '13-16', 3.0,
     "There are multiple steps on 13-16 and all reference workpaper 13-16-01.  The work performed on 13-16-01 doesn't appear to address every step on 13-16.  Please add comments to 13-16 steps clarify it was verified and how.\n",
     'Comment added on some of the steps. XX 1/4/2035', '60.8C12'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Lowe James', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/4/2020', '13-08-5d', 'Note',
     "The email evidence included in this workpaper is testimonial evidence by the provider.  Testimonial evidence is not as strong as documented evidence.  Is there any documented evidence that can be used to substantiate the provider's testimonial evidence (e.g., time studies, rotation schedule, contracts/agreements, etc.)?\n",
     'Auditors added a note on pg 1.XX 1/4/2035', ''],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Lowe James', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/4/2020', '15-07-4a', 4.0,
     "Where is the RAT-STATs sample documentation for this workpaper?\n\nThere were 40 out of 481 errors, so I calculate the error rate to be 8%.  Why wasn't that extrapolated?\n",
     'Listings were reviewed at 100%. XX 1/4/2035', ''],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Lowe James', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/4/2020', 'Sample', 5.0, 'Sample', 'Sample', '60.8C14'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Lowe James', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/4/2020', 'Sample', 6.0, 'Sample', 'Sample', '60.8C14'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Lowe James', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/4/2020', 'Sample', 7.0, 'Sample', 'Sample', '60.8C14'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Lowe James', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/4/2020', 'Sample', 8.0, 'Sample', 'Sample', '60.8C14'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Lowe James', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/4/2020', 'Sample', 9.0, 'Sample', 'Sample', '60.8C14'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Pharah Set', 'Supervisor: Abe Connor',
     'Auditor: Misha King', '5/4/2020', 'L-G1', 1.0,
     "Foot, or re-calculate, the bad debt totals on the provider's listings to verify the totals are calcualted correctly.  There have been times when the provider's calculations or formulas are not correct.  (Note, the easiest way to do this is through the Excel bad debt listing file where you can highlight all the amounts and see the total in the lower right corner of the Excel document).  Use the f tickmark to indicate you footed the totals.\n",
     'Calculated by Auditors and f tickmarks added in WP. XX 1/4/2035', 'PRM-I, Chap 3'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Pharah Set', 'Supervisor: Abe Connor',
     'Auditor: Misha King', '5/4/2020', 'Module K', 'Note',
     'Please update the remark on the Module K to indicate whether any issues were noted.',
     'Comment Updated. XX 1/4/2035', '60.8C12'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Pharah Set', 'Supervisor: Abe Connor',
     'Auditor: Misha King', '5/4/2020', 13.0, 2.0,
     'The Exhibit 13 Index shows section 12 being scoped, but there are no section 13-12 workpapers in the file.  Please update workpaper 13 or add the workpapers.\n',
     'Workpaper has been updated. XX 1/4/2035', '60.8C17'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Pharah Set', 'Supervisor: Abe Connor',
     'Auditor: Misha King', '5/4/2020', '13-16', 3.0,
     "There are multiple steps on 13-16 and all reference workpaper 13-16-01.  The work performed on 13-16-01 doesn't appear to address every step on 13-16.  Please add comments to 13-16 steps clarify it was verified and how.\n",
     'Comment added on some of the steps. XX 1/4/2035', '60.8C12'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Pharah Set', 'Supervisor: Abe Connor',
     'Auditor: Misha King', '5/4/2020', '13-08-5d', 'Note',
     "The email evidence included in this workpaper is testimonial evidence by the provider.  Testimonial evidence is not as strong as documented evidence.  Is there any documented evidence that can be used to substantiate the provider's testimonial evidence (e.g., time studies, rotation schedule, contracts/agreements, etc.)?\n",
     'Auditors added a note on pg 1.XX 1/4/2035', ''],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Pharah Set', 'Supervisor: Abe Connor',
     'Auditor: Misha King', '5/4/2020', '15-07-4a', 4.0,
     "Where is the RAT-STATs sample documentation for this workpaper?\n\nThere were 40 out of 481 errors, so I calculate the error rate to be 8%.  Why wasn't that extrapolated?\n",
     'Listings were reviewed at 100%. XX 1/4/2035', ''],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Pharah Set', 'Supervisor: Abe Connor',
     'Auditor: Misha King', '5/4/2020', 'Sample', 5.0, 'Sample', 'Sample', '60.8C18'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Pharah Set', 'Supervisor: Abe Connor',
     'Auditor: Misha King', '5/4/2020', 'Sample', 6.0, 'Sample', 'Sample', '60.8C18'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Pharah Set', 'Supervisor: Abe Connor',
     'Auditor: Misha King', '5/4/2020', 'Sample', 7.0, 'Sample', 'Sample', '60.8C18'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Pharah Set', 'Supervisor: Abe Connor',
     'Auditor: Misha King', '5/4/2020', 'Sample', 8.0, 'Sample', 'Sample', '60.8C18'],
    ['MANAGER REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Manager: Pharah Set', 'Supervisor: Abe Connor',
     'Auditor: Misha King', '5/4/2020', 'Sample', 9.0, 'Sample', 'Sample', '60.8C18'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Paris Jackson', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/5/2020', 'Exit ', 1.0,
     "Exit document has 12/31/16 instead of 12/31/18.    Did Provider ever reply?  Please add a note if they ever replied or not.  It's not clear if we were planning to combine the pre-exit and exit conference.  The Provider should have the right for both pre-exit and exit.  Please keep this in mind for future.  ",
     "Date has been corrected on pg 22. Provider never respond my emails and phone call so, pre-exits and exits were performed together. Will note for future Audit to performed pre-exit and exit separately. No response from provider as of today's date. XX 1/5/2035",
     'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Paris Jackson', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/5/2020', 'IME/GME', 'Note',
     'Please make sure all the issues addressed in the JE OY 5 QASP are covered in this audit.',
     'OY-5 QASP findings appear related to resident rotations.  A PFNY has been written to review elective rotaions in 6/30/2017.  XX 1/5/2035',
     'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Paris Jackson', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/5/2020', 'BD Audit  ', 2.0,
     'Sec 14 - BD Listings should have PBP or Prepared by Provider. ',
     'PBP added in 14-03-2a and 14-03-3a. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Paris Jackson', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/5/2020', 'DSH Listing ', 3.0,
     '15-07-01 Source: Documents submitted by provider upon request   We should include the name of the document in the source.',
     'Name of the documents added in source. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Paris Jackson', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/5/2020', 'BD Scope', 'Note',
     "AP 10 - Please include the type of BD that were scoped for review (Medicare regular BD and/or Medicare Crossover BD).  The WP's and BD Audit Program also don’t clearly state which type of BD were scoped. If regular BD were scoped, we should request for the BD Policy for the Perm File. ",
     'AP 10 in SOI has been updated as crossover IP and crossover OP bad debts. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Paris Jackson', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/5/2020', 'Sample', 4.0, 'Sample', 'Sample', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Paris Jackson', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/5/2020', 'Sample', 5.0, 'Sample', 'Sample', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Paris Jackson', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/5/2020', 'Sample', 6.0, 'Sample', 'Sample', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Paris Jackson', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/5/2020', 'Sample', 7.0, 'Sample', 'Sample', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Paris Jackson', 'Supervisor: Jared Noun',
     'Auditor: Bob Low', '1/5/2020', 'Sample', 8.0, 'Sample', 'Sample', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Sean Conner', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/5/2020', 'Exit ', 1.0,
     "Exit document has 12/31/16 instead of 12/31/18.    Did Provider ever reply?  Please add a note if they ever replied or not.  It's not clear if we were planning to combine the pre-exit and exit conference.  The Provider should have the right for both pre-exit and exit.  Please keep this in mind for future.  ",
     "Date has been corrected on pg 22. Provider never respond my emails and phone call so, pre-exits and exits were performed together. Will note for future Audit to performed pre-exit and exit separately. No response from provider as of today's date. XX 1/5/2035",
     'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Sean Conner', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/5/2020', 'IME/GME', 'Note',
     'Please make sure all the issues addressed in the JE OY 5 QASP are covered in this audit.',
     'OY-5 QASP findings appear related to resident rotations.  A PFNY has been written to review elective rotaions in 6/30/2017.  XX 1/5/2035',
     'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Sean Conner', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/5/2020', 'BD Audit  ', 2.0,
     'Sec 14 - BD Listings should have PBP or Prepared by Provider. ',
     'PBP added in 14-03-2a and 14-03-3a. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Sean Conner', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/5/2020', 'DSH Listing ', 3.0,
     '15-07-01 Source: Documents submitted by provider upon request   We should include the name of the document in the source.',
     'Name of the documents added in source. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Sean Conner', 'Supervisor: Keisha Graw',
     'Auditor: Sarah Woe', '2/5/2020', 'BD Scope', 'Note',
     "AP 10 - Please include the type of BD that were scoped for review (Medicare regular BD and/or Medicare Crossover BD).  The WP's and BD Audit Program also don’t clearly state which type of BD were scoped. If regular BD were scoped, we should request for the BD Policy for the Perm File. ",
     'AP 10 in SOI has been updated as crossover IP and crossover OP bad debts. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Darin King', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/5/2020', 'Exit ', 1.0,
     "Exit document has 12/31/16 instead of 12/31/18.    Did Provider ever reply?  Please add a note if they ever replied or not.  It's not clear if we were planning to combine the pre-exit and exit conference.  The Provider should have the right for both pre-exit and exit.  Please keep this in mind for future.  ",
     "Date has been corrected on pg 22. Provider never respond my emails and phone call so, pre-exits and exits were performed together. Will note for future Audit to performed pre-exit and exit separately. No response from provider as of today's date. XX 1/5/2035",
     'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Darin King', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/5/2020', 'IME/GME', 'Note',
     'Please make sure all the issues addressed in the JE OY 5 QASP are covered in this audit.',
     'OY-5 QASP findings appear related to resident rotations.  A PFNY has been written to review elective rotaions in 6/30/2017.  XX 1/5/2035',
     'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Darin King', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/5/2020', 'BD Audit  ', 2.0,
     'Sec 14 - BD Listings should have PBP or Prepared by Provider. ',
     'PBP added in 14-03-2a and 14-03-3a. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Darin King', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/5/2020', 'DSH Listing ', 3.0,
     '15-07-01 Source: Documents submitted by provider upon request   We should include the name of the document in the source.',
     'Name of the documents added in source. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Darin King', 'Supervisor: Karen Rodgers',
     'Auditor: Chang Lee', '3/5/2020', 'BD Scope', 'Note',
     "AP 10 - Please include the type of BD that were scoped for review (Medicare regular BD and/or Medicare Crossover BD).  The WP's and BD Audit Program also don’t clearly state which type of BD were scoped. If regular BD were scoped, we should request for the BD Policy for the Perm File. ",
     'AP 10 in SOI has been updated as crossover IP and crossover OP bad debts. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Soul Job', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/5/2020', 'Exit ', 1.0,
     "Exit document has 12/31/16 instead of 12/31/18.    Did Provider ever reply?  Please add a note if they ever replied or not.  It's not clear if we were planning to combine the pre-exit and exit conference.  The Provider should have the right for both pre-exit and exit.  Please keep this in mind for future.  ",
     "Date has been corrected on pg 22. Provider never respond my emails and phone call so, pre-exits and exits were performed together. Will note for future Audit to performed pre-exit and exit separately. No response from provider as of today's date. XX 1/5/2035",
     'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Soul Job', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/5/2020', 'IME/GME', 'Note',
     'Please make sure all the issues addressed in the JE OY 5 QASP are covered in this audit.',
     'OY-5 QASP findings appear related to resident rotations.  A PFNY has been written to review elective rotaions in 6/30/2017.  XX 1/5/2035',
     'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Soul Job', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/5/2020', 'BD Audit  ', 2.0,
     'Sec 14 - BD Listings should have PBP or Prepared by Provider. ',
     'PBP added in 14-03-2a and 14-03-3a. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Soul Job', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/5/2020', 'DSH Listing ', 3.0,
     '15-07-01 Source: Documents submitted by provider upon request   We should include the name of the document in the source.',
     'Name of the documents added in source. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Soul Job', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/5/2020', 'BD Scope', 'Note',
     "AP 10 - Please include the type of BD that were scoped for review (Medicare regular BD and/or Medicare Crossover BD).  The WP's and BD Audit Program also don’t clearly state which type of BD were scoped. If regular BD were scoped, we should request for the BD Policy for the Perm File. ",
     'AP 10 in SOI has been updated as crossover IP and crossover OP bad debts. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Johny Rocket', 'Supervisor: Abe Conner',
     'Auditor: Misha King', '5/5/2020', 'Exit ', 1.0,
     "Exit document has 12/31/16 instead of 12/31/18.    Did Provider ever reply?  Please add a note if they ever replied or not.  It's not clear if we were planning to combine the pre-exit and exit conference.  The Provider should have the right for both pre-exit and exit.  Please keep this in mind for future.  ",
     "Date has been corrected on pg 22. Provider never respond my emails and phone call so, pre-exits and exits were performed together. Will note for future Audit to performed pre-exit and exit separately. No response from provider as of today's date. XX 1/5/2035",
     'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Johny Rocket', 'Supervisor: Abe Conner',
     'Auditor: Misha King', '5/5/2020', 'IME/GME', 'Note',
     'Please make sure all the issues addressed in the JE OY 5 QASP are covered in this audit.',
     'OY-5 QASP findings appear related to resident rotations.  A PFNY has been written to review elective rotaions in 6/30/2017.  XX 1/5/2035',
     'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Johny Rocket', 'Supervisor: Abe Conner',
     'Auditor: Misha King', '5/5/2020', 'BD Audit  ', 2.0,
     'Sec 14 - BD Listings should have PBP or Prepared by Provider. ',
     'PBP added in 14-03-2a and 14-03-3a. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Johny Rocket', 'Supervisor: Abe Conner',
     'Auditor: Misha King', '5/5/2020', 'DSH Listing ', 3.0,
     '15-07-01 Source: Documents submitted by provider upon request   We should include the name of the document in the source.',
     'Name of the documents added in source. XX 1/5/2035', 'NA'],
    ['DIRECTOR REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Director: Johny Rocket', 'Supervisor: Abe Conner',
     'Auditor: Misha King', '5/5/2020', 'BD Scope', 'Note',
     "AP 10 - Please include the type of BD that were scoped for review (Medicare regular BD and/or Medicare Crossover BD).  The WP's and BD Audit Program also don’t clearly state which type of BD were scoped. If regular BD were scoped, we should request for the BD Policy for the Perm File. ",
     'AP 10 in SOI has been updated as crossover IP and crossover OP bad debts. XX 1/5/2035', 'NA'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Keisha Graw',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'L-07', 1.0,
     "In order to support that the three year review was conducted, shouldn't we be using either  STAR or prior year workpapers to document when the review was performed?  Also,  is the permanent file 3 year review checklist obsolete since we are now tracking the review in STAR? ",
     'Support added, XX, 1/6/2035', 'LDR step 7'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Keisha Graw',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'SOI', 2.0,
     'Bad debts were above scope and  required further review.  Therefore, this should have been documented on the SOI as well. ',
     'SOI updated, XX, 1/6/2035', '20.2F'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Keisha Graw',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'Sample', 3.0, 'Sample ', 'Sample', 20.3],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Keisha Graw',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'Sample', 4.0, 'Sample ', 'Sample', 20.3],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Keisha Graw',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'Sample', 5.0, 'Sample ', 'Sample', 20.3],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Keisha Graw',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'Sample', 6.0, 'Sample ', 'Sample', 20.3],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Keisha Graw',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'Sample', 7.0, 'Sample', 'Sample', 20.3],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Karen Rodgers',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'L-07', 1.0,
     "In order to support that the three year review was conducted, shouldn't we be using either  STAR or prior year workpapers to document when the review was performed?  Also,  is the permanent file 3 year review checklist obsolete since we are now tracking the review in STAR? ",
     'Support added, XX, 1/6/2035', 'LDR step 7'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Karen Rodgers',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'SOI', 2.0,
     'Bad debts were above scope and  required further review.  Therefore, this should have been documented on the SOI as well. ',
     'SOI updated, XX, 1/6/2035', '20.2F'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Karen Rodgers',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'Sample', 3.0, 'Sample ', 'Sample', '20.2F'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Karen Rodgers',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'Sample', 4.0, 'Sample ', 'Sample', '20.2F'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Karen Rodgers',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'Sample', 5.0, 'Sample ', 'Sample', '20.2F'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Karen Rodgers',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'Sample', 6.0, 'Sample ', 'Sample', '20.2F'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Karen Rodgers',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'Sample', 7.0, 'Sample', 'Sample', '20.2F'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Rob Taft',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'L-07', 1.0,
     "In order to support that the three year review was conducted, shouldn't we be using either  STAR or prior year workpapers to document when the review was performed?  Also,  is the permanent file 3 year review checklist obsolete since we are now tracking the review in STAR? ",
     'Support added, XX, 1/6/2035', 'LDR step 7'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Rob Taft',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'SOI', 2.0,
     'Bad debts were above scope and  required further review.  Therefore, this should have been documented on the SOI as well. ',
     'SOI updated, XX, 1/6/2035', '20.2F'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Rob Taft',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'Sample', 3.0, 'Sample ', 'Sample', 70.4],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Rob Taft',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'Sample', 4.0, 'Sample ', 'Sample', 70.4],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Rob Taft',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'Sample', 5.0, 'Sample ', 'Sample', 70.4],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Rob Taft',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'Sample', 6.0, 'Sample ', 'Sample', 70.4],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Rob Taft',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'Sample', 7.0, 'Sample', 'Sample', 70.4],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Abe Conner',
     'Supervisor: Rob Taft', 'Auditor: John Dew', '4/6/2020', 'L-07', 1.0,
     "In order to support that the three year review was conducted, shouldn't we be using either  STAR or prior year workpapers to document when the review was performed?  Also,  is the permanent file 3 year review checklist obsolete since we are now tracking the review in STAR? ",
     'Support added, XX, 1/6/2035', 'LDR step 7'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Abe Conner',
     'Supervisor: Rob Taft', 'Auditor: John Dew', '4/6/2020', 'SOI', 2.0,
     'Bad debts were above scope and  required further review.  Therefore, this should have been documented on the SOI as well. ',
     'SOI updated, XX, 1/6/2035', '20.2F'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Abe Conner',
     'Supervisor: Rob Taft', 'Auditor: John Dew', '4/6/2020', 'Sample', 3.0, 'Sample ', 'Sample', 'LDR step 7'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Abe Conner',
     'Supervisor: Rob Taft', 'Auditor: John Dew', '4/6/2020', 'Sample', 4.0, 'Sample ', 'Sample', 'LDR step 7'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Abe Conner',
     'Supervisor: Rob Taft', 'Auditor: John Dew', '4/6/2020', 'Sample', 5.0, 'Sample ', 'Sample', 'LDR step 7'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Abe Conner',
     'Supervisor: Rob Taft', 'Auditor: John Dew', '4/6/2020', 'Sample', 6.0, 'Sample ', 'Sample', 'LDR step 7'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Abe Conner',
     'Supervisor: Rob Taft', 'Auditor: John Dew', '4/6/2020', 'Sample', 7.0, 'Sample', 'Sample', 'LDR step 7'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Jared Noun',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'L-07', 1.0,
     "In order to support that the three year review was conducted, shouldn't we be using either  STAR or prior year workpapers to document when the review was performed?  Also,  is the permanent file 3 year review checklist obsolete since we are now tracking the review in STAR? ",
     'Support added, XX, 1/6/2035', 'LDR step 7'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Jared Noun',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'SOI', 2.0,
     'Bad debts were above scope and  required further review.  Therefore, this should have been documented on the SOI as well. ',
     'SOI updated, XX, 1/6/2035', '20.2F'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Jared Noun',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 3.0, 'Sample ', 'Sample', 'LDR step 6'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Jared Noun',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 4.0, 'Sample ', 'Sample', 'LDR step 6'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Jared Noun',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 5.0, 'Sample ', 'Sample', 'LDR step 6'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Jared Noun',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 6.0, 'Sample ', 'Sample', 'LDR step 6'],
    ['Inter-office file review', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Supervisor: Jared Noun',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 7.0, 'Sample', 'Sample', 'LDR step 6'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', '', 'N/A',
     'Provider exceeded thresholds for Bad Debts. Other areas will be reviewed at reviewers discretion. ', 'N/A',
     'N/A'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'Accept. Tab', 1.0,
     'Auditor and Audit Supervisor need to initial & date the Prepared By and Reviewed By columns.', '', '60.8C2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'L-A2', 2.0,
     'The following review points are applicable to review of the PY adjustment report:                          a) REF#44 (p.7) - Tickmark required.            ',
     '', '60.8C9'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'L-D1', 3.0,
     'Above the Purpose is a red highlighted, "Review   Required". These highlighted areas are to be  removed when the WPs are completed. ',
     '', 'N/A'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', '12-1B-1, 12-2-1', 4.0,
     'Per the testing of the N&AHE Pastoral Care  Program, the provider submitted supporting  documents from pgs. 2 through 231. The  supporting documents from the provider or  consultant should have a designation of  Provided-By-Provider or PBP or something similar  similar to distinguish that the support was  received from another party.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', '12-6-1, L-F1, L-G1-2', 5.0,
     'There is a proposed adjustment on the page.  Auditors tickmark has been added to show that  the auditor traced the adjustment from the WPs  to the adj. report, but audit supervisor is  required to place a tickmark by the adjustment  to verify that the supervisor has trraced the  adustments from the WPs to the adj. report also.  Insert supervisor tickmark.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'L-G1-2', 6.0,
     'Per Summary of All BDs tab, the O/P Dialysis  Traditional BDs show a beginning balance,  adjustment, and ending balance of $53,000,   ($4,223), and $48,776. Per the adjustment  report, the amounts are reported as $60,646,  ($4,223), and $56,423. Reconcile the amounts  and make appropriate changes.  ',
     '', '60.8C11'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', '15-7A-01', 7.0,
     'Tickmark A denotes that the error rate is below 30%, therefore only the errors found will be removed from Medicaid days. The tickmark should state the error rate is below the anticipated error rate of 6%, therefore only the errors found will be removed from Medicaid days. Change tickmark explanation.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'Sample', 8.0, 'Sample', '', '60.8C5'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'Sample', 9.0, 'Sample', '', '60.8C5'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'Sample', 10.0, 'Sample', '', '60.8C5'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'Sample', 11.0, 'Sample', '', '60.8C5'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alice Song',
     'Supervisor: Jared Noun', 'Auditor: Bob Low', '1/6/2020', 'Sample', 12.0, 'Sample', '', '60.8C5'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', '', 'N/A',
     'Provider exceeded thresholds for Bad Debts. Other areas will be reviewed at reviewers discretion. ', 'N/A',
     'N/A'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'Accept. Tab', 1.0,
     'Auditor and Audit Supervisor need to initial & date the Prepared By and Reviewed By columns.', '', '60.8C2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'L-A2', 2.0,
     'The following review points are applicable to review of the PY adjustment report:                          a) REF#44 (p.7) - Tickmark required.            ',
     '', '60.8C9'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'L-D1', 3.0,
     'Above the Purpose is a red highlighted, "Review   Required". These highlighted areas are to be  removed when the WPs are completed. ',
     '', 'N/A'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', '12-1B-1, 12-2-1', 4.0,
     'Per the testing of the N&AHE Pastoral Care  Program, the provider submitted supporting  documents from pgs. 2 through 231. The  supporting documents from the provider or  consultant should have a designation of  Provided-By-Provider or PBP or something similar  similar to distinguish that the support was  received from another party.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', '12-6-1, L-F1, L-G1-2', 5.0,
     'There is a proposed adjustment on the page.  Auditors tickmark has been added to show that  the auditor traced the adjustment from the WPs  to the adj. report, but audit supervisor is  required to place a tickmark by the adjustment  to verify that the supervisor has trraced the  adustments from the WPs to the adj. report also.  Insert supervisor tickmark.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'L-G1-2', 6.0,
     'Per Summary of All BDs tab, the O/P Dialysis  Traditional BDs show a beginning balance,  adjustment, and ending balance of $53,000,   ($4,223), and $48,776. Per the adjustment  report, the amounts are reported as $60,646,  ($4,223), and $56,423. Reconcile the amounts  and make appropriate changes.  ',
     '', '60.8C11'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', '15-7A-01', 7.0,
     'Tickmark A denotes that the error rate is below 30%, therefore only the errors found will be removed from Medicaid days. The tickmark should state the error rate is below the anticipated error rate of 6%, therefore only the errors found will be removed from Medicaid days. Change tickmark explanation.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'Sample', 8.0, 'Sample', '', '60.8C10'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'Sample', 9.0, 'Sample', '', '60.8C10'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'Sample', 10.0, 'Sample', '', '60.8C10'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'Sample', 11.0, 'Sample', '', '60.8C10'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miranda Gan',
     'Supervisor: Keisha Graw', 'Auditor: Sarah Woe', '2/6/2020', 'Sample', 12.0, 'Sample', '', '60.8C10'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', '', 'N/A',
     'Provider exceeded thresholds for Bad Debts. Other areas will be reviewed at reviewers discretion. ', 'N/A',
     'N/A'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'Accept. Tab', 1.0,
     'Auditor and Audit Supervisor need to initial & date the Prepared By and Reviewed By columns.', '', '60.8C2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'L-A2', 2.0,
     'The following review points are applicable to review of the PY adjustment report:                          a) REF#44 (p.7) - Tickmark required.            ',
     '', '60.8C9'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'L-D1', 3.0,
     'Above the Purpose is a red highlighted, "Review   Required". These highlighted areas are to be  removed when the WPs are completed. ',
     '', 'N/A'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', '12-1B-1, 12-2-1', 4.0,
     'Per the testing of the N&AHE Pastoral Care  Program, the provider submitted supporting  documents from pgs. 2 through 231. The  supporting documents from the provider or  consultant should have a designation of  Provided-By-Provider or PBP or something similar  similar to distinguish that the support was  received from another party.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', '12-6-1, L-F1, L-G1-2', 5.0,
     'There is a proposed adjustment on the page.  Auditors tickmark has been added to show that  the auditor traced the adjustment from the WPs  to the adj. report, but audit supervisor is  required to place a tickmark by the adjustment  to verify that the supervisor has trraced the  adustments from the WPs to the adj. report also.  Insert supervisor tickmark.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'L-G1-2', 6.0,
     'Per Summary of All BDs tab, the O/P Dialysis  Traditional BDs show a beginning balance,  adjustment, and ending balance of $53,000,   ($4,223), and $48,776. Per the adjustment  report, the amounts are reported as $60,646,  ($4,223), and $56,423. Reconcile the amounts  and make appropriate changes.  ',
     '', '60.8C11'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', '15-7A-01', 7.0,
     'Tickmark A denotes that the error rate is below 30%, therefore only the errors found will be removed from Medicaid days. The tickmark should state the error rate is below the anticipated error rate of 6%, therefore only the errors found will be removed from Medicaid days. Change tickmark explanation.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'Sample', 8.0, 'Sample', '', '60.8C4'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'Sample', 9.0, 'Sample', '', '60.8C4'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'Sample', 10.0, 'Sample', '', '60.8C4'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'Sample', 11.0, 'Sample', '', '60.8C4'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Alex Smart',
     'Supervisor: Karen Rodgers', 'Auditor: Chang Lee', '3/6/2020', 'Sample', 12.0, 'Sample', '', '60.8C4'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', '', 'N/A',
     'Provider exceeded thresholds for Bad Debts. Other areas will be reviewed at reviewers discretion. ', 'N/A',
     'N/A'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', 'Accept. Tab', 1.0,
     'Auditor and Audit Supervisor need to initial & date the Prepared By and Reviewed By columns.', '', '60.8C2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', 'L-A2', 2.0,
     'The following review points are applicable to review of the PY adjustment report:                          a) REF#44 (p.7) - Tickmark required.            ',
     '', '60.8C9'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', 'L-D1', 3.0,
     'Above the Purpose is a red highlighted, "Review   Required". These highlighted areas are to be  removed when the WPs are completed. ',
     '', 'N/A'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', '12-1B-1, 12-2-1', 4.0,
     'Per the testing of the N&AHE Pastoral Care  Program, the provider submitted supporting  documents from pgs. 2 through 231. The  supporting documents from the provider or  consultant should have a designation of  Provided-By-Provider or PBP or something similar  similar to distinguish that the support was  received from another party.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', '12-6-1, L-F1, L-G1-2', 5.0,
     'There is a proposed adjustment on the page.  Auditors tickmark has been added to show that  the auditor traced the adjustment from the WPs  to the adj. report, but audit supervisor is  required to place a tickmark by the adjustment  to verify that the supervisor has trraced the  adustments from the WPs to the adj. report also.  Insert supervisor tickmark.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', 'L-G1-2', 6.0,
     'Per Summary of All BDs tab, the O/P Dialysis  Traditional BDs show a beginning balance,  adjustment, and ending balance of $53,000,   ($4,223), and $48,776. Per the adjustment  report, the amounts are reported as $60,646,  ($4,223), and $56,423. Reconcile the amounts  and make appropriate changes.  ',
     '', '60.8C11'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', '15-7A-01', 7.0,
     'Tickmark A denotes that the error rate is below 30%, therefore only the errors found will be removed from Medicaid days. The tickmark should state the error rate is below the anticipated error rate of 6%, therefore only the errors found will be removed from Medicaid days. Change tickmark explanation.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', 'Sample', 8.0, 'Sample', '', '60.8C17'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', 'Sample', 9.0, 'Sample', '', '60.8C17'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', 'Sample', 10.0, 'Sample', '', '60.8C17'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', 'Sample', 11.0, 'Sample', '', '60.8C17'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Miah Lofs', 'Supervisor: Rob Taft',
     'Auditor: John Dew', '4/6/2020', 'Sample', 12.0, 'Sample', '', '60.8C17'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', '', 'N/A',
     'Provider exceeded thresholds for Bad Debts. Other areas will be reviewed at reviewers discretion. ', 'N/A',
     'N/A'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Accept. Tab', 1.0,
     'Auditor and Audit Supervisor need to initial & date the Prepared By and Reviewed By columns.', '', '60.8C2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'L-A2', 2.0,
     'The following review points are applicable to review of the PY adjustment report:                          a) REF#44 (p.7) - Tickmark required.            ',
     '', '60.8C9'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'L-D1', 3.0,
     'Above the Purpose is a red highlighted, "Review   Required". These highlighted areas are to be  removed when the WPs are completed. ',
     '', 'N/A'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', '12-1B-1, 12-2-1', 4.0,
     'Per the testing of the N&AHE Pastoral Care  Program, the provider submitted supporting  documents from pgs. 2 through 231. The  supporting documents from the provider or  consultant should have a designation of  Provided-By-Provider or PBP or something similar  similar to distinguish that the support was  received from another party.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', '12-6-1, L-F1, L-G1-2', 5.0,
     'There is a proposed adjustment on the page.  Auditors tickmark has been added to show that  the auditor traced the adjustment from the WPs  to the adj. report, but audit supervisor is  required to place a tickmark by the adjustment  to verify that the supervisor has trraced the  adustments from the WPs to the adj. report also.  Insert supervisor tickmark.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'L-G1-2', 6.0,
     'Per Summary of All BDs tab, the O/P Dialysis  Traditional BDs show a beginning balance,  adjustment, and ending balance of $53,000,   ($4,223), and $48,776. Per the adjustment  report, the amounts are reported as $60,646,  ($4,223), and $56,423. Reconcile the amounts  and make appropriate changes.  ',
     '', '60.8C11'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', '15-7A-01', 7.0,
     'Tickmark A denotes that the error rate is below 30%, therefore only the errors found will be removed from Medicaid days. The tickmark should state the error rate is below the anticipated error rate of 6%, therefore only the errors found will be removed from Medicaid days. Change tickmark explanation.',
     '', 'See R-2'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 8.0, 'Sample', '', '60.8C1'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 9.0, 'Sample', '', '60.8C1'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 10.0, 'Sample', '', '60.8C1'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 11.0, 'Sample', '', '60.8C1'],
    ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann',
     'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 12.0, 'Sample', '', '60.8C1']]


# ERROR FORMAT
# [0] REVIEW TYPE, [1] PROVIDER NAME, [2] PROVIDER #, [3] FISCAL YEAR END, [4] 2ND LEVEL REVIEWER, [5] SUPERVISOR, [6] AUDITOR, [7] DATE REVIEWED, [8] WKPR REF, [9] POINT #, [10] REVIEW POINT, [11] DISPOSITION, INITIALS, DATE, [12] UDR/EXHIBIT STEP/IOM CHAP 8 REF
# ['QUALITY REVIEW', 'ABC Hospital', 'XX-XXXX', '12/31/2033', 'Quality Reviewer: Carrie Ann', 'Supervisor: Abe Conner', 'Auditor: Misha King', '5/6/2020', 'Sample', 12.0, 'Sample', '', '60.8C1']

# Method to return top 5 errors in database
def get_top_five_errors(a, **kwargs):
    error_types = []
    for x in a:
        if x[0] == kwargs.get("review_level"):
            error_types.append(x[12])
        elif (x[12] != "NA" and x[12] != "n/a" and x[12] != "") and kwargs.get("review_level") is None:
            error_types.append(x[12])

    # Gets an array of top 5 errors with error type and frequency
    # It's an array of arrays
    # [("string", int), ("string", int), ("string", int), ("string", int), ("string", int)]
    # You need to import Counter class
    net = Counter(error_types).most_common(5)

    # Creates string that can display top five errors
    # top_five = net[0][0] + ": " + str(net[0][1]) + "\n" + net[1][0] + ": " + str(net[1][1]) + "\n" + net[2][0] + ": " + str(net[2][1]) + "\n" + net[3][0] + ": " + str(net[3][1]) + "\n" + net[4][0] + ": " + str(net[4][1]) + "\n"

    # To return the top five errors in their array form, return net
    return net
    # return top_five


# TEST AND OUTPUT FOR get_top_five_errors
#test = get_top_five_errors(errors, "SUPERVISOR REVIEW")
#print("Top five errors UDR/Exhibit Step/IOM Chap 8 Ref overall:")
#print(test)

print("\n\n")

# Returns top 5 errors from desk reviews (supervisor reviewing auditor)
def get_top_five_supervisor_errors(a):
    supervisor_errors = []
    for x in a:
        if x[0] == 'SUPERVISORY REVIEW':
            supervisor_errors.append(x)

    return get_top_five_errors(supervisor_errors, review_level="SUPERVISOR REVIEW")


# OUTPUT for get_top_five_supervisor_errors
test2 = get_top_five_supervisor_errors(errors)
print("Top five desk review UDR/Exhibit Step/IOM Chap 8 Ref errors:")
print(test2)

print("\n\n")

# Returns top 5 errors from manager (manager reviewing supervisor who reviewed auditor)
def get_top_five_manager_errors(a):
    manager_errors = []
    for x in a:
        if x[0] == 'MANAGER REVIEW':
            manager_errors.append(x)

    return get_top_five_errors(manager_errors, review_level="MANAGER REVIEW")


# OUTPUT for get_top_five_manager_errors
test3 = get_top_five_manager_errors(errors)
print("Top five manager review UDR/Exhibit Step/IOM Chap 8 Ref errors:")
print(test3)

print("\n\n")

# Returns top 5 errors from director (director reviewing supervisor who reviewed auditor)
def get_top_five_director_errors(a):
    director_errors = []
    for x in a:
        if x[0] == 'DIRECTOR REVIEW':
            director_errors.append(x)

    return get_top_five_errors(director_errors, review_level="DIRECTOR REVIEW")


# OUTPUT for get_top_five_supervisor_errors
test4 = get_top_five_director_errors(errors)
print("Top five director review UDR/Exhibit Step/IOM Chap 8 Ref errors:")
print(test4)

print("\n\n")

# Returns top five errors from quality reviews
def get_top_five_quality_errors(a):
    quality_reviewers = []
    for x in a:
        if x[0] == 'QUALITY REVIEW':
            quality_reviewers.append(x)

    return get_top_five_errors(quality_reviewers, review_level='QUALITY REVIEW')

# TEST get_top_five_quality_errors
print("Test for get_top_five_quality_errors")
quality_test = get_top_five_quality_errors(errors)
print(quality_test)

print("\n\n")

# Returns top five errors from interoffice reviews
def get_top_five_interoffice_errors(a):
    interoffice_errors = []
    for x in a:
        if x[0] == 'Inter-office file review':
            interoffice_errors.append(x)

    return get_top_five_errors(interoffice_errors, review_level='Inter-office file review')

# TEST get_top_five_interoffice_errors
print("Test for get_top_five_interoffice_errors")
interoffice_test = get_top_five_interoffice_errors(errors)
print(interoffice_test)

print("\n\n")

# This returns the top 5 reviewers overall based on review points given
# The argument is the array of errors (a) and
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
    #top_five = net[0][0] + ": " + str(net[0][1]) + "\n" + net[1][0] + ": " + str(net[1][1]) + "\n" + net[2][0] + ": " + str(net[2][1]) + "\n" + net[3][0] + ": " + str(net[3][1]) + "\n" + net[4][0] + ": " + str(net[4][1]) + "\n"
    #return top_five
    return net

# OUTPUT for get_top_5_reviewers
print("Test for get_top_five_reviewers")
test5 = get_top_five_reviewers(errors)
print(test5)

print("\n\n")

# This returns top 5 reviewers based on review type
def get_top_five_reviewers_by_type(a, r_type):
    reviewers = []
    for x in a:
        if r_type == "SUPERVISORY REVIEW":
            reviewers.append(x[5])
        if r_type == "DIRECTOR REVIEW":
            reviewers.append(x[4])
        if r_type == "MANAGER REVIEW":
            reviewers.append(x[4])
        if r_type == "QUALITY REVIEW":
            reviewers.append(x[4])
        if r_type == "Inter-office file review":
            reviewers.append(x[4])
    net = Counter(reviewers).most_common(5)
    # top_five = net[0][0] + ": " + str(net[0][1]) + "\n" + net[1][0] + ": " + str(net[1][1]) + "\n" + net[2][0] + ": " + str(net[2][1]) + "\n" + net[3][0] + ": " + str(net[3][1]) + "\n" + net[4][0] + ": " + str(net[4][1]) + "\n"
    # return top_five
    return net

# OUTPUT for get_top_five_reviewers_by_type
print("Test for get_top_five_reviewers_by_type using MANAGER REVIEW")
test6 = get_top_five_reviewers_by_type(errors, "MANAGER REVIEW")
print(test6)

print("\n\n")


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
print("Test for get_errors_by_error_type using error 60.8C2")
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
t4 = get_errors_by_review_type(errors, "SUPERVISORY REVIEW")
for x in t4:
    print(x)

print("\n\n")

# This returns errors based on any attributes you enter
def get_errors_by_all_attributes(a, review_type, name, error_type, d1, d2):
    all_errors = a
    if review_type != "":
        all_errors = get_errors_by_review_type(all_errors, review_type)
    if name != "":
        all_errors = get_errors_by_name(all_errors, name)
    if error_type != "":
        all_errors = get_errors_by_error_type(all_errors, error_type)
    if d1 != "" and d2 != "":
        all_errors = get_errors_by_review_date(all_errors, d1, d2)
    return all_errors

# TEST get_errors_by_all_attributes
# This returns errors arrays for Sisa Smith a manager between 1/1/2020 and 3/30/20
print("Test for getting errors by all relevant attributes")
t5 = get_errors_by_all_attributes(errors, "", "Sisa Smith", "", datetime.datetime(2020, 1, 1), datetime.datetime(2020, 3, 30))
for x in t5:
    print(x)

print("\n\n")


# Sort the object by their date. This method will be particularly useful for the line graph
def sort_by_date(data):
    return sorted(data, key=lambda error: error[7], reverse=False)


print(sort_by_date(errors))
