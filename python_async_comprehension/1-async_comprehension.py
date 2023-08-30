#!/usr/bin/env python3
"""Collects random numbers from 1 to 10 and returns them."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects random numbers from 1 to 10 and returns them."""
    return [i async for i in async_generator()]
