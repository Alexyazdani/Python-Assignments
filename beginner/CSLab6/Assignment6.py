"""
Assignment 6: A List API

Author: Alex Yazdani
CWID: 20399751
Date: 11/9/2022

This file is an API consisting of 5 functions for handling lists (assuming elements of int type).
The first function, swap_first_and_last() will swap the first and last element, and returns nothing.
shift_right() will shift all elements to the right by one index, and loop the final element to the front.  It returns nothing.
double() will modify the list by multiplying all elements by 2, and returns nothing.
is_sorted will check if the input list is sorted by ascending numerical order, returning true if so and false if not.
replace_evens() will modify the list by replacing all even numbers with 0, returning nothing.
The main() function acts as a test program to validate the design of each function.
"""

def swap_first_and_last(my_list):
    """
    swap_first_and_last() accepts any list of int type as paramenter and swaps the first and last elements.
    Returns nothing.
    """
    first_element = my_list[0]
    last_element = my_list[len(my_list) - 1]
    my_list[0] = last_element
    my_list[len(my_list) - 1] = first_element

def shift_right(my_list):
    """
    shift_right() accepts any list of int type as paramenter and shifts all elements to the right by one index.
    The last element is moved to the front.
    Returns nothing.
    """
    my_list.insert(0, my_list[len(my_list) - 1])
    del my_list[len(my_list) - 1]

def double(my_list):
    """
    double() accepts any list of int type as paramenter and doubles each element.
    Returns nothing.
    """
    for i in range(len(my_list)):
        my_list[i] = my_list[i]*2

def is_sorted(my_list):
    """
    is_sorted() accepts any list of int type as paramenter.  If the list is sorted in ascending numerical order, function returns true.  If not, returns false
    """
    sorted_list = my_list.copy()
    sorted_list.sort()
    if my_list == sorted_list:
        return True
    else:
        return False

def replace_evens(my_list):
    """
    replace_evens() accepts any list of int type as paramenter and replaces all even values with 0.
    Returns nothing.
    """
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            my_list[i] = 0


def main():
    """
    Test program for the list API
    """
    # tests swap_first_and_last()
    print("")
    print("RUN for: swap_first_and_last(my_list)")
    my_list = [1,4,2,9]
    print (my_list)
    swap_first_and_last(my_list)
    print(my_list)

    # tests shift_right()
    print("")
    print("RUN for: shift_right(my_list)")
    my_list = [1,4,2,9]
    print(my_list)
    shift_right(my_list)
    print(my_list)

    # tests double()
    print("")
    print("RUN for: double(my_list)")
    my_list = [1,4,2,9]
    print(my_list)
    double(my_list)
    print(my_list)

    # tests is_sorted()
    print("")
    print("RUN for: is_sorted(my_list)")
    my_list = [1,4,2,9]
    if is_sorted(my_list):
        print("my_list is sorted")
    else:
        print("my_list is not sorted")
    print("")
    print("RUN for: is_sorted(my_other_list)")
    my_other_list = [1,2,4,9]
    if is_sorted(my_other_list):
        print("my_other_list is sorted")
    else:
        print("my_other_list is not sorted")

    # tests replace_evens()
    print("")
    print("RUN for: replace_evens(my_list)")
    my_list = [1,4,2,9]
    print(my_list)
    replace_evens(my_list)
    print(my_list)

if __name__ == "__main__":
    main()

r"""PS C:\Users\ayazdani\PythonProjects\CSLab6>  c:; cd 'c:\Users\ayazdani\PythonProjects\CSLab6'; & 'C:\Users\ayazdani\AppData\Local\Programs\Python\Python310\python.exe' 'c:\Users\ayazdani\.vscode\extensions\ms-python.python-2022.16.1\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher' '54821' '--' 'c:\Users\ayazdani\PythonProjects\CSLab6\Assignment6.py' 

RUN for: swap_first_and_last(my_list)
[1, 4, 2, 9]
[9, 4, 2, 1]

RUN for: shift_right(my_list)
[1, 4, 2, 9]
[9, 1, 4, 2]

RUN for: double(my_list)
[1, 4, 2, 9]
[2, 8, 4, 18]

RUN for: is_sorted(my_list)
my_list is not sorted

RUN for: is_sorted(my_other_list)
my_other_list is sorted

RUN for: replace_evens(my_list)
[1, 4, 2, 9]
[1, 0, 0, 9]
"""