#!/usr/bin/python3
"""
Implements LRU caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    The class implements LRU cache
    """

    def __init__(self):
        """
        Overriding the default self.cache_data
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
                first_value = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(first_value[0]))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Getting an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
