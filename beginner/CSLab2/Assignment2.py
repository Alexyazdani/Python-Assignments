"""
Assignment 2 : The Cost of Driving

Author: Alex Yazdani
CWID: 20399751
Date: 10/5/2022

Program Description:

Ask the user for car's fuel efficiency, price of gasoline per gallon, and current amount of gas in their tank.
Print these 3 values.
Calculate and display the cost to drive 100 miles as a float.
Calculate and display the amount of miles the cars is capable of with current amount of gasoline.

"""

mpg = int(input("What is your vehicle's fuel efficiency (mpg) ?  "))
gas_price = float(input("What is the price of gasoline per gallon?  "))
current_fuel = int(input("How many gallons of gas are currently your vehicle's tank?  "))

print("")
print(f"MPG: {mpg}, Gas Price: ${gas_price}, Current Fuel: {current_fuel} Gallons")

fullcost = 100*gas_price/mpg
range = int(mpg*current_fuel)

print(f"${fullcost:.2f}")
print(f"{range} miles")


r"""
C:\Users\ayazdani\PycharmProjects\CS_Lab2\venv\Scripts\python.exe C:\Users\ayazdani\PycharmProjects\CS_Lab2\Assignment2.py 
What is your vehicle's fuel efficiency (mpg) ?  25
What is the price of gasoline per gallon?  4.099
How many gallons of gas are currently your vehicle's tank?  5

MPG: 25, Gas Price: $4.099, Current Fuel: 5 Gallons
$16.40
125 miles

Process finished with exit code 0


C:\Users\ayazdani\PycharmProjects\CS_Lab2\venv\Scripts\python.exe C:\Users\ayazdani\PycharmProjects\CS_Lab2\Assignment2.py 
What is your vehicle's fuel efficiency (mpg) ?  40
What is the price of gasoline per gallon?  3.799
How many gallons of gas are currently your vehicle's tank?  10

MPG: 40, Gas Price: $3.799, Current Fuel: 10 Gallons
$9.50
400 miles

Process finished with exit code 0

"""