r"""
Lab 1: Fibonacci
Alexander Yazdani
CWID: 20399751
Date: 04/18/2023

This file implements three different algorithms to perform the same task.  All
three algorithms will return the nth term of the Fibonacci sequence.

The first algorithm directly calculates this number by creating a list,
starting with terms 0 and 1, then calculating the next terms by adding the
previous two.

The next algorithm implements recursion to find the nth term, so a list is not
necessary.  Instead, the function will check if n is less than or equal to 1
(that is, if the value is 0 or 1), and then proceed to call itself again,
using n-1 and n-2 as inputs.

The final algorithm also uses the same implementation of recursion, but has a
decorator “@functools.lru_cache()” which uses memoization to improve
efficiency by removing unnecessary, repeated calculations.

All three algorithms assume the user provides a valid input, so
input validation is not built into the functions.  The input is assumed to be
a positive integer, or 0.

The “main” function acts as the test program for the
three functions.  Each function is tested in order to determine its complexity.
For every given value of n, each test was run 1,000,000 times.  This sample
size was chosen for ease of understanding as the total runtime in seconds is
equivalent to the average runtime in microseconds.
"""

import time
import functools


def fibonacci_direct(n):
    """
    Function to return the nth term of the Fibonacci sequence, using direct
    calculation.
    """
    fibonacci_sequence = [0, 1]
    for i in range(2, n+1):
        next_value = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence[n]


def fibonacci_recursive(n):
    """
    Function to return the nth term of the Fibonacci sequence, using recursion.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


@functools.lru_cache()
def fibonacci_memo(n):
    """
    Function to return the nth term of the Fibonacci sequence, using recursion
    and memoization.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_memo(n-1) + fibonacci_memo(n-2)


def main():
    r"""

    Program Test Run:

    Average DIRECT time for n = 50: 14.866610900000524
    Average DIRECT time for n = 100: 30.51912099999936
    Average DIRECT time for n = 150: 45.46397650000108
    Average DIRECT time for n = 200: 60.527410200000304
    Average DIRECT time for n = 250: 74.48115899999902
    Average DIRECT time for n = 300: 90.80297369999971
    Average DIRECT time for n = 350: 106.59069970000019
    Average DIRECT time for n = 400: 122.61559619999935
    Average DIRECT time for n = 450: 148.9105251000001
    Average DIRECT time for n = 500: 178.80167059999985
    Average DIRECT time for n = 550: 197.66744530000142
    Average DIRECT time for n = 600: 218.5783010999985
    Average DIRECT time for n = 650: 235.68987959999868
    Average DIRECT time for n = 700: 251.9030533999994
    Average DIRECT time for n = 750: 272.6861984999996

    Average MEMO time for n = 50: 0.1417273999995814
    Average MEMO time for n = 100: 0.1471068999999261
    Average MEMO time for n = 150: 0.14473480000015115
    Average MEMO time for n = 200: 0.14191930000015418
    Average MEMO time for n = 250: 0.14572779999980412
    Average MEMO time for n = 300: 0.15929709999909392
    Average MEMO time for n = 350: 0.13714190000064264
    Average MEMO time for n = 400: 0.14679160000014235
    Average MEMO time for n = 450: 0.1654171000009228
    Average MEMO time for n = 500: 0.13971920000039972
    Average MEMO time for n = 550: 0.14615240000057383
    Average MEMO time for n = 600: 0.12592229999972915
    Average MEMO time for n = 650: 0.1484868000006827
    Average MEMO time for n = 700: 0.13332030000128725
    Average MEMO time for n = 750: 0.12317939999957161

    Average RECURSIVE time for n = 1: 0.5938347999999678
    Average RECURSIVE time for n = 2: 1.5584281000010378
    Average RECURSIVE time for n = 3: 2.595024199999898
    Average RECURSIVE time for n = 4: 4.708096399999704
    Average RECURSIVE time for n = 5: 7.9280651999997644
    Average RECURSIVE time for n = 6: 12.781327299999248
    Average RECURSIVE time for n = 7: 21.132885900000474
    Average RECURSIVE time for n = 8: 34.36650449999979
    Average RECURSIVE time for n = 9: 55.9554834999999
    Average RECURSIVE time for n = 10: 91.15940740000042
    Average RECURSIVE time for n = 11: 148.89537100000052
    Average RECURSIVE time for n = 12: 240.29386319999867
    Average RECURSIVE time for n = 13: 384.99597209999956
    Average RECURSIVE time for n = 14: 625.4951256999993
    Average RECURSIVE time for n = 15: 1014.4422135999994
    Average RECURSIVE time for n = 16: 1635.8572860000004
    Average RECURSIVE time for n = 17: 2642.5439177000007
    Average RECURSIVE time for n = 18: 4276.558572999998
    Average RECURSIVE time for n = 19: 6929.834979799998
    Average RECURSIVE time for n = 20: 11248.750259999997
    """

    number_of_tests = 1000000
    size_of_n_list = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550,
                      600, 650, 700, 750]

    print()

    for size_of_n in size_of_n_list:
        start = time.perf_counter()
        for _ in range(number_of_tests):
            fibonacci_direct(size_of_n)
        stop = time.perf_counter()
        print(f"Average DIRECT time for n = {size_of_n}:", (stop - start))

    print()

    size_of_n_list = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550,
                      600, 650, 700, 750]
    for size_of_n in size_of_n_list:
        start = time.perf_counter()
        for _ in range(number_of_tests):
            fibonacci_memo(size_of_n)
        stop = time.perf_counter()
        print(f"Average MEMO time for n = {size_of_n}:", (stop - start))

    print()

    size_of_n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                      17, 18, 19, 20]
    for size_of_n in size_of_n_list:
        start = time.perf_counter()
        for _ in range(number_of_tests):
            fibonacci_recursive(size_of_n)
        stop = time.perf_counter()
        print(f"Average RECURSIVE time for n = {size_of_n}:", (stop - start))

    print()


if __name__ == "__main__":
    main()
