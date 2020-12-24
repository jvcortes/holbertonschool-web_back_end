#!/usr/bin/env python3
"""
Module for task 2
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    Measures and returns the execution time of `wait_n` with `n` and
    `max_delay` as its arguments.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    finish = time.perf_counter()
    result = (start - finish) / n

    return result
