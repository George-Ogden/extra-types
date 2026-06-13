from typing import TYPE_CHECKING, TypeAlias, cast

from ._dynamic import DynamicCheck, DynamicInstantiation

if TYPE_CHECKING:
    Char: TypeAlias = str
else:

    class Char(DynamicInstantiation, str, metaclass=DynamicCheck):
        """A character type representing strings of length one."""

        @classmethod
        def _is_instance(cls, instance: object) -> bool:
            return issubclass(type(instance), cls) and len(cast(str, instance)) == 1

        @classmethod
        def _is_subclass(cls, sub_cls: type) -> bool:
            return sub_cls is str
