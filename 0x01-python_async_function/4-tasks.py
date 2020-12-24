#!/usr/bin/env python3
"""
Module for task 4
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Generates a list of `n` floats containing the resulting values of `n`
    amount of `max_delay` seconds sleep asyncio `Task` objects.
    """
    values: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for value in asyncio.as_completed(tasks):
        delay = await value
        tasks.append(delay)

    return values
