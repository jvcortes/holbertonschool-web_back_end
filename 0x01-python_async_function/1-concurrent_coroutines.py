#!/usr/bin/env python3
"""
Module for task 1
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Generates a list of `n` floats containing the resulting values of `n`
    amount of `max_delay` seconds sleep coroutines.
    """
    values: List[float] = []
    coroutines: List = []
    for _ in range(n):
        coroutines.append(wait_random(max_delay))

    for value in asyncio.as_completed(coroutines):
        delay = await value
        values.append(delay)

    return values
