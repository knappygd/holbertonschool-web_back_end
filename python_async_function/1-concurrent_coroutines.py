#!/usr/bin/env python3
"""Execute multiple coroutines at the same time."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines."""
    list = []
    finished = []
    for created in range(n):
        list.append(asyncio.create_task(wait_random(max_delay)))
    for task in asyncio.as_completed(list):
        finished.append(await task)
    return finished
