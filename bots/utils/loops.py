import asyncio
from typing import Callable, NoReturn


async def repeat(func: Callable, delay: int) -> NoReturn:
    """Repeat a function forever with a delay of seconds."""
    while True:
        await asyncio.sleep(delay)
        func()
