from typing import Any

import pytest

from . import Prob
from .test_utils import instantiation_test_body, isinstance_test_body, issubclass_test_body


class CustomProb(float): ...


@pytest.mark.parametrize(
    "typ, expected", [(float, True), (CustomProb, True), (str, False), (list, False), (int, False)]
)
def test_issubclass(typ: type, expected: bool) -> None:
    issubclass_test_body(Prob, typ, expected)


@pytest.mark.parametrize(
    "obj, expected",
    [
        (0.0, True),
        (0.5, True),
        (1.0, True),
        (0.99, True),
        (-0.01, False),
        (-1.0, False),
        (1.1, False),
        (1.2, False),
        (CustomProb(0.5), True),
        (CustomProb(1.5), False),
    ],
)
def test_isinstance(obj: object, expected: bool) -> None:
    isinstance_test_body(Prob, obj, expected)


class Half:
    def __float__(self) -> float:
        return 0.5


@pytest.mark.parametrize(
    "arg, expected",
    [
        (1, 1.0),
        ("1.0.0", ValueError),
        (Half(), 0.5),
        (10, TypeError),
        ("-1", TypeError),
        (CustomProb(0.6), 0.6),
    ],
)
def test_instantiation(arg: Any, expected: object | type[BaseException]) -> None:
    instantiation_test_body(Prob, arg, expected)
