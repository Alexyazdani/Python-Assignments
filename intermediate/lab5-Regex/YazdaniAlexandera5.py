"""
Lab 5: Regex
Alexander Yazdani
CWID: 20399751
Date: 03/16/2023

This module creates a function called date_conversion() which prompts the user to input a date in a specific format (mm/dd/yyyy).
The module uses the re library to pull out this format from the input string.
The month, day and year are extracted and the input is validated.
Invalid inputs will result in SystemExit being raised.
The newly formatted date will be output if the input is valid.
"""


import re
MONTH_LIST = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
NUM_DIGITS_MONTH = 2
NUM_DIGITS_DAY = 2
NUM_DIGITS_YEAR = 4
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MIN_YEAR = 1000
MAX_YEAR = 2999


def date_conversion():
    """
    This function prompts the user for a date.
    The month, day, and year are placed into a list as strings, and later set as variable.
    The initial input is validated to make sure that the pattern (mm/dd/yyyy) is found, using the re module
    Next, it is verified that each number has the correct amount of digits, and are with an acceptable range.
    The month is found from a list of months using the number to help index
    Finally, the program checks if it is a leap year, and will raise an exception if February 29th is entered in with a common year.
    """
    MONTH_DICT = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
    date_from_user = input("Enter a date (mm/dd/yyyy):  ")
    date_string = re.findall(r'\d{1,2}\/\d{1,2}\/\d{1,4}', date_from_user)
    if len(date_string) == 0:
        raise SystemExit
    date_list = date_string[0].split("/")
    if (len(date_list) != 3):
        raise SystemExit
    if (len(date_list[0]) != NUM_DIGITS_MONTH) or (len(date_list[1]) != NUM_DIGITS_DAY) or (len(date_list[2]) != NUM_DIGITS_YEAR):
        raise SystemExit
    if (int(date_list[0]) < MIN_MONTH) or (int(date_list[0]) > MAX_MONTH):
        raise SystemExit
    month = MONTH_LIST[int(date_list[0]) - 1]
    day = date_list[1]
    year = date_list[2]
    if (int(year) < MIN_YEAR) or (int(year) > MAX_YEAR):
        raise SystemExit
    if int(date_list[2])%4 == 0:
        MONTH_DICT['February'] = 29
    if (int(day) < MIN_DAY) or (int(day) > MONTH_DICT[month]):
        raise SystemExit
    return f"{month} {day}, {year}"