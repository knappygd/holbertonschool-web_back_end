#!/usr/bin/env python3
"""Returns a multiplier function that multiplies a number by the parameter."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a multiplier function."""

    def fun(n: float):
        return n * multiplier
    return fun
