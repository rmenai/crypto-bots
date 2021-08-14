from bots.utils.coin import format_large, get_arrow
from bots.config import Symbols

import pytest


def test_format_large():
    assert format_large(1000000000000000) == "1.00P"
    assert format_large(1000000000000) == "1.00T"
    assert format_large(1000000000) == "1.00B"
    assert format_large(1000000) == "1.00M"
    assert format_large(1000) == "1.00K"
    assert format_large(1) == "1.00"

    assert format_large(999996) == "1.00M"
    assert format_large(1006) == "1.01K"

    with pytest.raises(ValueError):
        assert format_large(-1)


def test_get_arrow():
    assert get_arrow(10) == Symbols.arrow_up
    assert get_arrow(0) == Symbols.arrow_up
    assert get_arrow(-1) == Symbols.arrow_down
