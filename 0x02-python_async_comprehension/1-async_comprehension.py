#!/usr/bin/env python3
"""
Module for task 1
"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns a list containing all the possible generated values by the
    `async_generator` function.
    """
    return [x async for x in async_generator()]
