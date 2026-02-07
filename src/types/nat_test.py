import contextlib
from typing import Any

import pytest

from . import Nat


@pytest.mark.parametrize("typ, expected", [(int, True), (float, False), (bool, True)])
def test_issubclass(typ: type, expected: bool) -> None:
    assert issubclass(typ, Nat) == expected


@pytest.mark.parametrize(
    "obj, expected", [(1, True), (0, True), (-1, False), (1.5, False), ("1", False)]
)
def test_isinstance(obj: object, expected: bool) -> None:
    assert isinstance(obj, Nat) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [(1, 1), ("1", 1), (-1, TypeError), ("-1", TypeError), (False, 0), (None, TypeError)],
)
def test_instantiation(arg: Any, expected: object | type[BaseException]) -> None:
    with (
        pytest.raises(expected)
        if isinstance(expected, type) and issubclass(expected, BaseException)
        else contextlib.nullcontext()
    ):
        assert Nat(arg) == expected
