
'''
This file acts as a test driver for the AlexanderYazdaniBank.py module.
All mutators are used, and their boolean results are printed.
The new current balance is also printed after each action.
'''
from AlexanderYazdaniBank import BankAccount

def main():
    '''
    Main test driving function.
    '''
    my_account = BankAccount(1000.00)
    print(my_account.get_balance(), "\n")

    print(my_account.deposit(500.00))
    print(my_account.get_balance(), "\n")

    print(my_account.withdraw(2000.00))
    print(my_account.get_balance(), "\n")

    print(my_account.add_interest(1))
    print(my_account.get_balance(), "\n")

    print(my_account.add_interest(2))
    print(my_account.get_balance(), "\n")

    print(my_account.deposit(125000.99))
    print(my_account.get_balance(), "\n")

    print(my_account.withdraw(0.99))
    print(my_account.get_balance(), "\n")

    print(my_account.withdraw(126500.00))
    print(my_account.get_balance(), "\n")

    print(my_account.withdraw(10.00))
    print(my_account.get_balance(), "\n")

    print(my_account.add_interest(1))
    print(my_account.get_balance(), "\n")

if __name__ == "__main__":
    main()

'''
Current Account Balance:  $1,000.00 

True
Current Account Balance:  $1,500.00

False
Current Account Balance:  $1,490.00

True
Current Account Balance:  $1,504.90

False
Current Account Balance:  $1,504.90

True
Current Account Balance:  $126,505.89

True
Current Account Balance:  $126,504.90

True
Current Account Balance:  $4.90

False
Current Account Balance: -$5.10

False
Current Account Balance: -$5.10

'''
