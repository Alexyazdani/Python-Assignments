"""
Lab 5: Regex (Test Module)
Alexander Yazdani
CWID: 20399751
Date: 03/16/2023

This file acts as a test driver for the date_conversion() function defined in the YazdaniAlexandera5.py file.
The program loops through the function 5 times.
The first 3 user inputs are random, valid inputs.
The 4th input demonstrates the functionality of leap year recognition.
The 5th input is invalid, triggering SystemExit to be raised.
The test run can be seen at the end of the file.
"""
from YazdaniAlexandera5 import date_conversion
NUM_DATES = 5


def main():
    for date in range(NUM_DATES):
        print()
        converted_date = date_conversion()
        print(f"The converted date is: {converted_date}")

if __name__ == "__main__":    
    main()

r"""

Enter a date (mm/dd/yyyy):  03/16/2023
The converted date is: March 16, 2023

Enter a date (mm/dd/yyyy):  01/24/1956
The converted date is: January 24, 1956

Enter a date (mm/dd/yyyy):  08/28/1998
The converted date is: August 28, 1998

Enter a date (mm/dd/yyyy):  02/29/2020
The converted date is: February 29, 2020

Enter a date (mm/dd/yyyy):  13/01/2000
C:\Users\ayazdani\PythonProjects\intermediate\lab5-Regex>
"""