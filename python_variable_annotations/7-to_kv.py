#!/usr/bin/env python3
"""Returns a k, v tuple with the parameters as inputs."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a k, v tuple."""
    return (k, v * v)
