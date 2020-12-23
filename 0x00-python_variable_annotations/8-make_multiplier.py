#!/usr/bin/env python3
"""
Module for task 8
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function
    """
    def a(n: float) -> float:
        """
        Returns a number multiplied by an external multiplier integer
        """
        return n * multiplier
    return a
