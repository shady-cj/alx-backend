#!/usr/bin/python3
"""
Implements LFU caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    The class implements LFU cache
    """

    def __init__(self):
        """
        Overriding the default self.cache_data
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = OrderedDict()

    def put(self, key, item):
        """
        Putting an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS and\
                 key not in self.cache_data:
                least = None
                for k, v in self.frequency.items():
                    if least is None:
                        least = (k, v)
                    elif v < least[1]:
                        least = (k, v)
                self.frequency.pop(least[0])
                self.cache_data.pop(least[0])
                print('DISCARD: {}'.format(least[0]))
            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1
            self.frequency.move_to_end(key)

    def get(self, key):
        """
        Getting an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.frequency.move_to_end(key)
            return self.cache_data.get(key)
        return None
