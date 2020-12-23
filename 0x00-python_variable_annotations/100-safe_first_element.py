#!/usr/bin/env python3
"""
Module for task 10
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a list, if it has one.
    """
    if lst:
        return lst[0]
    else:
        return None
