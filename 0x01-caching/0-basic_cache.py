#!/usr/bin/env python3
"""
This is a basic CACHE module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    this class inherites from the pareent class
    (BaseCaching) 

    """

    def put(self, key, item):
        """
        this method add data to the cache_data based
        key and value
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        this method gets an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
