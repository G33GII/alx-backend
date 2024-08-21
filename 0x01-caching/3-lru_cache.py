#!/usr/bin/env python3
""" 3-main """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Defines a LRU caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the cache and LRU order tracking.
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """
        Assign the item to the cache under the key.
        Implements LRU eviction if cache exceeds the max limit.
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
        Return the item stored in the cache for the key.
        Move the key to the end to mark it as recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]
