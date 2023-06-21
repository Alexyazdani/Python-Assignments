"""
Lab 7: Implementing Priority Queue
Alexander Yazdani
CWID: 20399751
Date: 06/06/2023

This file defines a class called MinHeap which acts as a priority queue.
The class has an insert() method which will insert the node at the end of the
queue and percolate up until it reaches the appropriate position.
There is also a remove() method which will return the minimum node, then bring
the last node to the front and percolate down until the tree meets the min heap
condition.
"""

import copy


class MinHeap:
    """
    Class which acts as a priority queue.
    """
    class EmptyHeapError(Exception):
        pass

    def __init__(self, list_in=None):
        if list_in is None:
            self._heap_list = [None]
            self._size = 0
        else:
            self._heap_list = copy.deepcopy(list_in)
            self._size = len(list_in)
            self._heap_list.insert(0, 0)
            self._order_heap()

    @property
    def size(self):
        return self._size

    def insert(self, data):
        """
        Insert a node into the queue.
        """
        self._heap_list.append(None)
        self._size += 1
        child_index = self._size
        while child_index > 1 and data < self._heap_list[child_index // 2]:
            self._heap_list[child_index] = self._heap_list[child_index // 2]
            child_index = child_index // 2
        self._heap_list[child_index] = data

    def _percolate_down(self, hole):
        """
        Method to be used by remove()
        Percolates down binary tree, replacing nodes
        until min heap condition is met.
        """
        child_index = 2*hole
        while child_index <= self._size:
            if child_index + 1 <= self._size:
                if (self._heap_list[child_index+1] < self._heap_list[child_index]):
                    child_index += 1
            if self._heap_list[hole] > self._heap_list[child_index]:
                tmp = self._heap_list[hole]
                self._heap_list[hole] = self._heap_list[child_index]
                self._heap_list[child_index] = tmp
                hole = child_index
                child_index = 2*hole
            else:
                return

    def remove(self):
        """
        Remove the minimum node from the queue.
        """
        if self._size == 0:
            raise MinHeap.EmptyHeapError
        return_value = self._heap_list[1]
        self._heap_list[1] = self._heap_list[self._size]
        self._size -= 1
        self._heap_list.pop()
        if self._size > 0:
            self._percolate_down(1)
        return return_value

    def _order_heap(self):
        """
        Order the heap to meet min heap condition.
        """
        for i in range(self._size // 2, 0, -1):
            self._percolate_down(i)


def main():
    test = MinHeap([])
    print(test._heap_list)
    test.insert(5)
    print(test._heap_list)
    test.insert(7)
    print(test._heap_list)
    test.insert(16)
    print(test._heap_list)
    test.insert(16)
    print(test._heap_list)
    test.insert(15)
    print(test._heap_list)
    test.insert(20)
    print(test._heap_list)
    test.insert(16)
    print(test._heap_list)
    test.insert(10)
    print(test._heap_list)
    test.insert(16)
    print(test._heap_list)
    test.insert(13)
    print(test._heap_list)
    test.insert(19)
    print(test._heap_list)
    test.insert(16)
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)
    test.remove()
    print(test._heap_list)


if __name__ == "__main__":
    main()

"""
Test Program Output:


[0]
[0, 5]
[0, 5, 7]
[0, 5, 7, 16]
[0, 5, 7, 16, 16]
[0, 5, 7, 16, 16, 15]
[0, 5, 7, 16, 16, 15, 20]
[0, 5, 7, 16, 16, 15, 20, 16]
[0, 5, 7, 16, 10, 15, 20, 16, 16]
[0, 5, 7, 16, 10, 15, 20, 16, 16, 16]
[0, 5, 7, 16, 10, 13, 20, 16, 16, 16, 15]
[0, 5, 7, 16, 10, 13, 20, 16, 16, 16, 15, 19]
[0, 5, 7, 16, 10, 13, 16, 16, 16, 16, 15, 19, 20]
[0, 7, 10, 16, 16, 13, 16, 16, 20, 16, 15, 19]
[0, 10, 13, 16, 16, 15, 16, 16, 20, 16, 19]
[0, 13, 15, 16, 16, 19, 16, 16, 20, 16]
[0, 15, 16, 16, 16, 19, 16, 16, 20]
[0, 16, 16, 16, 20, 19, 16, 16]
[0, 16, 16, 16, 20, 19, 16]
[0, 16, 16, 16, 20, 19]
[0, 16, 19, 16, 20]
[0, 16, 19, 20]
[0, 19, 20]
[0, 20]
[0]

Exception has occurred: MinHeap.EmptyHeapError
exception: no description
"""
