import contextlib

import pytest

from .type_utils import strict_cast, strict_not_none
from .types import Char


@pytest.mark.parametrize(
    "typ, expr, passes",
    [
        (int, 5, True),
        (int | str, 5, True),
        (str | None, 5, False),
        (str, 5, False),
        (None, 5, False),
        (int | str, None, False),
        (str | None, "abc", True),
        (Char, "a", True),
        (Char, "ab", False),
        (None, "ab", False),
        (None, None, True),
        (Char | None, "a", True),
        (Char | None, "ab", False),
        (Char | None, None, True),
    ],
)
def test_strict_cast(typ: object, expr: object, passes: bool) -> None:
    with contextlib.nullcontext() if passes else pytest.raises(TypeError):
        assert strict_cast(typ, expr) is expr


@pytest.mark.parametrize("obj", [5, None, "abc", True])
def test_strict_not_none(obj: object) -> None:
    with pytest.raises(TypeError) if obj is None else contextlib.nullcontext():
        assert strict_not_none(obj) is obj
