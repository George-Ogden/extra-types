import enum
from typing import Any

import pytest

from . import Nat
from .test_utils import instantiation_test_body, isinstance_test_body, issubclass_test_body


class Bull(enum.IntEnum):
    FAWS = 0
    TWOO = 1


@pytest.mark.parametrize(
    "typ, expected", [(int, True), (float, False), (bool, False), (Bull, False)]
)
def test_issubclass(typ: type, expected: bool) -> None:
    issubclass_test_body(Nat, typ, expected)


@pytest.mark.parametrize(
    "obj, expected",
    [
        (1, True),
        (0, True),
        (-1, False),
        (1.5, False),
        ("1", False),
        (Bull.FAWS, False),
        (Bull.TWOO, False),
    ],
)
def test_isinstance(obj: object, expected: bool) -> None:
    isinstance_test_body(Nat, obj, expected)


class Negated:
    def __init__(self, x: int, /) -> None:
        self.x = x

    def __int__(self) -> int:
        return -self.x


@pytest.mark.parametrize(
    "arg, expected",
    [
        (1, 1),
        ("1", 1),
        (-1, TypeError),
        ("-1", TypeError),
        (False, 0),
        (None, TypeError),
        (Bull.FAWS, 0),
        (Bull.TWOO, 1),
        (Negated(1), TypeError),
        (Negated(-2), 2),
        (Negated(0), 0),
    ],
)
def test_instantiation(arg: Any, expected: object | type[BaseException]) -> None:
    instantiation_test_body(Nat, arg, expected)
