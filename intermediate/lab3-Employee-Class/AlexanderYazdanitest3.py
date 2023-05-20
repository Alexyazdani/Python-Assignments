"""
Lab 3: Inheritance- Employee Class and subclasses
Alexander Yazdani
CWID: 20399751
Date: 02/27/2023

This is a test driver for the module AlexanderYazdania3, which contains the class Employee() and subclasses ProductionWorker() and ShiftSuperVisor().
The file contains 2 test runs, the first uses all valid data.  It is shown that all inputs are written to the correct attributes of the objects defined.
The second test uses mostly invalid inputs.  Rather than writing these as attributes, the attributes are left as their default values.
Name and Employee Number default to an empty string, shift defaults to 0, hourly pay, salary, and bonus all default to 0.00
"""

from AlexanderYazdania3 import *

def main():

    print()
    print("Enter Production Worker Info:")
    Production_name = input("Enter the name:  ")
    Production_number = input("Enter the ID number:  ")
    Production_shift = input("Enter the shift number:  ")
    Production_hourly_pay = input("Enter the hourly pay rate:  ")
    Worker = ProductionWorker(Production_name, Production_number, Production_shift, Production_hourly_pay)

    print()
    print("Enter Shift Supervisor Info:")
    Supervisor_name = input("Enter the name:  ")
    Supervisor_number = input("Enter the number:  ")
    Supervisor_salary = input("Enter the annual salary:  ")
    Supervisor_bonus = input("Enter the annual production bonus:  ")
    Supervisor = ShiftSuperVisor(Supervisor_name, Supervisor_number, Supervisor_salary, Supervisor_bonus)

    print()
    print("Production Worker Information:")
    print(f"Name:  {Worker.get_name()}")
    print(f"ID Number:  {Worker.get_number()}")
    print(f"Shift Number:  {Worker.get_shift()}")
    print(f"Hourly Pay:  ${Worker.get_hourly_pay():,}")

    print()
    print("Shift Supervisor Information:")
    print(f"Name:  {Supervisor.get_name()}")
    print(f"ID Number:  {Supervisor.get_number()}")
    print(f"Annual Salary:  ${Supervisor.get_salary():,}")
    print(f"Annual Production Bonus:  ${Supervisor.get_bonus():,}")

    print()

if __name__ == "__main__":
    main()

"""
This is the first test run, which only uses valid inputs.
The outputs show that all attributes of the subclasses have been set correctly based on their inputs.

Enter Production Worker Info:
Enter the name:  Romulus Shaggerholm
Enter the ID number:  12345678
Enter the shift number:  1
Enter the hourly pay rate:  42.38

Enter Shift Supervisor Info:
Enter the name:  Blaidd the Half-Wolf
Enter the number:  00220033
Enter the annual salary:  135000
Enter the annual production bonus:  12000

Production Worker Information:
Name:  Romulus Shaggerholm
ID Number:  12345678
Shift Number:  1
Hourly Pay:  $42.38

Shift Supervisor Information:
Name:  Blaidd the Half-Wolf
ID Number:  00220033
Annual Salary:  $135,000.00
Annual Production Bonus:  $12,000.00

"""


"""
This is the second test run, which tries to use many invalid inputs.  
It can be seen that only valid input are written, and attributes that are given invalid inputs remain their default values.

Enter Production Worker Info:
Enter the name:  abcdefghijklmnopqrstuvwxyz
Enter the ID number:  abcdefgh
Enter the shift number:  3
Enter the hourly pay rate:  banana  

Enter Shift Supervisor Info:
Enter the name:  Jonathan blake
Enter the number:  12345678
Enter the annual salary:  potato
Enter the annual production bonus:  apple

Production Worker Information:
Name:
ID Number:
Shift Number:  0
Hourly Pay:  $0.00

Shift Supervisor Information:
Name:  Jonathan blake
ID Number:  12345678
Annual Salary:  $0.00
Annual Production Bonus:  $0.00
"""