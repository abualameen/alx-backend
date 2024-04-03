#!/usr/bin/env python3
"""
 this module is the most recently used cache policy 
 implementation

"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    the class is the MRU Cache policy

    """
    def __init__(self):
        """
        this method initializes the MRU instnace

        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Adds an item to the cache
        If the cache is full, removes the most
        recently used item before adding the new one.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            mru_key = self.access_order.pop()
            print("DISCARD:", mru_key)

    def get(self, key):
        """
        this method retrieves an item from the based
        onthe provided key

        """
        if key in self.cache_data:
            if key in self.access_order:
                self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        else:
            return None
