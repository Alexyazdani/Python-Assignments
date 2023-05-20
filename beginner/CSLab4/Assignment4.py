"""
Assignment 4: Processing Data

Author: Alex Yazdani
CWID: 20399751
Date: 10/17/2022

This program prompts the user for integer numbers and reads in these numbers for as long as the user wishes.
The program then outputs the total sum of the list, the max and min values, the number of even values, the number of add values, and the average value.
"""

evencnt = 0
oddcnt = 0
totalcount = 1

print("This program will calculate statistics for your integer data")
firstval = int(input("Please type a number: "))
if firstval % 2 == 0:
    if firstval != 0:
        evencnt = 1
else:
    oddcnt = 1
minval = firstval
maxval = firstval
total = firstval
cont = input("Do you have another number to enter? ")
# The first number is taken before the loop to initialize min/max values

while cont == "Y" or cont == "y" or cont == "YES" or cont == "Yes" or cont == "yes":
    totalcount = totalcount + 1
    numb = int(input("Please type a number: "))
    total = total + numb
    if numb > maxval:
        maxval = numb
    if numb < minval:
        minval = numb
    if numb % 2 == 0:
        if numb != 0:
            evencnt = evencnt + 1
    else:
        oddcnt = oddcnt + 1
    cont = input("Do you have another number to enter? ")
averageval = total/totalcount

print("")
print(f"The total of your numbers is: {total}")
print(f"The smallest of your numbers is: {minval}")
print(f"The largest of your numbers is: {maxval}")
print(f"The number of even numbers is:  {evencnt}")
print(f"The number of odd numbers is:  {oddcnt}")
print(f"The average of you numbers is:  {averageval:.1f}")

r"""
C:\Users\ayazdani\AppData\Local\Programs\Python\Python310\python.exe C:\Users\ayazdani\PycharmProjects\CSLab4\Assignment4.py 
This program will calculate statistics for your integer data
Please type a number: 7
Do you have another number to enter? Y
Please type a number: -13
Do you have another number to enter? Y
Please type a number: -3
Do you have another number to enter? Y
Please type a number: 99
Do you have another number to enter? N

The total of your numbers is: 90
The smallest of your numbers is: -13
The largest of your numbers is: 99
The number of even numbers is:  0
The number of odd numbers is:  4
The average of you numbers is:  22.5

Process finished with exit code 0


C:\Users\ayazdani\AppData\Local\Programs\Python\Python310\python.exe C:\Users\ayazdani\PycharmProjects\CSLab4\Assignment4.py 
This program will calculate statistics for your integer data
Please type a number: 7
Do you have another number to enter? Y
Please type a number: -14
Do you have another number to enter? Y
Please type a number: 100
Do you have another number to enter? Y
Please type a number: -18
Do you have another number to enter? Y
Please type a number: 29
Do you have another number to enter? Y
Please type a number: 0
Do you have another number to enter? Y
Please type a number: -80
Do you have another number to enter? N

The total of your numbers is: 24
The smallest of your numbers is: -80
The largest of your numbers is: 100
The number of even numbers is:  4
The number of odd numbers is:  2
The average of you numbers is:  3.4

Process finished with exit code 0


C:\Users\ayazdani\AppData\Local\Programs\Python\Python310\python.exe C:\Users\ayazdani\PycharmProjects\CSLab4\Assignment4.py 
This program will calculate statistics for your integer data
Please type a number: 40
Do you have another number to enter? Y
Please type a number: 23
Do you have another number to enter? Y
Please type a number: 90
Do you have another number to enter? Y
Please type a number: -2
Do you have another number to enter? Y
Please type a number: 69
Do you have another number to enter? Y
Please type a number: 34
Do you have another number to enter? Y
Please type a number: 97
Do you have another number to enter? N

The total of your numbers is: 351
The smallest of your numbers is: -2
The largest of your numbers is: 97
The number of even numbers is:  4
The number of odd numbers is:  3
The average of you numbers is:  50.1

Process finished with exit code 0

"""