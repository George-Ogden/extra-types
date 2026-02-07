from collections.abc import Sequence
import enum

import pytest

from . import Char
from .test_utils import isinstance_test_body, issubclass_test_body


class Bull(enum.IntEnum):
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
