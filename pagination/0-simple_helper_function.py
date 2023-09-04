#!/usr/bin/env python3
"""Task 0"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple."""
    start = page * page_size - page_size
    end = start + page_size
    return (start, end)
