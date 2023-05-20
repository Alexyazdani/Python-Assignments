"""
Hash Table for Separate Chaining.
Need to add .add() and .remove() methods to linkedlist.
"""

from LinkedList import LinkedList
import math
import copy

class HashSC:

    INIT_TABLE_SIZE = 97
    INIT_MAX_LAMBDA = 1.5

    def __init__(self, table_size=None):
        if table_size is None or table_size < HashSC.INIT_TABLE_SIZE:
            self._table_size = HashSC.INIT_TABLE_SIZE
        else:
            self._table_size = self._next_prime(table_size)
        self._max_lambda = HashSC.INIT_MAX_LAMBDA
        self._buckets = [LinkedList() for _ in range(self._table_size)]
        self._size = 0

    @property
    def size(self):
        return self._size

    @property
    def max_lambda(self):
        return self._max_lambda

    @max_lambda.setter
    def max_lambda(self, max_lambda):
        if max_lambda > 0:
            self._max_lambda = max_lambda

    def _next_prime(self, floor):
        # loop doesn't work for 2 or 3
        if floor <= 2:
            return 2
        elif floor == 3:
            return 3
        if floor % 2 == 0:
            candidate = floor + 1
        else:
            candidate = floor

        while True:
            # we know candidate is odd.  check for divisibility by 3
            if candidate % 3 != 0:
                loop_lim = int((math.sqrt(candidate) + 1)/6)
                # now we can check for divisibility by 6k +/- 1 up to sqrt
                for k in range(1, loop_lim + 1):
                    if candidate % (6 * k - 1) == 0:
                        break
                    if candidate % (6 * k + 1) == 0:
                        break
                    if k == loop_lim:
                        return candidate
            candidate += 2

    def _rehash(self):
        old_table_size = self._table_size
        self._table_size = self._next_prime(2 * old_table_size)
        old_buckets = copy.copy(self._buckets)
        self._buckets = [LinkedList() for _ in range(self._table_size)]
        self._size = 0
        for k in range(old_table_size):
            for item in old_buckets[k]:
                self.insert(item)

    def _internal_hash(self, item):
        return hash(item) % self._table_size

    def insert(self, item):
        target_bucket = self._internal_hash(item)
        if item in self._buckets[target_bucket]:
            return False
        else:
            self._buckets[target_bucket].add(item)
            self._size += 1
            if self._size > self._max_lambda * self._table_size:
                self._rehash()

            return True

    def __contains__(self, item):
        target_bucket = self._internal_hash(item)
        if item in self._buckets[target_bucket]:
            return True
        else:
            return False
    
    def remove(self, item):
        target_bucket = self._internal_hash(item)
        if self._buckets[target_bucket].remove(item):
            self._size -= 1
            return True
        else:
            return False


class Employee:

    def __init__(self, name, SSN):
        self._name = name
        self._SSN = SSN

    def __hash__(self):
        return hash((self._name, self._SSN))

    @property
    def name(self):
        return self._name

    @property
    def SSN(self):
        return self._SSN


def main():
    my_hash_table = HashSC()
    employees = []
    employees.append(Employee("mike", 123456789))
    employees.append(Employee("fred", 987654321))
    employees.append(Employee("rick", 555555555))

    print("Hash Table Size:", my_hash_table.size)
    for i in range(3):
        print("Adding", employees[i].name, "twice")
        my_hash_table.insert(employees[i])
        my_hash_table.insert(employees[i])

    print("Hash Table Size (should be 3):", my_hash_table.size)

    for i in range(3):
        if employees[i] in my_hash_table:
            print("Verified that", employees[i].name, "is in the table")
        else:
            print("oops,", employees[i].name, "was not found")


    my_hash_table_two = HashSC()

    substrate = "asdlkfj asdoiBIUYVuwer slkdjLJfwoe89)B)(798rjMG0293lkJLJ42lk3j)(*"

    substrate = substrate + substrate
    string_list = [substrate[k:k+5] for k in range(len(substrate) - 5)]

    my_hash_table_two.max_lambda = .5
    inserted = 0
    for k in range(len(substrate) - 5):
        if my_hash_table_two.insert(string_list[k]):
            print("Inserted string", k, ":", string_list[k])
            inserted += 1

        else:
            print("Did not insert", k, ":", string_list[k])
    print("Strings inserted:", inserted)
    print("Size of table:", my_hash_table_two.size)
    print("Number of buckets:", my_hash_table_two._table_size)
    print("\nFind the strings:")
    for k in range(len(substrate) - 5):
        if string_list[k] in my_hash_table_two:
            print("Found string", k, ":", string_list[k])
        else:
            print("Did not find", k, ":", string_list[k])


if __name__ == "__main__":
    main()
