#!/usr/bin/env python3
"""Yields a random number from 1 to 10."""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields a random number from 1 to 10."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
