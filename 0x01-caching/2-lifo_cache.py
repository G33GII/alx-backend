from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Defines a LIFO caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionary the item value for the given key.
        If the number of items in
        the cache is higher than BaseCaching.MAX_ITEMS,
        the last item put in the cache is discarded and added to the cache.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {last_key}")
            self.cache_data.pop(last_key)

    def get(self, key):
        """
        Return the value linked to the given key in the cache.
        If the key doesn't exist or is None, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
