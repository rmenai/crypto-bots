from math import floor, log

from bots.config import Symbols


def format_large(num: int) -> str:
    """Formats large numbers to an approximate."""
    units = ['', 'K', 'M', 'B', 'T', 'P']
    k = 1000.0
    magnitude = int(floor(log(num, k)))

    n = num / k ** magnitude
    if f"{n:.2f}" == "1000.00":
        n = 1
        magnitude = magnitude + 1

    return f"{n:.2f}{units[magnitude]}"


def get_arrow(pct: float) -> str:
    """Return an arrow according to the percentage."""
    arrow = Symbols.arrow_up
    if pct < 0:
        arrow = Symbols.arrow_down

    return arrow
