#!/usr/bin/env python3
"""
Module for task 3
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Returns an asyncio `Task` object that executes the `wait_random` function
    with `max_delay` as its argument.
    """
    return asyncio.create_task(wait_random(max_delay))
