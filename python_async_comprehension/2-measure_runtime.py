#!/usr/bin/env python3
"""Measure the total runtime of parallel executed funcs."""
from typing import List
from time import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of parallel executed funcs."""
    start = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    finish = time()
    return finish - start
