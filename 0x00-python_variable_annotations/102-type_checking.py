#!/usr/bin/env python3
"""
Module for task 12
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a "zoomed" array determined by its factor variable
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
