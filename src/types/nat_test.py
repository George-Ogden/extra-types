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
