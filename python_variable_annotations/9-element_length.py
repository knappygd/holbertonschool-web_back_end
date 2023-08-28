#!/usr/bin/env python3
"""Annotate the given function."""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotated function."""
    return [(i, len(i)) for i in lst]
