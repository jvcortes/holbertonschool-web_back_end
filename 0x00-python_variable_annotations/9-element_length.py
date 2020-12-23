#!/usr/bin/env python3
"""
Module for task 9
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list containing every item and its length by every item inside
    a list of iterables.
    """
    return [(x, len(x)) for x in lst]
