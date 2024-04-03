#!/usr/bin/env python3
"""
LFU Cache implementation
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Class LFUCache that inherits from BaseCaching
    and is a caching system implementing the LFU algorithm.
    """

    def __init__(self):
        """
        Initialize the LFU Cache
        """
        super().__init__()
        self.frequency = {}
        self.access_order = []

    def put(self, key, item):
        """
        Add an item to the cache using LFU policy.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.update_existing_key(key)
        else:
            self.add_new_key(key, item)

        self.update_access_order(key)

    def update_existing_key(self, key):
        """
        Update frequency count for an existing key.
        """
        self.frequency[key] += 1

    def add_new_key(self, key, item):
        """
        Add a new key and its corresponding item to the cache.
        """
        if len(self.cache_data) >= self.MAX_ITEMS:
            self.remove_least_frequent()

        self.cache_data[key] = item
        self.frequency[key] = 1

    def update_access_order(self, key):
        """
        Update access order of the keys in the cache.
        """
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)

    def reorder_cache(self):
        """
        Reorder cache based on access frequency and access order
        """
        self.access_order.sort(key=lambda k: (self.frequency[k], self.access_order.index(k)))

    def remove_least_frequent(self):
        """
        Remove the least frequent item(s) from the cache.
        """
        min_frequency = min(self.frequency.values())
        least_frequent_keys = [k for k, v in self.frequency.items() if v == min_frequency]

        if len(least_frequent_keys) > 1:
            self.reorder_cache()

        key_to_remove = self.access_order[0]
        self.discard_key(key_to_remove)

    def discard_key(self, key):
        """
        Discard a key from the cache.
        """
        del self.cache_data[key]
        del self.frequency[key]
        self.access_order.remove(key)
        print("DISCARD:", key)

    def get(self, key):
        """
        Retrieve an item from the cache based on the provided key.
        """
        if key in self.cache_data:
            self.update_existing_key(key)
            self.update_access_order(key)
            return self.cache_data[key]
        else:
            return None
