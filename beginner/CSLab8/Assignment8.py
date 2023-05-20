"""
Assignment 8: Linguistic Analysis

Author: Alex Yazdani
CWID: 20399751
Date: 11/18/2022

This file imports the function find_file from "Assignment 7: File Processing".
The file prompts the user for a file to open, verifies it exists, then opens and reads the file once.
It then creates a dict with A-Z setting each key's value to 0.
This file counts each alphabetic letter in the user's file as a total.
It then iterates through each character in the datafile, checks if it is alphabetic, and then increments the value of that letter in the dict.
Finally, the file converts each value in the dict to a whole number percentage, or frequency.
The dict is then printed
"""

from Assignment7 import find_file

def main():
    """
    Verifies the file exists and pulls the filename from the user.
    Opens and reads the file.
    Creates a dict with A-Z.
    Counts how many occurances of each letter are in the file.
    Represents the frequency of each letter in the file as a percentage in the dict.
    """
    data_filename = find_file()
    data_file = open(data_filename, "r")
    raw_data = (data_file.read()).upper()

    letter_count = 0
    for char in raw_data:
        if char.isalpha():
            letter_count += 1

    letter_freq = {}

    for letter in range(65,91):
        letter_freq[chr(letter)] = 0

    for char in raw_data:
        if char in letter_freq:
            letter_freq[char] += 1
            
    for akey in letter_freq:
        letter_freq[akey] /= (letter_count/100)
        letter_freq[akey] = f"{round(letter_freq[akey])}%"
    print("\nThe following are the frequencies of each letter in your file:\n")
    print("Letter:      Frequency:\n")
    for k,v in sorted(letter_freq.items()):
        print("  ",k,"          ",v,)
    print()

if __name__ == "__main__":
    main()


r"""
What is the name of the file you would like to process?  x
That is not a valid filename, please try again.

What is the name of the file you would like to process?  testfilelab8.txt

The following are the frequencies of each letter in your file:

Letter:      Frequency:

   A            7%
   B            3%
   C            3%
   D            1%
   E            12%
   F            4%
   G            2%
   H            7%
   I            8%
   J            1%
   K            1%
   L            5%
   M            2%
   N            5%
   O            8%
   P            0%
   Q            0%
   R            4%
   S            8%
   T            13%
   U            3%
   V            0%
   W            2%
   X            0%
   Y            2%
   Z            1%

PS C:\Users\ayazdani\PythonProjects\CSLab8> 
"""