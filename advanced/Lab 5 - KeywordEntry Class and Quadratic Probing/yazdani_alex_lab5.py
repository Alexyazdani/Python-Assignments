"""
Lab 5: KeywordEntry Class and Quadratic Probing
Alexander Yazdani
CWID: 20399751
Date: 05/16/2023

This file contains a definition for a class called HashQP, which will act as a
hash table that uses quadratic probing with lazy deletion.
Rehashing is done when the max lambda is reached (using the load size to
calculate lambda).
Another class is defined, HashEntry, which acts as the contents of each
'bucket' in the hash table.
Each HashEntry has a state attribute (ACTIVE, EMPTY, OR DELETED) and a data
attribute, which is the data being stored.
One final class, KeywordEntry is defined, which is used in the test program.
KeywordEntry is not yet fully developed, but eventually will be used within a
web crawler.
Each object of this class can store a word as well as links the word was found
on, and their position.
A test program at the end of the file shows the ability to insert, remove, and
find entries in the has table.
"""

import math
import copy
from enum import Enum


class HashEntry:
    """
    Entry class to be used to store data and state information in a quadratic
    probing hash table
    """
    class State(Enum):
        ACTIVE = 0
        EMPTY = 1
        DELETED = 2

    def __init__(self, data=None):
        self._data = data
        self._state = HashEntry.State.EMPTY


class HashQP:
    """
    Quadratic probing hash table class.
    Includes methods to insert, remove, and find entries.
    Automatically rehashes.
    """
    class NotFoundError(Exception):
        pass

    INIT_TABLE_SIZE = 97
    INIT_MAX_LAMBDA = .49

    def __init__(self, table_size=None):

        if table_size is None or table_size < HashQP.INIT_TABLE_SIZE:
            self._table_size = self._next_prime(HashQP.INIT_TABLE_SIZE)
        else:
            self._table_size = self._next_prime(table_size)
        self._buckets = [HashEntry() for _ in range(self._table_size)]
        self._max_lambda = HashQP.INIT_MAX_LAMBDA
        self._size = 0
        self._load_size = 0

    def _internal_hash(self, item):
        return hash(item) % self._table_size

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
                loop_lim = int((math.sqrt(candidate) + 1) / 6)
                # now we can check for divisibility by 6k +/- 1 up to sqrt
                for k in range(1, loop_lim + 1):
                    if candidate % (6 * k - 1) == 0:
                        break
                    if candidate % (6 * k + 1) == 0:
                        break
                    if k == loop_lim:
                        return candidate
            candidate += 2

    def _find_pos(self, data):
        kth_odd_number = 1
        bucket = self._internal_hash(data)
        while self._buckets[bucket]._state != HashEntry.State.EMPTY and \
                self._buckets[bucket]._data != data:
            bucket += kth_odd_number
            kth_odd_number += 2
            if bucket >= self._table_size:
                bucket -= self._table_size
        return bucket
    
    def find(self, data):
        """
        Uses _find_pos() method to return the data of an Entry.
        Returns NotFoundError if entry is not active state.
        """
        bucket = self._find_pos(data)
        if self._buckets[bucket]._state == HashEntry.State.ACTIVE:
            return self._buckets[bucket]._data
        else:
            raise self.NotFoundError
    
    def __contains__(self, data):
        bucket = self._find_pos(data)
        return self._buckets[bucket]._state == HashEntry.State.ACTIVE

    def remove(self, data):
        """
        Lazy deletion, returns false unless entry is active.
        """
        bucket = self._find_pos(data)
        if self._buckets[bucket]._state != HashEntry.State.ACTIVE:
            return False
        else:
            self._buckets[bucket]._state = HashEntry.State.DELETED
            self._size -= 1
            return True
        
    def insert(self, data):
        """
        Insert an entry and rehash if necessary.
        Returns false if entry is already active.
        """
        bucket = self._find_pos(data)
        if self._buckets[bucket]._state == HashEntry.State.ACTIVE:
            return False
        elif self._buckets[bucket]._state == HashEntry.State.EMPTY:
            self._load_size += 1
        self._buckets[bucket]._data = data
        self._buckets[bucket]._state = HashEntry.State.ACTIVE
        self._size += 1
        if self._load_size > self._max_lambda * self._table_size:
            self._rehash()
        return True

    def _rehash(self):
        """
        Rehashes the table
        """
        old_table_size = self._table_size
        self._table_size = self._next_prime(2 * old_table_size)
        old_buckets = copy.copy(self._buckets)
        self._buckets = [HashEntry() for _ in range(self._table_size)]
        self._size = 0
        self._load_size = 0
        for k in range(old_table_size):
            if old_buckets[k]._state == HashEntry.State.ACTIVE:
                self.insert(old_buckets[k]._data)
                

class KeywordEntry:
    """
    Class to be used in later webcrawler, currently unfinished.
    """
    def __init__(self, word: str, url: str = None, location: int = None):
        self._word = word.upper()
        if url:
            self._sites = {url: [location]}
        else:
            self._sites = {}

    def __lt__(self, other):
        if isinstance(other, str):
            return self._word < other.upper()
        else:
            return self._word < other._word

    def __gt__(self, other):
        if isinstance(other, str):
            return self._word > other.upper()
        else:
            return self._word > other._word

    def __eq__(self, other):
        if isinstance(other, str):
            return self._word == other.upper()
        else:
            return self._word == other._word

    def __hash__(self):
        return hash(self._word)

    def add(self, url: str, location: int) -> None:
        if url in self._sites:
            self._sites[url].append(location)
        else:
            self._sites[url] = [location]

    def get_locations(self, url: str) -> list:
        try:
            return self._sites[url]
        except IndexError:
            return []

    @property
    def sites(self) -> list:
        return [key for key in self._sites]


def main():
    """
    Test program for KeywordEntry magic methods and HashQP class.
    It is shown that entries are properly found, while nonexistent
    or deleted entries return an error.
    """
    my_hashtable = HashQP()
    obj_1 = KeywordEntry("apple", "foothill.edu", 0)
    obj_2 = KeywordEntry("banana", "calpoly.edu", 4)
    obj_3 = KeywordEntry("cranberry", "ucla.edu", 2)
    obj_4 = KeywordEntry("durian", "uci.edu", 7)
    obj_5 = KeywordEntry("eggplant", "ucdavis.edu", 22)
    obj_6 = KeywordEntry("apple", "berkeley.edu", 9)
    obj_7 = KeywordEntry("grape", "stanford.edu", 5)
    obj_8 = KeywordEntry("honeydew", "usc.edu", 33)
    obj_9 = KeywordEntry("icaco", "ucsd.edu", 12)
    obj_10 = KeywordEntry("jujube", "ucsb.edu", 4)
    obj_list = [obj_1, obj_2, obj_3, obj_4, obj_5,
                obj_6, obj_7, obj_8, obj_9, obj_10]
    obj_11 = KeywordEntry("potato", "ucsc.edu", 11)

    print("\nTesting magic methods of KeywordEntry class:")
    print(f"APPLE < BANANA? {obj_1.__lt__(obj_2)}")
    print(f"APPLE > BANANA? {obj_1.__gt__(obj_2)}")
    print(f"APPLE = BANANA? {obj_1.__eq__(obj_2)}")
    print(f"APPLE = APPLE?  {obj_1.__eq__(obj_6)}  (Comparison to another KeywordEntry)")
    print(f"APPLE = APPLE?  {obj_1.__eq__('APPLE')}  (Direct string comparison)")
    print(f"Hash of obj_1: {hash(obj_1)}")

    for key in obj_list:
        my_hashtable.insert(key)

    print("\nSites from Quadratic Probing Hash Table using find() method:")
    for obj in obj_list:
        print(my_hashtable.find(obj._word).sites)
    
    print("\nTrying to find a nonexistent entry:")
    try:
        print(my_hashtable.find(obj_11._word).sites)
    except:
        print("Not found in hash table!")
    
    my_hashtable.remove(obj_10)
    print("\nTrying to find a deleted entry:")
    try:
        print(my_hashtable.find(obj_10._word).sites)
    except:
        print("Not found in hash table!")


if __name__ == "__main__":
    main()

"""
Testing magic methods of KeywordEntry class:
APPLE < BANANA? True
APPLE > BANANA? False
APPLE = BANANA? False
APPLE = APPLE?  True  (Comparison to another KeywordEntry)
APPLE = APPLE?  True  (Direct string comparison)
Hash of obj_1: 1975482276465733496

Sites from Quadratic Probing Hash Table using find() method:
['foothill.edu']
['calpoly.edu']
['ucla.edu']
['uci.edu']
['ucdavis.edu']
['foothill.edu']
['stanford.edu']
['usc.edu']
['ucsd.edu']
['ucsb.edu']

Trying to find a nonexistent entry:
Not found in hash table!

Trying to find a deleted entry:
Not found in hash table!
"""
