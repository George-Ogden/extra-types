from typing import TypeIs, cast

from ._dynamic import DynamicCheck, DynamicInstantiation


class Prob(DynamicInstantiation, float, metaclass=DynamicCheck):
    """A numeric type representing values between 0 and 1 inclusive."""

    @classmethod
    def _is_instance(cls, instance: object) -> bool:
        return issubclass(type(instance), cls) and 0 <= cast(float, instance) <= 1

    @classmethod
    def _is_subclass(cls, sub_cls: type) -> TypeIs[type[float]]:
        return issubclass(sub_cls, float)
