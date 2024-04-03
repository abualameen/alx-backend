#!/usr/bin/env python3
"""
this module implements the least recently used policy

"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    this method implements LRU CECHE

    """

    def __init__(self):
        """ initializes the LRU Cache """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        this method add item to cache use LRU policy
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        # self.access_order.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            # del self.cache_data[lru_key]
            lru_key = self.access_order.pop(0)
            print("DISCARD:", lru_key)
            if lru_key in self.cache_data:
                del self.cache_data[lru_key]
        self.access_order.append(key)

    def get(self, key):
        """
        gets or retrieves an item for the cache
        Updates the access order to reflect the most recent use of the key

        """
        if key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        else:
            return None
