import itertools

from .. import types
from ._dynamic import DynamicInstantiation
from .conftest import mcls_instances


def test_init_all() -> None:
    for instance in itertools.chain(mcls_instances, DynamicInstantiation.__subclasses__()):
        assert instance.__name__ in types.__all__


def test_init_instances() -> None:
    for instance in itertools.chain(mcls_instances, DynamicInstantiation.__subclasses__()):
        assert getattr(types, instance.__name__) is instance
