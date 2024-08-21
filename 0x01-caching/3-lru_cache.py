#!/usr/bin/python3
""" 3-main """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Defines a LRU caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """
        Assign to the dictionary the item value for the given key.
        If the number of items in the cache
        is higher than BaseCaching.MAX_ITEMS,
        the least recently used item is discarded from the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lru_order.remove(key)
        self.lru_order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_recent_key = self.lru_order.pop(0)
            print(f"DISCARD: {least_recent_key}")
            del self.cache_data[least_recent_key]

    def get(self, key):
        """
        Return the value linked to the given key in the cache.
        If the key doesn't exist or is None, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]
