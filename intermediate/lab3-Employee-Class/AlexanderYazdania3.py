"""
Lab 3: Inheritance- Employee Class and subclasses
Alexander Yazdani
CWID: 20399751
Date: 02/27/2023

This Program creates the class Employee() which assigns a name and a Employee number to each employee.
There are 2 subclasses for Employee().
The ProductionWorker() class adds a shift attribute (representing night or day) and an hourly wage.
The ShiftSuperVisor() class adds salary and bonus attributes.
Exceptions are used to validate inputs to all mutator methods for the following requirements:
1.  Name must not exceed 20 chars.
2.  Number must have exactly 8 numeric digits.
3.  Shift defaults to 0, and must be set to either 1 or 2 to represent day vs. night shift.
4.  Hourly wage, salary, and year-end bonus must be numeric, and will be displayed as dollar amounts to 2 decimal places.
"""

from decimal import Decimal


class Employee():

    def __init__(self, empl_name, empl_number):
        """
        Constructor for Employee parent class.
        """
        self.empl_name = ""
        self.empl_number = ""
        self.set_name(empl_name)
        self.set_number(empl_number)

    def set_name(self, empl_name):
        """
        Setter method to set name and validate name is string of length <= 20.
        """
        try:
            if type(empl_name) != str:
                raise TypeError("Name must be a string.")
            if len(empl_name) > 20:
                raise ValueError("Name cannot exceed 20 characters.")
            self.empl_name = empl_name
            return True
        except:
            return False
        
    def set_number(self, empl_number):
        """
        Setter method to set employee number and validate it is 8-digit number.
        """
        try:
            if not str(empl_number).isdigit():
                raise TypeError("ID must be an 8 digit number.")
            if len(str(empl_number)) != 8:
                raise ValueError("ID must be an 8 digit number.")
            self.empl_number = str(empl_number)
            return True
        except:
            return False
    
    def get_name(self):
        """
        Getter method that returns employee name.
        """
        return self.empl_name
    
    def get_number(self):
        """
        Getter method that returns emplyee number.
        """
        return self.empl_number
        

class ProductionWorker(Employee):
    """
    Child class for Employee class, adds shift and hourly pay.
    """
    def __init__(self, empl_name, empl_number, shift, hourly_pay):
        """
        Constructor for ProductionWorker child class of Employee parent class
        """
        super(ProductionWorker, self).__init__(empl_name, empl_number)
        self.shift = 0
        self.hourly_pay = round(Decimal(0), 2)
        self.set_shift(shift)
        self.set_hourly_pay(hourly_pay)

    def set_shift(self, shift):
        """
        Setter for shift value, validates value passed before setting.
        """
        try:
            if (str(shift) == "1") or (str(shift) == "2"):
                self.shift = int(shift)
                return True
            else:
                raise TypeError("Shift must have value 1 (daytime) or 2 (nighttime).")
        except:
            return False

    def set_hourly_pay(self, hourly_pay):
        """
        Setter for hourly pay, validates value passed before setting.
        """
        try:
            self.hourly_pay = round(Decimal(f'{hourly_pay}'), 2)
            return True
        except:
            return False
    
    def get_shift(self):
        """
        Returns shift value.
        """
        return self.shift
    
    def get_hourly_pay(self):
        """
        Returns hourly pay.
        """
        return self.hourly_pay
    
    
class ShiftSuperVisor(Employee):
    """
    ShiftSuperVisor child class, adds salary and year-end bonus.
    """
    def __init__(self, empl_name, empl_number, salary, bonus):
        """
        Constructor for ShiftSuperVisor child class of Employee parent class.
        """
        super(ShiftSuperVisor, self).__init__(empl_name, empl_number)
        self.salary = round(Decimal(0), 2)
        self.bonus = round(Decimal(0), 2)
        self.set_salary(salary)
        self.set_bonus(bonus)
    
    def set_salary(self, salary):
        """
        Setter for salary, validates value before setting.
        """
        try:
            self.salary = round(Decimal(salary), 2)
            return True
        except:
            return False
    
    def set_bonus(self, bonus):
        """
        Setter for year-end bonus, validates before setting.
        """
        try:
            self.bonus = round(Decimal(bonus), 2)
            return True
        except:
            return False
    
    def get_salary(self):
        """
        Returns salary.
        """
        return self.salary
    
    def get_bonus(self):
        """
        Returns year-end bonus.
        """
        return self.bonus
