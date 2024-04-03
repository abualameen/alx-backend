#!/usr/bin/env python3
"""
module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Class LFUCache that inherits from BaseCaching
    and is a caching system implementing the LFU algorithm.
    """

    def __init__(self):
        """ Initialize the LFU Cache """
        super().__init__()
        self.frequency = {}
        self.access_order = []

    def put(self, key, item):
        """
        Add an item to the cache using LFU policy.
        """
        if key is None or item is None:
            return

        # If key already exists, update its frequency
        if key in self.cache_data:
            self.access_order.remove(key)
            self.frequency[key] += 1
        else:
            # If key is new, add it to cache and set its frequency to 1
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.remove_least_frequent()

            self.cache_data[key] = item
            self.frequency[key] = 1

        self.access_order.append(key)

    def remove_least_frequent(self):
        """
        Remove the least frequent item(s) from the cache.
        """
        min_frequency = min(self.frequency.values())
        least_frequent_keys = [k for k, v in self.frequency.items() if v == min_frequency]

        # If there are multiple least frequent keys, use LRU to decide
        if len(least_frequent_keys) > 1:
            lru_key = min(self.access_order, key=self.access_order.index)
            least_frequent_keys.remove(lru_key)

        # Remove the least frequent key(s) from cache and frequency dictionary
        for key in least_frequent_keys:
            del self.cache_data[key]
            del self.frequency[key]
            self.access_order.remove(key)
            print("DISCARD:", key)

    def get(self, key):
        """
        Retrieve an item from the cache based on the provided key.
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        else:
            return None
