#!/usr/bin/env python3
"""
this module returns a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.
"""


def index_range(page, page_size):
    """
    the function return a tupple
    """
    if page == 1:
        page = 0
    else:
        page_size = page * page_size
        page = page * 10
    
    return ((page, page_size))
