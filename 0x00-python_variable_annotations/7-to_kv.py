#!/usr/bin/env python3
''' create a tuple '''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' create a tuple '''
    return (k, v * v)
