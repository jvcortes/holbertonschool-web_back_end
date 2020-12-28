#!/usr/bin/python3
"""
Module for task 2
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO style cache storage.
    """

    def __init__(self):
        """
        Instance init method
        """
        BaseCaching.__init__(self)
        self.order = []

    def put(self, key, item):
        """
        Inserts a key and value pair into the storage.
        """
        if not (key or item):
            return
        self.cache_data[key] = item

        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

        if len(self.order) > BaseCaching.MAX_ITEMS:
            last = self.order.pop(-2)
            self.cache_data.pop(last)
            print('DISCARD: {}'.format(last))

    def get(self, key):
        """
        Retrieves a value inside storage from a key.
        """
       try:
            return self.cache_data[key]
        except KeyError:
            pass
