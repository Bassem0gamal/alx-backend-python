#!/usr/bin/env python3
""" Multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Multiplier """
    return lambda x: x * multiplier
