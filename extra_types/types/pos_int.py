from typing import TYPE_CHECKING, TypeAlias

from ._dynamic import DynamicCheck, DynamicInstantiation

if TYPE_CHECKING:
    PosInt: TypeAlias = int
else:

    class PosInt(DynamicInstantiation, int, metaclass=DynamicCheck):
        """A positive number type representing integers strictly greater than zero."""

        @classmethod
        def _is_instance(cls, instance: object) -> bool:
            return issubclass(type(instance), cls) and instance > 0

        @classmethod
        def _is_subclass(cls, sub_cls: type) -> bool:
            return sub_cls is int
