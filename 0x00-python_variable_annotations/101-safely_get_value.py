#!/usr/bin/env python3
"""
Module for task 11
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar("T")

def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
    Safely returns the value from a key of a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
