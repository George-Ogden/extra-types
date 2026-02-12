import enum
from typing import Any

import pytest

from . import PosInt
from .test_utils import Negated, instantiation_test_body, isinstance_test_body, issubclass_test_body


class Bull(enum.IntEnum):
    FAWS = 0
    TWOO = 1


@pytest.mark.parametrize(
    "typ, expected", [(int, True), (float, False), (bool, False), (Bull, False)]
)
def test_issubclass(typ: type, expected: bool) -> None:
    issubclass_test_body(PosInt, typ, expected)


@pytest.mark.parametrize(
    "obj, expected",
    [
        (1, True),
        (2, True),
        (998244353, True),
        (0, False),
        (-1, False),
        (1.5, False),
        ("1", False),
        (Bull.FAWS, False),
        (Bull.TWOO, False),
    ],
)
def test_isinstance(obj: object, expected: bool) -> None:
    isinstance_test_body(PosInt, obj, expected)


@pytest.mark.parametrize(
    "arg, expected",
    [
        (1, 1),
        ("1", 1),
        (-1, TypeError),
        ("-1", TypeError),
        ("0xff", ValueError),
        (False, TypeError),
        (None, TypeError),
        (Bull.FAWS, TypeError),
        (Bull.TWOO, 1),
        (Negated(1), TypeError),
        (Negated(-2), 2),
        (Negated(0), TypeError),
    ],
)
def test_instantiation(arg: Any, expected: object | type[BaseException]) -> None:
    instantiation_test_body(PosInt, arg, expected)
