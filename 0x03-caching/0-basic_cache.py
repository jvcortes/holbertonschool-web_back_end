#!/usr/bin/python3
"""
Module for task 0
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic dictionary cache
    """

    def __init__(self):
        """
        Instance init method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Generates a key and value pair inside the cache dictionary
        """
        if not (key or item):
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves a value from a kwy inside the cache dictionary
        """
        if not key or key not in self.cache_data:
            return
        return self.cache_data[key]
