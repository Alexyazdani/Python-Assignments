"""
Lab 4: Linked Lists
Alexander Yazdani
CWID: 20399751
Date: 03/09/2023

This file creates a class ListNode() which is used in other files as nodes making up a linked list.
The class has both a data attribute and a next attribute to act as a pointer to the next node in the list.
"""
class ListNode():
    """
    ListNode class with both datavalue and next-pointer attributes
    """
    def __init__(self, dataval=None):
        """
        Object intializes to both None for both parameters, though a datavalue can be specified
        """
        self.dataval = dataval
        self.nextval = None

        