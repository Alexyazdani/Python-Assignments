import random
import copy
import mergesort
import shellsort
import time


LIST_SIZE = 10000
print("\nComparing Merge Sort and Shell Sort:\nList sizes up to 10,240,000\n")
for _ in range(11):
    list_one = list(range(0, LIST_SIZE))
    random.shuffle(list_one)
    list_two = copy.copy(list_one)

    print("\nMerge Sort...")
    start_time = time.perf_counter()
    mergesort.merge_sort(list_two)
    stop_time = time.perf_counter()
    elapsed = stop_time - start_time
    print("Sorting", '{:,}'.format(LIST_SIZE), "items took", elapsed, "seconds")

    print("Shell Sort...")
    start_time = time.perf_counter()
    shellsort.shell_sort(list_one)
    stop_time = time.perf_counter()
    elapsed = stop_time - start_time
    print("Sorting", '{:,}'.format(LIST_SIZE), "items took", elapsed, "seconds\n")
    assert list_one == list_two

    LIST_SIZE *= 2

# print("\nComparing Merge Sort and Shell Sort:\nList sizes: 10,000, 20,000, 40,000, 80,000, 160,000\nEach trial was run 3 times and the average sort time is displayed.")

# for _ in range(5):

#     list_one = list(range(0, LIST_SIZE))
#     random.shuffle(list_one)
#     list_two = copy.copy(list_one)
#     list_three = copy.copy(list_one)
#     list_four = copy.copy(list_one)
#     list_five = copy.copy(list_one)
#     list_six = copy.copy(list_one)

#     print("\nMerge Sort...")
#     start_time = time.perf_counter()
#     mergesort.merge_sort(list_one)
#     mergesort.merge_sort(list_two)
#     mergesort.merge_sort(list_three)
#     stop_time = time.perf_counter()
#     elapsed = stop_time - start_time
#     average = elapsed/3
#     print("Sorting", LIST_SIZE, "items took", average, "seconds")

#     print("Shell Sort...")
#     start_time = time.perf_counter()
#     shellsort.shell_sort(list_four)
#     shellsort.shell_sort(list_five)
#     shellsort.shell_sort(list_six)
#     stop_time = time.perf_counter()
#     elapsed = stop_time - start_time
#     average = elapsed/3
#     print("Sorting", LIST_SIZE, "items took", average, "seconds\n")
#     assert list_one == list_two

#     LIST_SIZE *= 2

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