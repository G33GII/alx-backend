#!/usr/bin/env python3
"""
MRUCache module
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A class that implements an MRU (Most Recently Used) caching system.

    Inherits from BaseCaching and uses an OrderedDict to manage cache items.
    The MRUCache evicts the most recently used item when the cache exceeds
    its size limit.
    """

    def __init__(self):
        """
        Initialize the MRUCache instance.
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache. If the cache exceeds the maximum limit,
        evict the most recently used item.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to be stored in the cache.
        """
        if key is None or item is None:
            return

        if key in self.order:
            self.order.move_to_end(key)
        else:
            if len(self.order) == BaseCaching.MAX_ITEMS:
                mru_key, _ = self.order.popitem()
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

        self.order[key] = item
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key associated with the item to retrieve.

        Returns:
            any: The item associated with the key, or None if the key
            does not exist in the cache.
        """
        if key is None or key not in self.order:
            return None

        self.order.move_to_end(key)
        return self.cache_data[key]
