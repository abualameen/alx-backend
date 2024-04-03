#!/usr/bin/env python3
"""
this module implement a cache policy LIFOCache
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ This method implements the LIFO caching system"""

    def __init__(self):
        """ initializes the LIFO Cache"""
        super().__init__()

    def put(self, key, item):
        """
        this method add items to the ceche dic

        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            last_item_key = next(reversed(self.cache_data))
            print("DISCARD:", last_item_key)
            del self.cache_data[last_item_key]

    def get(self, key):
        """
        this method retrieves the items from the cache

        """
        return self.cache_data.get(key)
