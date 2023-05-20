"""
Linked List
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None
        self._curr = None
    
    def __contains__(self, data):
        if self._head == None:
            return False
        else:
            p = self._head
            while p is not None:
                if p.data == data:
                    return True
                p = p.next
            return False

    def add_to_head(self, data):
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node
        self.reset_to_head()

    def remove_from_head(self):
        if self._head is None:
            return None
        ret_val = self._head.data
        self._head = self._head.next
        return ret_val

    def reset_to_head(self):
        self._curr = self._head
        if self._curr is None:
            return None
        else:
            return self._curr.data

    def add_after_curr(self, data):
        if self._curr is None:
            self.add_to_head(data)
            return
        new_node = Node(data)
        new_node.next = self._curr.next
        self._curr.next = new_node

    def remove_after_curr(self):
        if self._curr is None or self._curr.next is None:
            return None
        ret_val = self._curr.next.data
        self._curr.next = self._curr.next.next
        return ret_val

    def find(self, value):
        curr_pos = self._head
        while curr_pos is not None:
            if curr_pos.data == value:
                return curr_pos.data
            curr_pos = curr_pos.next
        return None

    def delete(self, value):
        self.reset_to_head()
        if self._curr is None:
            return None
        if self._curr.data == value:
            return self.remove_from_head()
        while self._curr is not None:
            if self._curr.next.data == value:
                ret_value = self.remove_after_curr()
                self.reset_to_head()
                return ret_value
            self._curr = self._curr.next
        self.reset_to_head()
        return None
