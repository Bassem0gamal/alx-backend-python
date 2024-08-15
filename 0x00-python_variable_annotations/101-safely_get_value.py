#!/usr/bin/env python3
''' Safly get value '''
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[Any, T] = None) -> Union[Any, T]:
    ''' Safly get value '''
    if key in dct:
        return dct[key]
    else:
        return default
