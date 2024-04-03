#!/usr/bin/env python3
"""
this module is the LEAST FREQUENTLY USED CACHE POLICY
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
        self.cache_data[key] = item

        # Update frequency of the key
        self.frequency[key] = self.frequency.get(key, 0) + 1

        # Update access order
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)

        # Discard least frequency used items if cache exceeds capacity
        if len(self.cache_data) > self.MAX_ITEMS:
            min_frequency = min(self.frequency.values())
            keys_to_discard = [k for k, v in self.frequency.items() if v == min_frequency]

            if len(keys_to_discard) > 1:
                # If there are multiple keys with the same
                # lowest frequency, use LRU to decide
                lru_key = min(self.access_order, key=self.access_order.index)
                discarded_key = lru_key
            else:
                discarded_key = keys_to_discard[0]

            print("DISCARD:", discarded_key)
            del self.cache_data[discarded_key]
            del self.frequency[discarded_key]

            # Remove discarded key from access_order
            self.access_order.remove(discarded_key)

    def get(self, key):
        """
        Retrieve an item from the cache based on the provided key.
        """
        if key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            # Increment frequency of the key
            self.frequency[key] = self.frequency.get(key, 0) + 1
            return self.cache_data[key]
        else:
            return None
