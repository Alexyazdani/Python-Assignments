"""
Lab 2: Bank Account Class
Alexander Yazdani
CWID: 20399751
Date: 02/07/2023

This module creates a class BankAccount() which acts as a bank account.
The user can make deposits/withdrawals, collect monthly interest, view current balance, and receive fines for overages.

"""
from decimal import Decimal
from datetime import date

class BankAccount():

    def __init__(self, initial_balance = 0):
        '''
        Consuctor for BankAccount() class to initialize balance and interest date.
        '''
        self.balance = round(Decimal(f'{initial_balance}'), 2)
        self.last_interest_date = "0000-00-00"

    def deposit(self, amount):
        '''
        Method to make deposits.
        '''
        try:
            self.balance += round(Decimal(f'{amount}'), 2)
            return True
        except:
            return False

    def withdraw(self, amount):
        '''
        Method to make withdrawals.
        Overages are denied and a $10.00 penalty is charged.
        '''
        OVERAGE_FEE = 10.00
        try:
            if self.balance < amount:
                self.balance -= Decimal(OVERAGE_FEE)
                return False
            else:
                self.balance -= round(Decimal(f'{amount}'), 2)
                return True
        except:
            return False

    def add_interest(self, interest):
        '''
        Method to collect interest on current balance.
        Can only be used once per month.
        The Method will check if it has been used this month, this year.
        Interest rate must be between 1 and 2 percent
        '''
        current_month = (str(date.today()).split('-'))[1]
        current_year = (str(date.today()).split('-'))[0]
        try:
            # if self.last_interest_date == (str(date.today()).split('-'))[1]:
            if self.last_interest_date.split('-')[1] == current_month:
                if self.last_interest_date.split('-')[0] == current_year:
                    return False
            if (interest > 2) or (interest < 1):
                return False
            else:
                self.last_interest_date = str(date.today())
                self.balance = round((self.balance*Decimal(1 + interest*0.01)), 2)
                return True
        except:
            return False
    
    def get_balance(self):
        '''
        Method to view current balance, formats with a dollar sign and thousand separators.
        The method's output is also descriptive.
        '''
        if self.balance >= 0:
            return f"  ${self.balance:,}"
        else:
            return f" -${abs(self.balance):,}"