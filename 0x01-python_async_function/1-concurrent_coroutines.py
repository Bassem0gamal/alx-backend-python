#!/usr/bin/env python3
""" Execute multiple coroutines  """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Execute multiple coroutines """
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
