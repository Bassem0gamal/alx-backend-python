#!/usr/bin/env python3
''' sum a list of floats and numbers '''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' sum a list of floats and numbers '''
    return sum(mxd_lst)
