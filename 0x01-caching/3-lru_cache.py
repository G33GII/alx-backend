#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A class that implements an LRU (Least Recently Used) caching system.

    Inherits from BaseCaching and provides functionality to add items to
    the cache with an eviction strategy that removes the least recently
    used item when the cache exceeds its size limit.
    """

    def __init__(self):
        """
        Initialize the LRUCache instance.
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """
        Add an item to the cache. If the cache exceeds the maximum limit,
        evict the least recently used item.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to be stored in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lru_order.remove(key)
        self.lru_order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_recent_key = self.lru_order.pop(0)
            del self.cache_data[least_recent_key]
            print(f"DISCARD: {least_recent_key}")

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

        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]
