#!/usr/bin/env python3
"""Like 3 but with random."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines."""
    list = [list.append(task_wait_random(max_delay)) for w in range(n)]
    return [await t for t in asyncio.as_completed(list)]
