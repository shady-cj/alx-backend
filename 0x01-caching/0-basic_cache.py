#!/usr/bin/python3
"""
The module implements  a class BasicCache that
inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits BaseCaching and extends the
    functionality
    """

    def put(self, key, item):
        """
        Puts an item into the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets the item from cache
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
