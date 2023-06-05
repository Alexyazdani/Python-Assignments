"""
Midterm part 1
Alexander Yazdani
CWID: 20399751
Date: 05/28/2023

This file creates a class called Webstore().
Webstore() objects can crawl the web and store text data as KeywordEntry()
objects.
The data can be stored in any datastructure as long as it has both insert()
and find() implemented.
KeywordEntry() objects store the text itself when a word is found, as well as
location information.
"""

import timeit
import random
from urllib.parse import urljoin
import re
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests

from random_words import RandomWords
from BST import BinarySearchTree
from hash_table import HashQP
from splay_tree import SplayTree
from AVL_tree import AVLTree


def link_fisher(url, depth, reg_ex=""):
    """
    This function acts as a simple search engine.
    The url input is the starting base URL that the function will attempt to
    access
    The depth input specifies the depth of recursion.
    Depth of 0 will return the input URL, depth of 1 returns the input URL and
    all URLs found on that page, etc.
    """
    link_list = [url]
    if depth == 0:
        return link_list
    headers = {'User-Agent': ''}
    try:
        page = requests.get(url, headers=headers)
    except Exception:
        print("Cannot Access Page")
        return link_list
    if page.status_code >= 400:
        print("Page Error")
    data = page.text
    soup = BeautifulSoup(data, features="html.parser")
    for link in soup.find_all('a'):
        link_url = urljoin(url, link.get('href'))
        if not reg_ex or re.search(reg_ex, link_url):
            if depth > 1:
                link_list += link_fisher(link_url, depth-1, reg_ex)
            link_list.append(link_url)
    return list(set(link_list))


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta',
                               '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def words_from_html(body):
    """
    Parses the html of a webpage with Beautiful Soup.
    """
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.find_all(string=True)
    visible_texts = filter(tag_visible, texts)
    text_string = " ".join(t for t in visible_texts)
    words = re.findall(r'\w+', text_string)
    return words


def text_harvester(url):
    """
    Text harvester, returns list of words on a page.
    """
    headers = {
        'User-Agent': ''}
    try:
        page = requests.get(url, headers=headers)
    except:
        return []
    res = words_from_html(page.content)
    return res


class KeywordEntry:

    def __init__(self, word: str, url: str = None, location: int = None):
        self._word = word.upper()
        if url:
            self._sites = {url: [location]}
        else:
            self._sites = {}

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

    def __lt__(self, other):
        if isinstance(other, KeywordEntry):
            return self._word < other._word
        else:
            return self._word < other.upper()

    def __gt__(self, other):
        if isinstance(other, KeywordEntry):
            return self._word > other._word
        else:
            return self._word > other.upper()

    def __eq__(self, other):
        if isinstance(other, KeywordEntry):
            return self._word == other._word
        else:
            return self._word == other.upper()

    def __hash__(self):
        return hash(self._word)
    

class WebStore():
    """
    Class that can crawl websites recuresively and store text data in the form of KeywordEntry() objects.
    can use any data structure for storing data that has both insert() and find().
    """
    def __init__(self, ds):
        self._store = ds()

    def crawl(self, url: str, depth=0, reg_ex=""):
        """
        Uses link_fisher() and text_harvester() to extract text from links.
        Ignores words < 4 letters and non-alphanumeric text.
        If word is in self._store already, it will add link/location info to KeywordEntry object.
        If word is not in self._store, it creates a new object and inserts into self._store
        """
        for link in link_fisher(url, depth, reg_ex):
            link_text = text_harvester(link)
            for word in link_text:
                if (len(word) < 4) or (not word.isalpha()):
                    continue
                try:
                    self._store.find(word).add(link, link_text.index(word))
                except:
                    keyword = KeywordEntry(word, link, link_text.index(word))
                    self._store.insert(keyword)

    def search(self, keyword: str):
        """
        Searches for a KeywordEntry in self._store
        """
        return self._store.find(keyword)._sites

    def search_list(self, kw_list: list):
        """
        Uses search() method an keeps track of how many words are found vs. not found in self._store.
        """
        found = 0
        not_found = 0
        for word in kw_list:
            try:
                self.search(word)
                found += 1
            except:
                not_found += 1
        return (found, not_found)

    def crawl_and_list(self, url, depth=0, reg_ex=''):
        word_set = set()
        for link in link_fisher(url, depth, reg_ex):
            for word in text_harvester(link):
                if len(word) < 4 or not word.isalpha():
                    continue
                word_set.add(word)
        return list(word_set)


rw = RandomWords()
num_random_words = 5449
search_trials = 10
crawl_trials = 2
structures = [BinarySearchTree, SplayTree, AVLTree, HashQP]
for depth in range(4):
    print("\n\n\nDepth = ", depth)
    stores = [WebStore(ds) for ds in structures]
    known_words = stores[0].crawl_and_list("http://compsci.mrreed.com", depth)
    total_words = len(known_words)
    print(f"{len(known_words)} have been stored in the crawl")
    if len(known_words) > num_random_words:
        known_words = random.sample(known_words, num_random_words)
    num_words = len(known_words)
    random_words = rw.random_words(count=num_words)
    known_count = 0
    for word in random_words:
        if word in known_words:
            known_count += 1
    print(f"{known_count/len(random_words)*100:.1f}% of random words "
          f"are in known words")
    for i, store in enumerate(stores):
        print("\n\nData Structure:", structures[i])
        time_s = timeit.timeit(f'store.crawl("http://compsci.mrreed.com", depth)',
                               setup=f"from __main__ import store, depth",
                               number=crawl_trials) / crawl_trials
        print(f"Crawl and Store took {time_s:.2f} seconds")
        for phase in (random_words, known_words):
            if phase is random_words:
                print("Search is random from total pool of random words")
            else:
                print("Search only includes words that appear on the site")
            for divisor in [1, 10, 100]:
                list_len = max(num_words // divisor, 1)
                print(f"- Searching for {list_len} words")
                search_list = random.sample(phase, list_len)
                store.search_list(search_list)
                total_time_us = timeit.timeit('store.search_list(search_list)',
                            setup="from __main__ import store, search_list",
                            number=search_trials)
                time_us = total_time_us / search_trials / list_len * (10 ** 6)
                found, not_found = store.search_list(search_list)
                print(f"-- {found} of the words in kw_list were found, out of "
                      f"{found + not_found} or "
                      f"{found / (not_found + found) * 100:.0f}%")
                print(f"-- {time_us:5.2f} microseconds per search")
print(f"{search_trials} search trials and "
      f"{crawl_trials} crawl trials were conducted")


"""
Test program output:
Ran with all other applications closed on an Intel i7 core.
"""


"""
Depth =  0
38 have been stored in the crawl
0.0% of random words are in known words


Data Structure: <class 'BST.BinarySearchTree'>
Crawl and Store took 0.07 seconds
Search is random from total pool of random words
- Searching for 38 words
-- 0 of the words in kw_list were found, out of 38 or 0%
-- 63.40 microseconds per search
- Searching for 3 words
-- 0 of the words in kw_list were found, out of 3 or 0%
-- 11.70 microseconds per search
- Searching for 1 words
-- 0 of the words in kw_list were found, out of 1 or 0%
-- 45.45 microseconds per search
Search only includes words that appear on the site
- Searching for 38 words
-- 38 of the words in kw_list were found, out of 38 or 100%
-- 17.72 microseconds per search
- Searching for 3 words
-- 3 of the words in kw_list were found, out of 3 or 100%
-- 19.68 microseconds per search
- Searching for 1 words
-- 1 of the words in kw_list were found, out of 1 or 100%
-- 16.85 microseconds per search


Data Structure: <class 'splay_tree.SplayTree'>
Crawl and Store took 0.06 seconds
Search is random from total pool of random words
- Searching for 38 words
-- 0 of the words in kw_list were found, out of 38 or 0%
-- 22.46 microseconds per search
- Searching for 3 words
-- 0 of the words in kw_list were found, out of 3 or 0%
-- 24.28 microseconds per search
- Searching for 1 words
-- 0 of the words in kw_list were found, out of 1 or 0%
-- 11.60 microseconds per search
Search only includes words that appear on the site
- Searching for 38 words
-- 38 of the words in kw_list were found, out of 38 or 100%
-- 28.84 microseconds per search
- Searching for 3 words
-- 3 of the words in kw_list were found, out of 3 or 100%
-- 13.85 microseconds per search
- Searching for 1 words
-- 1 of the words in kw_list were found, out of 1 or 100%
-- 10.14 microseconds per search


Data Structure: <class 'AVL_tree.AVLTree'>
Crawl and Store took 0.17 seconds
Search is random from total pool of random words
- Searching for 38 words
-- 0 of the words in kw_list were found, out of 38 or 0%
-- 13.12 microseconds per search
- Searching for 3 words
-- 0 of the words in kw_list were found, out of 3 or 0%
-- 12.96 microseconds per search
- Searching for 1 words
-- 0 of the words in kw_list were found, out of 1 or 0%
-- 16.77 microseconds per search
Search only includes words that appear on the site
- Searching for 38 words
-- 38 of the words in kw_list were found, out of 38 or 100%
--  9.58 microseconds per search
- Searching for 3 words
-- 3 of the words in kw_list were found, out of 3 or 100%
-- 14.16 microseconds per search
- Searching for 1 words
-- 1 of the words in kw_list were found, out of 1 or 100%
-- 10.04 microseconds per search


Data Structure: <class 'hash_table.HashQP'>
Crawl and Store took 0.10 seconds
Search is random from total pool of random words
- Searching for 38 words
-- 0 of the words in kw_list were found, out of 38 or 0%
--  6.00 microseconds per search
- Searching for 3 words
-- 0 of the words in kw_list were found, out of 3 or 0%
-- 10.95 microseconds per search
- Searching for 1 words
-- 0 of the words in kw_list were found, out of 1 or 0%
--  9.03 microseconds per search
Search only includes words that appear on the site
- Searching for 38 words
-- 38 of the words in kw_list were found, out of 38 or 100%
--  7.45 microseconds per search
- Searching for 3 words
-- 3 of the words in kw_list were found, out of 3 or 100%
--  7.43 microseconds per search
- Searching for 1 words
-- 1 of the words in kw_list were found, out of 1 or 100%
--  6.26 microseconds per search



Depth =  1
598 have been stored in the crawl
10.0% of random words are in known words


Data Structure: <class 'BST.BinarySearchTree'>
Crawl and Store took 2.19 seconds
Search is random from total pool of random words
- Searching for 598 words
-- 60 of the words in kw_list were found, out of 598 or 10%
-- 18.99 microseconds per search
- Searching for 59 words
-- 6 of the words in kw_list were found, out of 59 or 10%
-- 27.99 microseconds per search
- Searching for 5 words
-- 1 of the words in kw_list were found, out of 5 or 20%
-- 20.60 microseconds per search
Search only includes words that appear on the site
- Searching for 598 words
-- 598 of the words in kw_list were found, out of 598 or 100%
-- 17.95 microseconds per search
- Searching for 59 words
-- 59 of the words in kw_list were found, out of 59 or 100%
-- 16.78 microseconds per search
- Searching for 5 words
-- 5 of the words in kw_list were found, out of 5 or 100%
-- 20.62 microseconds per search


Data Structure: <class 'splay_tree.SplayTree'>
Crawl and Store took 2.18 seconds
Search is random from total pool of random words
- Searching for 598 words
-- 60 of the words in kw_list were found, out of 598 or 10%
-- 29.75 microseconds per search
- Searching for 59 words
-- 8 of the words in kw_list were found, out of 59 or 14%
-- 23.51 microseconds per search
- Searching for 5 words
-- 0 of the words in kw_list were found, out of 5 or 0%
-- 13.73 microseconds per search
Search only includes words that appear on the site
- Searching for 598 words
-- 598 of the words in kw_list were found, out of 598 or 100%
-- 31.55 microseconds per search
- Searching for 59 words
-- 59 of the words in kw_list were found, out of 59 or 100%
-- 27.62 microseconds per search
- Searching for 5 words
-- 5 of the words in kw_list were found, out of 5 or 100%
-- 18.97 microseconds per search


Data Structure: <class 'AVL_tree.AVLTree'>
Crawl and Store took 0.76 seconds
Search is random from total pool of random words
- Searching for 598 words
-- 60 of the words in kw_list were found, out of 598 or 10%
-- 17.59 microseconds per search
- Searching for 59 words
-- 2 of the words in kw_list were found, out of 59 or 3%
-- 25.20 microseconds per search
- Searching for 5 words
-- 0 of the words in kw_list were found, out of 5 or 0%
-- 16.05 microseconds per search
Search only includes words that appear on the site
- Searching for 598 words
-- 598 of the words in kw_list were found, out of 598 or 100%
-- 13.80 microseconds per search
- Searching for 59 words
-- 59 of the words in kw_list were found, out of 59 or 100%
-- 13.99 microseconds per search
- Searching for 5 words
-- 5 of the words in kw_list were found, out of 5 or 100%
-- 12.63 microseconds per search


Data Structure: <class 'hash_table.HashQP'>
Crawl and Store took 0.79 seconds
Search is random from total pool of random words
- Searching for 598 words
-- 60 of the words in kw_list were found, out of 598 or 10%
--  5.63 microseconds per search
- Searching for 59 words
-- 8 of the words in kw_list were found, out of 59 or 14%
--  3.65 microseconds per search
- Searching for 5 words
-- 0 of the words in kw_list were found, out of 5 or 0%
--  6.43 microseconds per search
Search only includes words that appear on the site
- Searching for 598 words
-- 598 of the words in kw_list were found, out of 598 or 100%
--  5.54 microseconds per search
- Searching for 59 words
-- 59 of the words in kw_list were found, out of 59 or 100%
--  4.39 microseconds per search
- Searching for 5 words
-- 5 of the words in kw_list were found, out of 5 or 100%
--  6.98 microseconds per search



Depth =  2
3920 have been stored in the crawl
71.5% of random words are in known words


Data Structure: <class 'BST.BinarySearchTree'>
Crawl and Store took 23.22 seconds
Search is random from total pool of random words
- Searching for 3920 words
-- 2802 of the words in kw_list were found, out of 3920 or 71%
-- 25.31 microseconds per search
- Searching for 392 words
-- 274 of the words in kw_list were found, out of 392 or 70%
-- 25.51 microseconds per search
- Searching for 39 words
-- 30 of the words in kw_list were found, out of 39 or 77%
-- 24.14 microseconds per search
Search only includes words that appear on the site
- Searching for 3920 words
-- 3920 of the words in kw_list were found, out of 3920 or 100%
-- 23.36 microseconds per search
- Searching for 392 words
-- 392 of the words in kw_list were found, out of 392 or 100%
-- 24.45 microseconds per search
- Searching for 39 words
-- 39 of the words in kw_list were found, out of 39 or 100%
-- 23.02 microseconds per search


Data Structure: <class 'splay_tree.SplayTree'>
Crawl and Store took 26.73 seconds
Search is random from total pool of random words
- Searching for 3920 words
-- 2802 of the words in kw_list were found, out of 3920 or 71%
-- 33.82 microseconds per search
- Searching for 392 words
-- 275 of the words in kw_list were found, out of 392 or 70%
-- 26.87 microseconds per search
- Searching for 39 words
-- 29 of the words in kw_list were found, out of 39 or 74%
-- 19.72 microseconds per search
Search only includes words that appear on the site
- Searching for 3920 words
-- 3920 of the words in kw_list were found, out of 3920 or 100%
-- 35.76 microseconds per search
- Searching for 392 words
-- 392 of the words in kw_list were found, out of 392 or 100%
-- 26.61 microseconds per search
- Searching for 39 words
-- 39 of the words in kw_list were found, out of 39 or 100%
-- 16.75 microseconds per search


Data Structure: <class 'AVL_tree.AVLTree'>
Crawl and Store took 21.20 seconds
Search is random from total pool of random words
- Searching for 3920 words
-- 2802 of the words in kw_list were found, out of 3920 or 71%
-- 17.34 microseconds per search
- Searching for 392 words
-- 274 of the words in kw_list were found, out of 392 or 70%
-- 18.63 microseconds per search
- Searching for 39 words
-- 27 of the words in kw_list were found, out of 39 or 69%
-- 16.82 microseconds per search
Search only includes words that appear on the site
- Searching for 3920 words
-- 3920 of the words in kw_list were found, out of 3920 or 100%
-- 16.72 microseconds per search
- Searching for 392 words
-- 392 of the words in kw_list were found, out of 392 or 100%
-- 18.84 microseconds per search
- Searching for 39 words
-- 39 of the words in kw_list were found, out of 39 or 100%
-- 21.98 microseconds per search


Data Structure: <class 'hash_table.HashQP'>
Crawl and Store took 20.16 seconds
Search is random from total pool of random words
- Searching for 3920 words
-- 2802 of the words in kw_list were found, out of 3920 or 71%
--  3.94 microseconds per search
- Searching for 392 words
-- 289 of the words in kw_list were found, out of 392 or 74%
--  4.15 microseconds per search
- Searching for 39 words
-- 31 of the words in kw_list were found, out of 39 or 79%
--  3.97 microseconds per search
Search only includes words that appear on the site
- Searching for 3920 words
-- 3920 of the words in kw_list were found, out of 3920 or 100%
--  4.12 microseconds per search
- Searching for 392 words
-- 392 of the words in kw_list were found, out of 392 or 100%
--  4.15 microseconds per search
- Searching for 39 words
-- 39 of the words in kw_list were found, out of 39 or 100%
--  3.97 microseconds per search



Depth =  3
5298 have been stored in the crawl
97.2% of random words are in known words


Data Structure: <class 'BST.BinarySearchTree'>
Crawl and Store took 184.05 seconds
Search is random from total pool of random words
- Searching for 5298 words
-- 5148 of the words in kw_list were found, out of 5298 or 97%
-- 23.25 microseconds per search
- Searching for 529 words
-- 515 of the words in kw_list were found, out of 529 or 97%
-- 23.86 microseconds per search
- Searching for 52 words
-- 51 of the words in kw_list were found, out of 52 or 98%
-- 24.79 microseconds per search
Search only includes words that appear on the site
- Searching for 5298 words
-- 5298 of the words in kw_list were found, out of 5298 or 100%
-- 23.07 microseconds per search
- Searching for 529 words
-- 529 of the words in kw_list were found, out of 529 or 100%
-- 23.40 microseconds per search
- Searching for 52 words
-- 52 of the words in kw_list were found, out of 52 or 100%
-- 26.13 microseconds per search


Data Structure: <class 'splay_tree.SplayTree'>
Crawl and Store took 204.79 seconds
Search is random from total pool of random words
- Searching for 5298 words
-- 5148 of the words in kw_list were found, out of 5298 or 97%
-- 37.12 microseconds per search
- Searching for 529 words
-- 519 of the words in kw_list were found, out of 529 or 98%
-- 26.73 microseconds per search
- Searching for 52 words
-- 48 of the words in kw_list were found, out of 52 or 92%
-- 17.94 microseconds per search
Search only includes words that appear on the site
- Searching for 5298 words
-- 5298 of the words in kw_list were found, out of 5298 or 100%
-- 36.93 microseconds per search
- Searching for 529 words
-- 529 of the words in kw_list were found, out of 529 or 100%
-- 27.13 microseconds per search
- Searching for 52 words
-- 52 of the words in kw_list were found, out of 52 or 100%
-- 18.82 microseconds per search


Data Structure: <class 'AVL_tree.AVLTree'>
Crawl and Store took 193.13 seconds
Search is random from total pool of random words
- Searching for 5298 words
-- 5148 of the words in kw_list were found, out of 5298 or 97%
-- 18.10 microseconds per search
- Searching for 529 words
-- 510 of the words in kw_list were found, out of 529 or 96%
-- 18.51 microseconds per search
- Searching for 52 words
-- 48 of the words in kw_list were found, out of 52 or 92%
-- 17.81 microseconds per search
Search only includes words that appear on the site
- Searching for 5298 words
-- 5298 of the words in kw_list were found, out of 5298 or 100%
-- 17.97 microseconds per search
- Searching for 529 words
-- 529 of the words in kw_list were found, out of 529 or 100%
-- 18.43 microseconds per search
- Searching for 52 words
-- 52 of the words in kw_list were found, out of 52 or 100%
-- 17.87 microseconds per search


Data Structure: <class 'hash_table.HashQP'>
Crawl and Store took 163.24 seconds
Search is random from total pool of random words
- Searching for 5298 words
-- 5148 of the words in kw_list were found, out of 5298 or 97%
--  4.13 microseconds per search
- Searching for 529 words
-- 519 of the words in kw_list were found, out of 529 or 98%
--  4.10 microseconds per search
- Searching for 52 words
-- 48 of the words in kw_list were found, out of 52 or 92%
--  4.18 microseconds per search
Search only includes words that appear on the site
- Searching for 5298 words
-- 5298 of the words in kw_list were found, out of 5298 or 100%
--  4.18 microseconds per search
- Searching for 529 words
-- 529 of the words in kw_list were found, out of 529 or 100%
--  4.15 microseconds per search
- Searching for 52 words
-- 52 of the words in kw_list were found, out of 52 or 100%
--  4.13 microseconds per search
10 search trials and 2 crawl trials were conducted
"""