#!/usr/bin/python3
""" 1-fifo_cache.py """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """

    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the first item added to the cache
                discarded_key = next(iter(self.cache_data))
                print("DISCARD:", discarded_key)
                del self.cache_data[discarded_key]
                # print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
