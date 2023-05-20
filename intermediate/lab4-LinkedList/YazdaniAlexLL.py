"""
Lab 4: Linked Lists
Alexander Yazdani
CWID: 20399751
Date: 03/09/2023

This file creates 2 classes.
The first used the ListNode() class created earlier to create a Linked List of these nodes.
There are mutiple methods defined, including those to: 
- __iter__ to iterate through the list
- length to get the number of items in the list
- append_node to add a node on the end of the list
- fetch_node to return the data value of a specified node
- set_node to overwrite or set the value of a specified node
- insert_node to insert a Node in a
- delete_node to delete a node at a specified location
- pop_node to pop a Node off of the end of the list and return it
All location specifications are done with index base 0.

The next class LListIterator() acts as an iterator for the LinkedList() class.
This class has methods to iterate through the list, step to the next Node, and fetch the current node.
The class keeps track of the current node.
"""

from YazdaniAlexListNode import ListNode

class LinkedList():
    """
    Class to create linked lists.  Composed of ListNode class nodes
    """
    def __init__(self):
        """
        Init function sets initial list as empty
        """
        self.head_val = None

    def __iter__(self):
        """
        Iterator method using a generator to iterate through the list
        """
        try:
            iter_val = self.head_val
            while iter_val is not None:
                yield iter_val.dataval
                iter_val = iter_val.nextval
            return True
        except: 
            return False

    def length(self):
        """
        Returns the length of the Linked List
        """
        try:
            count = 0
            for node in self.__iter__():
                count = int(count) + 1
            return count
        except:
            return False

    def append_node(self, new_data):
        """
        Method to append a node to the end of a Linked List
        """
        try:
            new_node = ListNode(new_data)
            if self.head_val is None:
                self.head_val = new_node
                return True
            last_val = self.head_val
            while(last_val.nextval):
                last_val = last_val.nextval
            last_val.nextval = new_node
            return True
        except:
            return False
        
    def fetch_node(self, index):
        """
        Method to fetch a node from a given index (base 0)
        """
        try:
            temp_head = self.head_val
            for node in range(index+1):
                if node == index:
                    return temp_head.dataval
                temp_head = temp_head.nextval
            return False
        except:
            return False

    def set_node(self, index, new_data):
        """
        Method to set a node of a given index (base 0)
        """
        try:
            temp_head = self.head_val
            if index == 0:
                temp_head.dataval = new_data
                return True
            for node in range(index+1):
                if node == (index-1):
                    temp_head.nextval.dataval = new_data
                temp_head = temp_head.nextval
            return True
        except:
            return False

    def insert_node(self, index, new_data):
        """
        Method to insert a node after a given position
        """
        try:
            new_node = ListNode(new_data)
            temp_head = self.head_val
            if index == 0:
                new_node.nextval = self.head_val
                self.head_val = new_node
            for node in range(index+1):
                if node == (index-1):
                    temp2 = temp_head.nextval
                    temp_head.nextval = new_node
                    temp_head.nextval.nextval = temp2
                    return True
                temp_head = temp_head.nextval
            return True
        except:
            return False

    def delete_node(self, index):
        """
        Method to delete a node at a specified index
        """
        try:
            temp_head = self.head_val
            if index == 0:
                self.head_val = self.head_val.nextval
            for node in range(index+1):
                if node == (index-1):
                    temp_head.nextval = temp_head.nextval.nextval
                    return True
                temp_head = temp_head.nextval
            return True
        except:
            return False
        
    def pop_node(self):
        """
        Method to pop a node and return that value
        """
        try:
            if self.head_val is None:
                return True
            cur_val = self.head_val
            while(cur_val.nextval.nextval):
                cur_val = cur_val.nextval
            popped_val = cur_val.nextval.dataval
            cur_val.nextval = None
            return popped_val
        except:
            return False


class LListIterator():
    """
    Iterator helper class for Linked lists
    """
    def __init__(self, head):
        """
        Init function sets the current node as the specified head ListNode
        """
        self.cur_val = head

    def __iter__(self, LList):
        """
        Iterator method
        """
        try:
            iter_val = LList.head_val
            while iter_val is not None:
                yield iter_val.dataval
                iter_val = iter_val.nextval
            return True
        except:
            return False

    def __next__(self):
        """
        Method to traverse the list 1 node at a time
        """
        try:
            if self.cur_val == None:
                raise StopIteration
            else:
                self.cur_val = self.cur_val.nextval
                return self.cur_val
        except:
            return False
    
    def get_current_val(self):
        """
        Getter that returns the current node
        """
        try:
            return self.cur_val
        except:
            return False


        