#!/usr/bin/env python3
"""
Defines the BasicCache class.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Represents a caching system with no limit.
    """

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.

        Args:
            key (str): The key to store the value under.
            item (Any): The value to store.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

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
