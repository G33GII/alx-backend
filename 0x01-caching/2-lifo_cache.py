#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO (Last-In-First-Out) caching system.
    Inherits from BaseCaching and implements a put and get method.
    """

    def __init__(self):
        """
        Initialize the class with the parent's initialization.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache using LIFO policy.

        Args:
            key (str): The key for the item.
            item (any): The item to be cached.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

    def get(self, key):
        """
        Retrieve an item by key from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The cached item, or None if the key does not exist.
        """
        return self.cache_data.get(key, None)
