
import random

def insertion_sort(target):
    """
    O(N^2)
    """
    for pos in range(1, len(target)):
        tmp = target[pos]
        k = pos
        while tmp < target[k-1] and k > 0:
            target[k] = target[k-1]
            k -= 1
        target[k] = tmp


def shell_sort(target):
    """
    O(N^2)
    """
    gap = len(target) // 2
    while gap > 0:
        print(gap)
        for pos in range(gap, len(target)):
            tmp = target[pos]
            k = pos
            while tmp < target[k-gap] and k >= gap:
                target[k] = target[k-gap]
                k -= gap
            target[k] = tmp
        gap //= 2


def merge_sort(collection_to_sort):
    """
    O(Nlog(N))
    """
    collection_to_sort[:] = _merge_sort(collection_to_sort)

def _merge_sort(_collection_to_sort):
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


def heap_sort(list_to_sort):
    """
    O(Nlog(N))
    """
    array_size = len(list_to_sort)
    for i in range(array_size // 2, -1, -1):
        percolate_down(list_to_sort, i, array_size)
    for i in range(array_size - 1, 0, -1):
        (list_to_sort[0], list_to_sort[i]) = (list_to_sort[i], list_to_sort[0])
        percolate_down(list_to_sort, 0, i)

def percolate_down(list_to_sort, hole, list_size):
    data = list_to_sort[hole]
    while 2 * hole + 1 < list_size:
        child = 2 * hole + 1
        if child < list_size - 1 and list_to_sort[child] < list_to_sort[child + 1]:
            child += 1
        if data < list_to_sort[child]:
            list_to_sort[hole] = list_to_sort[child]
        else:
            break
        hole = child
    list_to_sort[hole] = data


def quick_sort(list_to_sort):
    """
    O(N^2)
    """
    _quick_sort(list_to_sort, 0, len(list_to_sort) - 1)

def _quick_sort(list_to_sort, left, right):
    QS_RECUSRION_LIMIT = 15
    if left + QS_RECUSRION_LIMIT <= right:
        pivot = median_three(list_to_sort, left, right)
        i = left
        j = right - 1
        while i < j:
            for i in range(i + 1, j + 1):
                if pivot <= list_to_sort[i]:
                    break
            for j in range(j - 1, i - 1, -1):
                if list_to_sort[j] <= pivot:
                    break
            if i < j:
                list_to_sort[i], list_to_sort[j] = \
                    list_to_sort[j], list_to_sort[i]
            else:
                break
        list_to_sort[i], list_to_sort[right - 1] = \
            list_to_sort[right - 1], list_to_sort[i]
        _quick_sort(list_to_sort, left, i - 1)
        _quick_sort(list_to_sort, i + 1, right)
    else:
        insertion_sort(list_to_sort, left, right)

def median_three(list_to_sort, left, right):
    center = (left + right) // 2
    if list_to_sort[center] < list_to_sort[left]:
        list_to_sort[left], list_to_sort[center] = \
            list_to_sort[center], list_to_sort[left]
    if list_to_sort[right] < list_to_sort[left]:
        list_to_sort[left], list_to_sort[right] = \
            list_to_sort[right], list_to_sort[left]
    if list_to_sort[right] < list_to_sort[center]:
        list_to_sort[center], list_to_sort[right] = \
            list_to_sort[right], list_to_sort[center]
    list_to_sort[center], list_to_sort[right - 1] = \
        list_to_sort[right - 1], list_to_sort[center]
    return list_to_sort[right - 1]

def quicksort_insertion_sort(target, left, right):
    for pos in range(left + 1, right + 1):
        tmp = target[pos]
        k = pos
        while tmp < target[k - 1] and k > 0:
            target[k] = target[k - 1]
            k -= 1
        target[k] = tmp


def main():
    test_list = list(range(0, 113))
    random.shuffle(test_list)
    print("\n\nUnsorted List:\n")
    print(test_list)
    merge_sort(test_list)
    print("\n\nSorted List with merge_sort():\n")
    print(test_list)

if __name__ == "__main__":
    main()
