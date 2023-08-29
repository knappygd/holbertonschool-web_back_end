#!/usr/bin/env python3
"""Return a list of tasks."""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines."""
    finished: List[float] = []
    return [finished.append(task_wait_random(max_delay)) for w in range(n)]
