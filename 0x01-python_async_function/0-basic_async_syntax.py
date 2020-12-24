#!/usr/bin/env python3
"""
Module for task 0
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits randomly from 0 to `max_delay` seconds.
    """
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)

    return value
