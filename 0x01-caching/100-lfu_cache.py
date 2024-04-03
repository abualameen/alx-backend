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

    def remove_least_frequent(self):
        """
        Remove the least frequent item(s) from the cache.
        """
        min_frequency = min(self.frequency.values())
        least_frequent_keys = [k for k, v in self.frequency.items() if v == min_frequency]

        if len(least_frequent_keys) > 1:
            lru_key = min(self.access_order, key=self.access_order.index)
            least_frequent_keys.remove(lru_key)

        for key in least_frequent_keys:
            self.discard_key(key)

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

    def __reorder_items(self, mru_key):
        """
        Reorders the items in the cache based on the most recently used item.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])
