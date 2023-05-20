'''
Alexander Yazdani

The following program acts as a test driver for the module 'AlexanderYazdania1.py'
The program verifies the ability to duplicate elements of a list, search a list, and sort a list
'''
from AlexanderYazdania1 import *

def convert_to_list():
    '''
    Takes a user's input of space-separated elements and converts to a list
    Validates User input
    '''
    try:
        str1 = input("Enter elements of a list separated by space:  ")
        list1 = list(str1.split())
    except:
        print("Invalid Input")
        return convert_to_list()
    return list1

def main():
    '''
    Test program for solution module 'AlexanderYazdania1.py
    '''
    user_list1 = convert_to_list()
    dup_list1 = duplicate_list_elements(user_list1, [])
    print(f"List: {user_list1}")
    print(f"Dup: {dup_list1}")

    user_list2 = convert_to_list()
    dup_list2 = duplicate_list_elements(user_list2, [])
    print(f"List: {user_list2}")
    print(f"Dup: {dup_list2}")

    user_list3 = convert_to_list()
    dup_list3 = duplicate_list_elements(user_list3, [])
    print(f"List: {user_list3}")
    print(f"Dup: {dup_list3}")

    search3 = search_and_sort("banana", dup_list3)
    print(f"Search: {search3}")
    print(f"Sorted list: {dup_list3}")


if __name__ == "__main__":
    main()

r''' Test run:
Enter elements of a list separated by space:
List: []
Dup: []
Enter elements of a list separated by space:  potato
List: ['potato']
Dup: ['potato', 'potato']
Enter elements of a list separated by space:  potato apple banana
List: ['potato', 'apple', 'banana']
Dup: ['potato', 'potato', 'apple', 'apple', 'banana', 'banana']        
Search: banana in the list
Sorted list: ['apple', 'apple', 'banana', 'banana', 'potato', 'potato']
'''