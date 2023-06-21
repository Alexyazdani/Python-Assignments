"""
Lab 8: Merge Sort
Alexander Yazdani
CWID: 20399751
Date: 06/14/2023

This file defines a public/private function pair to perform a merge sort, as
well as a helper function merge() which will merge and sort two pre-sorted
lists.  The private _merge_sort() function splits an input list into two lists
and then calls itself recursively on each list until the size of the list is
1.  Then, the merge function is used to order the list as the recursion
unwinds.

A test client provided by Eric Reed of Foothill College was modified to compare
the time (and time complexity) of the merge sort and a shell sort as the size
of the input list increases.  The client starts with a list of size 10,000,
which doubles for each trial until it reaches the final size of 10,240,000.
"""


def merge_sort(collection_to_sort):
    """
    Public function to perform a merge sort.
    """
    collection_to_sort[:] = _merge_sort(collection_to_sort)


def _merge_sort(_collection_to_sort):
    """
    Private function to perform a merge sort.
    Uses recursion to split, reorder, and then merge elements.
    """
    if len(_collection_to_sort) > 1:
        _mid_point = len(_collection_to_sort)//2
        _list_one = _collection_to_sort[:_mid_point]
        _list_two = _collection_to_sort[_mid_point:]
        _list_one = _merge_sort(_list_one)
        _list_two = _merge_sort(_list_two)
        return merge(_list_one, _list_two)
    else:
        return _collection_to_sort


def merge(list_one, list_two):
    """
    Helper function to merge two pre-sorted lists, used to help perform merge
    sort.
    """
    working = []
    list_one_pos = 0
    list_two_pos = 0
    while list_one_pos < len(list_one) and list_two_pos < len(list_two):
        if list_one[list_one_pos] <= list_two[list_two_pos]:
            working.append(list_one[list_one_pos])
            list_one_pos += 1
        else:
            working.append(list_two[list_two_pos])
            list_two_pos += 1
    while list_one_pos < len(list_one):
        working.append(list_one[list_one_pos])
        list_one_pos += 1
    while list_two_pos < len(list_two):
        working.append(list_two[list_two_pos])
        list_two_pos += 1
    return working


"""

Comparing Merge Sort and Shell Sort:
List sizes up to 10,240,000


Merge Sort...
Sorting 10,000 items took 0.07732030000011036 seconds
Shell Sort...
Sorting 10,000 items took 0.0802932999999939 seconds


Merge Sort...
Sorting 20,000 items took 0.1622479000000112 seconds
Shell Sort...
Sorting 20,000 items took 0.17419519999998556 seconds


Merge Sort...
Sorting 40,000 items took 0.33331429999998363 seconds
Shell Sort...
Sorting 40,000 items took 0.40649839999991855 seconds


Merge Sort...
Sorting 80,000 items took 0.7316960000000563 seconds
Shell Sort...
Sorting 80,000 items took 0.9708972999999332 seconds


Merge Sort...
Sorting 160,000 items took 1.5158052999997835 seconds
Shell Sort...
Sorting 160,000 items took 2.4091869999999744 seconds


Merge Sort...
Sorting 320,000 items took 3.2524272999999084 seconds
Shell Sort...
Sorting 320,000 items took 5.853394999999864 seconds


Merge Sort...
Sorting 640,000 items took 7.1022755000001325 seconds
Shell Sort...
Sorting 640,000 items took 13.950977700000067 seconds


Merge Sort...
Sorting 1,280,000 items took 15.330739700000095 seconds
Shell Sort...
Sorting 1,280,000 items took 35.07622700000002 seconds


Merge Sort...
Sorting 2,560,000 items took 36.9253470000001 seconds
Shell Sort...
Sorting 2,560,000 items took 90.56247510000003 seconds


Merge Sort...
Sorting 5,120,000 items took 69.78235500000005 seconds
Shell Sort...
Sorting 5,120,000 items took 235.67352619999997 seconds


Merge Sort...
Sorting 10,240,000 items took 147.8207379999999 seconds
Shell Sort...
Sorting 10,240,000 items took 609.968402 seconds

"""
