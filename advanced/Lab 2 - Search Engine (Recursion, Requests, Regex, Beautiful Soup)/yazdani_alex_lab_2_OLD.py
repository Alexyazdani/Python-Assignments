# import requests

# headers = {'User-Agent': ''}
# page = requests.get("http://foothill.edu", headers=headers)
# data = page.text
# print(data)



# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# import requests
# import re

# def get_links(url):
#     link_list = []
#     headers = {'User-Agent': ''}
#     try:
#         page = requests.get(url, headers=headers)
#     except:
#         print("Cannot access page")
#         return link_list
#     if page.status_code >= 400:
#         print("Page Error")
#     data = page.text
#     soup = BeautifulSoup(data, features="html.parser")
#     for link in soup.find_all('a'):
#         link_list.append(urljoin(url, link.get('href')))
#     return link_list

# print(get_links("http://foothill.edu"))






from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import re

def get_links(url, depth, reg_ex=""):
    link_list = [url] #if not reg_ex or re.search(reg_ex, url) else []
    if depth == 0:
        return link_list
    headers = {'User-Agent': ''}
    try:
        page = requests.get(url, headers=headers)
    except:
        print("Cannot access page")
        return link_list
    if page.status_code >= 400:
        print("Page Error")
    data = page.text
    soup = BeautifulSoup(data, features="html.parser")
    for link in soup.find_all('a'):
        link_url = urljoin(url, link.get('href'))
        if not reg_ex or re.search(reg_ex, link_url):
            if depth > 1:
                link_list += get_links(link_url, depth-1, reg_ex)
            link_list.append(link_url)
    return list(set(link_list))


def main():
    depth_list = [0, 1, 2, 3]
    print()

    for depth in depth_list:
        print(f"Number of links with depth={depth}, no regex:",  len(get_links("http://compsci.mrreed.com", depth)))
    print()

    for depth in depth_list:
        print(f'Number of links with depth={depth}, regex = "9":',  len(get_links("http://compsci.mrreed.com", depth, "9")))
    print()

if __name__ == "__main__":
    main()
