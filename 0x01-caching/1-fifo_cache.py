#!/usr/bin/env python3
"""
Defines the FIFOCache class.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Represents a FIFO caching system.
    """

    def __init__(self):
        """
        Initializes the FIFOCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds a key-value pair to the cache using the FIFO algorithm.

        Args:
            key (str): The key to store the value under.
            item (Any): The value to store.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]

    def get(self, key):
        """
        Retrieves a value from the cache based on the given key.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            Any: The value stored under the given key, or None if the key is
            None or does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
