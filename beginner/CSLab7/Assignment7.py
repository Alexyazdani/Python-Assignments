"""
Assignment 7: File Processing

Author: Alex Yazdani
CWID: 20399751
Date: 11/17/2022 (resubmitted 12/6/2022)

This file prompts the user for a file, responding with an error message if the file does not exist, and prompting the user again.
Once a valid filename is provided, the main() function opens and reads the file, the responds with the number of characters, words, and lines.
The file is then closed.
"""


def find_file():
    """
    Asks user for a file to check if it exists, returns filename if it does.
    If it does not, an error message is displayed and the user is prompted again for input.
    """
    while True:
        file_name = input("What is the name of the file you would like to process?  ")
        try:
            test_file = open(file_name, "r")
            return file_name
        except:
            print("That is not a valid filename, please try again.\n")


def main():
    """
    Uses find_function() to ask the user for a file input and check if it exists.
    If it does not, it will give an error message and ask again.
    If user provides valid file, file is opened and read.
    Prints the number of characters, words, and lines in the file.
    """
    data_filename = find_file()
    data_file = open(data_filename, "r")
    raw_data = data_file.read()
    char_count = len(raw_data)
    word_count = len(raw_data.split())
    line_count = len(raw_data.split("\n"))
    data_file.close()
    print()
    print(raw_data)
    print(f"\nNumber of characters:    {char_count}")
    print(f"Number of words:         {word_count}")
    print(f"Number of lines:         {line_count}\n")



if __name__ == "__main__":
    main()


r"""
PS C:\Users\ayazdani\PythonProjects\CSLab7>  c:; cd 'c:\Users\ayazdani\PythonProjects\CSLab7'; & 'C:\Users\ayazdani\AppData\Local\Programs\Python\Python310\python.exe' 'c:\Users\ayazdani\.vscode\extensions\ms-python.python-2022.18.2\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher' '59198' '--' 'c:\Users\ayazdani\PythonProjects\CSLab7\Assignment7.py'
What is the name of the file you would like to process?  x
That is not a valid filename, please try again.

What is the name of the file you would like to process?  y
That is not a valid filename, please try again.

What is the name of the file you would like to process?  z
That is not a valid filename, please try again.

What is the name of the file you would like to process?  testfile.txt

This is the test file for Lab 7: File Processing
These are the opening lines to "Like a Rolling Stone" by Bob Dylan:
Once upon a time you dressed so fine
Threw the bums a dime in your prime, didn't you?
People call, say, "Beware doll you're bound to fall"
You thought they were all kiddin' you

Number of characters:    293
Number of words:         57
Number of lines:         6

PS C:\Users\ayazdani\PythonProjects\CSLab7> 
"""









# def main():
#     """
#     Original test program for find_file()
#     """
#     data_filename = find_file()
#     data_file = open(data_filename, "r")
#     print()
#     for line in data_file:
#         print(line, end ="")

