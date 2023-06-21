"""
Lab 9 - Mini Search Engine
Alexander Yazdani
CWID: 20399751
Date: 06/16/2023


"""

import sys
from urllib.parse import urljoin
import re
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests

from BST import BinarySearchTree
from hash_table import HashQP
from splay_tree import SplayTree
from AVL_tree import AVLTree
from keyword_entry import KeywordEntry
from minheap import MinHeap


class ResultEntry():
    """
    Class to act as search results for Webstore classs, containing url and
    score.  Lower score corresponds to higher priorities, and results act as
    entries to WebStore's priority queue.
    """
    def __init__(self, site, score):
        self._site = site
        self._score = score

    def __lt__(self, other):
        if isinstance(other, ResultEntry):
            return self._score < other._score
        else:
            return self._score < other

    def __gt__(self, other):
        if isinstance(other, ResultEntry):
            return self._score > other._score
        else:
            return self._score > other

    def __eq__(self, other):
        if isinstance(other, ResultEntry):
            return self._score == other._score
        else:
            return self._score == other

    @property
    def site(self) -> str:
        return self._site

    @property
    def score(self) -> int:
        return self._score


class WebStore():
    """
    Class that can crawl websites recuresively and store text data in the form
    of KeywordEntry() objects.  Can use any data structure for storing data
    that has both insert() and find().
    """
    def __init__(self, ds):
        self._store = ds()
        self._search_result = MinHeap()

    def crawl(self, url: str, depth=0, reg_ex=""):
        """
        Uses link_fisher() and text_harvester() to extract text from links.
        Ignores words < 4 letters and non-alphanumeric text.  If word is in
        self._store already, it will add link/location info to KeywordEntry
        object.  If word is not in self._store, it creates a new object and
        inserts into self._store.
        """
        for link in link_fisher(url, depth, reg_ex):
            for i, word in enumerate(text_harvester(link)):
                if len(word) < 4 or not word.isalpha():
                    continue
                # print(word)
                try:
                    self._store.find(word).add(link, i)
                except self._store.NotFoundError:
                    self._store.insert(KeywordEntry(word, link, i))

    def search(self, keyword: str):
        """
        Searches for a KeywordEntry in self._store
        """
        return self._store.find(keyword).sites

    def search_list(self, kw_list: list):
        """
        Uses search() method an keeps track of how many words are found vs.
        not found in self._store.
        """
        found = 0
        not_found = 0
        for word in kw_list:
            try:
                self.search(word)
                found += 1
            except self._store.NotFoundError:
                not_found += 1
        return (found, not_found)

    def search_pair(self, term_one: str, term_two: str) -> bool:
        """
        Method to search for a pair of words.
        Returns False if the two words are never found on the same webpage in
        the self._store.  Returns True if both words are found on at least one
        webpage, and adds url as a ResultEntry to the priority queue
        self._search_result.  ResultEntry has score calculated to correspond
        to priority.
        """
        self._search_result = MinHeap()
        try:
            keyword_one = self._store.find(term_one)
            keyword_two = self._store.find(term_two)
        except self._store.NotFoundError:
            return False
        links = set()
        for url in keyword_one.sites:
            if url in keyword_two.sites:
                links.add(url)
        proximity_to_each_other = sys.maxsize
        for url in links:
            proximity_to_top = (keyword_one._sites[url][0] + 1) * \
                (keyword_two._sites[url][0] + 1)
            frequency = 1 / (len(keyword_one._sites[url]) * 
                             len(keyword_two._sites[url]))
            locations_one = []
            locations_two = []
            for location in keyword_one._sites[url]:
                locations_one.append(location)
            for location in keyword_two._sites[url]:
                locations_two.append(location)
            m = len(locations_one)
            n = len(locations_two)
            a = 0
            b = 0
            while (a < m and b < n):
                if (abs(locations_one[a] - locations_two[b]) <
                        proximity_to_each_other):
                    proximity_to_each_other = abs(locations_one[a] -
                                                  locations_two[b])
                if proximity_to_each_other < 2:
                    proximity_to_each_other = 1
                    break
                if (locations_one[a] < locations_two[b]):
                    a += 1
                else:
                    b += 1
            score = proximity_to_top*frequency*proximity_to_each_other
            result = ResultEntry(url, score)
            self._search_result.insert(result)
        return True

    def get_result(self) -> ResultEntry:
        """
        Pops highest priority item from queue.
        Raises index error if queue is empty
        """
        try:
            return self._search_result.remove()
        except MinHeap.EmptyHeapError:
            raise IndexError


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
    """
    Function to help filter visible text.
    """
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


def display(node):
    print(node.data._word)


def main():

    store = WebStore(AVLTree)
    store.crawl("http://compsci.mrreed.com", 2)

    while True:
        term_one = input("Enter first term: ")
        term_two = input("Enter second term: ")
        store.search_pair(term_one, term_two)
        while True:
            try:
                result = store.get_result()
                print(result.site, result.score)
            except IndexError:
                break
        print()
    

if __name__ == "__main__":
    main()


"""
Enter first term: persistent
Enter second term: defect

Enter first term: placement
Enter second term: defect
http://compsci.mrreed.com 1.1

Enter first term: spike
Enter second term: position
http://compsci.mrreed.com/8167.html 6.0

Enter first term: waters
Enter second term: waters
http://compsci.mrreed.com/4820.html 100.0
http://compsci.mrreed.com/2649.html 7744.0

Enter first term: scissors
Enter second term: scissors
http://compsci.mrreed.com/2649.html 4.0
http://compsci.mrreed.com/7918.html 100.0
http://compsci.mrreed.com/5738.html 400.0
http://compsci.mrreed.com/8167.html 484.0
http://compsci.mrreed.com/4542.html 6889.0

Enter first term: scissors
Enter second term: floor
http://compsci.mrreed.com/2649.html 1920.0
http://compsci.mrreed.com/4542.html 114540.0

Enter first term: floor
Enter second term: scissors
http://compsci.mrreed.com/2649.html 1920.0
http://compsci.mrreed.com/4542.html 114540.0
"""
