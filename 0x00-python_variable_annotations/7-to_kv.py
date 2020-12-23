#!/usr/bin/env python3
"""
Module for task 7
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of the square root of k, v
    """
    return k, v ** 2
