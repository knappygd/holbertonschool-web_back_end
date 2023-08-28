#!/usr/bin/env python3
"""Sums the values of a mixed list."""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of values of a mixed list."""
    return sum(mxd_lst)
