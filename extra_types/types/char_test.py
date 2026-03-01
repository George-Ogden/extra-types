from collections.abc import Sequence
import enum
from typing import Any

import pytest

from . import Char
from .test_utils import instantiation_test_body, isinstance_test_body, issubclass_test_body


class Bull(enum.StrEnum):
    FAWS = "0"
    TWOO = "1"


@pytest.mark.parametrize(
    "typ, expected", [(str, True), (list, False), (Sequence, False), (Bull, False)]
)
def test_issubclass(typ: type, expected: bool) -> None:
    issubclass_test_body(Char, typ, expected)


@pytest.mark.parametrize(
    "obj, expected",
    [
        ("0", True),
        ("\0", True),
        ("", False),
        ("aa", False),
        ("ab", False),
        (["a"], False),
        (Bull.FAWS, False),
        (Bull.TWOO, False),
    ],
)
def test_isinstance(obj: object, expected: bool) -> None:
    isinstance_test_body(Char, obj, expected)


class Invisible:
    def __str__(self) -> str:
        return ""


@pytest.mark.parametrize(
    "arg, expected",
    [
        (1, "1"),
        ("a", "a"),
        ("aa", TypeError),
        (10, TypeError),
        (Invisible(), TypeError),
        (b"ab", TypeError),
        (Bull.FAWS, "0"),
        (Bull.TWOO, "1"),
    ],
)
def test_instantiation(arg: Any, expected: object | type[BaseException]) -> None:
    instantiation_test_body(Char, arg, expected)
