#!/usr/bin/env python3
"""
LFUCache module
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A class that implements an LFU (Least Frequently Used) caching system.

    Inherits from BaseCaching and manages
    cache items by their access frequency.

    The LFUCache evicts the least frequently used item when the cache exceeds
    its size limit. If multiple items have
    the same frequency, the least recently
    used among them is evicted.
    """

    def __init__(self):
        """
        Initialize the LFUCache instance.
        """
        super().__init__()
        self.frequency = {}
        self.order = {}

    def put(self, key, item):
        """
        Add an item to the cache. If the cache exceeds the maximum limit,
        evict the least frequently used item.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to be stored in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update frequency and move key to the appropriate frequency list
            self.frequency[key] += 1
            self.order[self.frequency[key] - 1].remove(key)
            self.order[self.frequency[key]].append(key)
        else:
            # Add new key with frequency 1
            self.frequency[key] = 1
            self.order.setdefault(1, []).append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Evict the least frequently used (and least recently used) key
            min_freq = min(self.order)
            lfu_key = self.order[min_freq].pop(0)
            if not self.order[min_freq]:
                del self.order[min_freq]
            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]
            print("DISCARD:", lfu_key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key associated with the item to retrieve.

        Returns:
            any: The item associated with the key, or None if the key
            does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and move key to the appropriate frequency list
        self.frequency[key] += 1
        self.order[self.frequency[key] - 1].remove(key)
        self.order.setdefault(self.frequency[key], []).append(key)
        return self.cache_data[key]
