"""
Assignment 3: Branching Out

Author: Alex Yazdani
CWID: 20399751
Date: 10/14/2022

This program prompts the user for their age, the number of tickets they have received in the past 3 years, and the value of their car.
It uses this information to calculate the premium the user must pay for coverage, or will refuse coverage if they have too many tickets.
"""
age = int(input("Drivers Age? "))
tickets = int(input("Number of Tickets? "))
carvalue = int(input("Value of Car? "))

if age < 25:
    agefactor = 1.15
elif age <= 29:
    agefactor = 1.1
else:
    agefactor = 1

if tickets == 1:
    ticketfactor = 1.1
elif tickets == 2:
    ticketfactor = 1.25
elif tickets == 3:
    ticketfactor = 1.5
elif tickets > 3:
    ticketfactor = 0
else:
    ticketfactor = 1

premium = carvalue*0.05*agefactor*ticketfactor

if premium == 0:
    print("Premium: $0   You are refused coverage because you have more than 3 tickets.")
else:
    print(f"Premium: ${premium:.2f}")

r"""
C:\Users\ayazdani\PycharmProjects\CSLab3\venv\Scripts\python.exe C:\Users\ayazdani\PycharmProjects\CSLab3\Assignment3.py 
Drivers Age? 35
Number of Tickets? 1
Value of Car? 10000
Premium: $550.00

Process finished with exit code 0

C:\Users\ayazdani\PycharmProjects\CSLab3\venv\Scripts\python.exe C:\Users\ayazdani\PycharmProjects\CSLab3\Assignment3.py 
Drivers Age? 29
Number of Tickets? 2
Value of Car? 15000
Premium: $1031.25

Process finished with exit code 0

C:\Users\ayazdani\PycharmProjects\CSLab3\venv\Scripts\python.exe C:\Users\ayazdani\PycharmProjects\CSLab3\Assignment3.py 
Drivers Age? 19
Number of Tickets? 3
Value of Car? 850
Premium: $73.31

Process finished with exit code 0

C:\Users\ayazdani\PycharmProjects\CSLab3\venv\Scripts\python.exe C:\Users\ayazdani\PycharmProjects\CSLab3\Assignment3.py 
Drivers Age? 81
Number of Tickets? 4
Value of Car? 12500
Premium: $0   You are refused coverage because you have more than 3 tickets.

Process finished with exit code 0

"""