#!/usr/bin/python3
"""
Implements fifo Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    extends the BaseCaching and implements
    FiFo caching functionalities
    """

    def __init__(self):
        """
        Re-initializing self.cache_data as OrderedDict()
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

    def get(self, key):
        """
        Getting an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
