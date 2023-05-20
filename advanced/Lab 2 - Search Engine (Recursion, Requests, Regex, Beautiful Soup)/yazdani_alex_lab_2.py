"""
Lab 2: Crawl for Links
Alexander Yazdani
CWID: 20399751
Date: 04/25/2023

This file defines a function, link_fisher, which acts as a simple search
engine.
The function uses requests to pull the text out of a webpage.
Then the function uses BeautifulSoup4 to parse the data.
All links are pulled out of the data and added to a list, which the function
eventually returns.
Relative links are converted to absolute links using urljoin() from
urllib.parse.
Recursion is used to repeat this process until the requirement of the 'depth'
input is met.
set() is used to remove duplicate links.
the re module is used to provide funtionality for an input, reg_ex, which will
make the function return only URLs containing the specified regular expression.

The function will always return a list containing the input URL as the first
element, even if that URL does not match the reg_ex input.
This can be changed to filter the input URL by changing the line "link_list =
[url]" to "link_list = [url] if not reg_ex or re.search(reg_ex, url) else []"

The function does not validate user input and has not been designed to handle
invalid inputs.
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import re


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


def main():
    """
    Test run output:

    Number of links with depth=0, no reg_ex input: 1
    Number of links with depth=1, no reg_ex input: 8
    Number of links with depth=2, no reg_ex input: 98
    Number of links with depth=3, no reg_ex input: 706

    Number of links with depth=0, reg_ex = "9": 1
    Number of links with depth=1, reg_ex = "9": 3
    Number of links with depth=2, reg_ex = "9": 17
    Number of links with depth=3, reg_ex = "9": 63

    """
    depth_list = [0, 1, 2, 3]
    print()

    for depth in depth_list:
        print(f"Number of links with depth={depth}, no reg_ex input:",
              len(link_fisher("http://compsci.mrreed.com", depth)))
    print()

    for depth in depth_list:
        print(f'Number of links with depth={depth}, reg_ex = "9":',
              len(link_fisher("http://compsci.mrreed.com", depth, "9")))
    print()


if __name__ == "__main__":
    main()
