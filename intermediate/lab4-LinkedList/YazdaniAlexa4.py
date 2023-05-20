"""
Lab 4: Linked Lists (Test Driver)
Alexander Yazdani
CWID: 20399751
Date: 03/09/2023

This file acts as a test driver for the classes defined in this project: ListNode(), LinkedList(), and ListIterator().
The file demonstrates all methods for the LinkedList class in working condition.
"""

from YazdaniAlexLL import LinkedList
from YazdaniAlexLL import LListIterator
from YazdaniAlexListNode import ListNode

def main():

    Week1 = LinkedList()
    Week1.head_val = ListNode("Mon")

    Day2 = ListNode("Tue")
    Day3 = ListNode("Wed")
    Day4 = ListNode("Thu")
    Day5 = ListNode("Fri")
    Day6 = ListNode("Sat")
    Day7 = ListNode("Sun")

    Week1.head_val.nextval = Day2
    Day2.nextval = Day3
    Day3.nextval = Day4
    Day4.nextval = Day5
    Day5.nextval = Day6
    Day6.nextval = Day7

    print("Initial Linked List:")
    for val in Week1.__iter__():
        print(val)
    print()

    print("length of Linked List:")
    print(Week1.length())
    print()

    print("Demonstartion of appending a node 'Banana' to Linked List:")
    print(f"Return Result: {Week1.append_node('Banana')}")
    for val in Week1.__iter__():
        print(val)
    print()
    
    print("Demonstration of fetching the value of node at index location 5:")
    print(Week1.fetch_node(5))
    print()

    print("Demonstration of setting node 3 to 'Apple':")
    print(f"Return Result: {Week1.set_node(3, 'Apple')}")
    for val in Week1.__iter__():
        print(val)
    print()

    print("Demonstration of inserting Node with Value 'Potato' as Node 3:")
    print(f"Return Result: {Week1.insert_node(3, 'Potato')}")
    for val in Week1.__iter__():
        print(val)
    print()

    print("Demonstration of deleting Node 7:")
    print(f"Return Result: {Week1.delete_node(7)}")
    for val in Week1.__iter__():
        print(val)
    print()

    print("Demonstration of popping last item and returning it:")
    print(f"Return Result: {Week1.pop_node()}")
    for val in Week1.__iter__():
        print(val)
    print()

if __name__ == "__main__":    
    main()

"""
Test Run:

Initial Linked List:
Mon
Tue
Wed
Thu
Fri
Sat
Sun

length of Linked List:
7

Demonstartion of appending a node 'Banana' to Linked List:
Return Result: True
Mon
Tue
Wed
Thu
Fri
Sat
Sun
Banana

Demonstration of fetching the value of node at index location 5:
Sat

Demonstration of setting node 3 to 'Apple':
Return Result: True
Mon
Tue
Wed
Apple
Fri
Sat
Sun
Banana

Demonstration of inserting Node with Value 'Potato' as Node 3:
Return Result: True
Mon
Tue
Wed
Potato
Apple
Fri
Sat
Sun
Banana

Demonstration of deleting Node 7:
Return Result: True
Mon
Tue
Wed
Potato
Apple
Fri
Sat
Banana

Demonstration of popping last item and returning it:
Return Result: Banana
Mon
Tue
Wed
Potato
Apple
Fri
Sat
"""