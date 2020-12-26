#!/usr/bin/env python3
"""
Module for task 2
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the execution time of `async_comprehension` called four times.
    """
    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    finish = time.perf_counter()

    return finish - start
