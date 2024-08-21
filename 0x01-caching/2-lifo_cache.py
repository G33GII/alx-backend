#!/usr/bin/env python3
"""_summary_
"""

class LIFOCache(BaseCaching):
    """
    LIFO (Last In First Out) cache implementation.

    Inherits from the BaseCaching class and uses
    the self.cache_data dictionary
    from the parent class to store the cached items.
    """

    def __init__(self):
        """
        Initializes the LIFOCache object.
        Calls the parent class __init__ method.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache.
        If the number of items in the cache
        is higher that BaseCaching.MAX_ITEMS
        then the last item put in cache is removed
        from the cache and discarded.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = next(reversed(self.cache_data))
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

    def get(self, key):
        """
        Get an item by key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
