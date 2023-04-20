#!/usr/bin/python3
"""
Implementing the LIFO Caching system
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Implements the LIFO system
    """

    def __init__(self):
        """
        Overriding self.cache_data to OrderedDict
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Putting an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS and\
                 key not in self.cache_data:
                first_value = self.cache_data.popitem()
                print('DISCARD: {}'.format(first_value[0]))
            self.cache_data[key] = item

    def get(self, key):
        """
        Getting an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
