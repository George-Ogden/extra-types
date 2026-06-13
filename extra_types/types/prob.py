import sys
from typing import TYPE_CHECKING, TypeAlias, cast

if sys.version_info >= (3, 13):
    from typing import TypeIs
else:
    from typing_extensions import TypeIs


from ._dynamic import DynamicCheck, DynamicInstantiation

if TYPE_CHECKING:
    Prob: TypeAlias = float
else:

    class Prob(DynamicInstantiation, float, metaclass=DynamicCheck):
        """A numeric type representing values between 0 and 1 inclusive."""

        @classmethod
        def _is_instance(cls, instance: object) -> bool:
            return issubclass(type(instance), cls) and 0 <= cast(float, instance) <= 1

        @classmethod
        def _is_subclass(cls, sub_cls: type) -> TypeIs[type[float]]:
            return issubclass(sub_cls, float)
