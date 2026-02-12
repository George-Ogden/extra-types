import contextlib

import pytest


def issubclass_test_body(superclass: type, subclass: type, expected: bool) -> None:
    assert issubclass(subclass, superclass) == expected


def isinstance_test_body(typ: type, obj: object, expected: bool) -> None:
    assert isinstance(obj, typ) == expected


def instantiation_test_body(typ: type, arg: object, expected: object | type[BaseException]) -> None:
    with (
        pytest.raises(expected)
        if isinstance(expected, type) and issubclass(expected, BaseException)
        else contextlib.nullcontext()
    ):
        assert typ(arg) == expected


class Negated:
    def __init__(self, x: int, /) -> None:
        self.x = x

    def __int__(self) -> int:
        return -self.x
