from typing import TYPE_CHECKING

from ._dynamic import DynamicCheck, DynamicInstantiation

if TYPE_CHECKING:
    Nat = int
else:

    class Nat(DynamicInstantiation, int, metaclass=DynamicCheck):
        @classmethod
        def _is_instance(cls, instance: object) -> bool:
            return isinstance(instance, int) and instance >= 0

        @classmethod
        def _is_subclass(cls, instance: object) -> bool:
            return issubclass(instance, int)
