'''
Alexander Yazdani

This module contains 2 functions.  The first, duplicate_list_elements(), will duplicate every element in a list.
The second function, search_and_sort(), will search a list for a given element, and also sort the list.
'''
def duplicate_list_elements(lst, dup_lst = []):
    '''
    Duplicates each element of a list
    '''
    if len(lst) > 0:
        dup_lst.append(lst[0])
        dup_lst.append(lst[0])
        duplicate_list_elements(lst[1:], dup_lst)
    return dup_lst

def search_and_sort(element, lst):
    '''
    Searches a given list for an element, then sorts that list.
    Also will validate user input
    '''
    try:
        if element in lst:
            search_result = (f"{element} in the list")
        else:
            search_result = (f"{element} not in the list")
        lst.sort()
        return search_result
    except:
        return "Invalid list input"
