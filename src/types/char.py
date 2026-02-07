from typing import cast

from ._dynamic import DynamicCheck, DynamicInstantiation


class Char(DynamicInstantiation, int, metaclass=DynamicCheck):
    @classmethod
    def _is_instance(cls, instance: object) -> bool:
        return issubclass(type(instance), cls) and len(cast(str, instance)) == 1

    @classmethod
    def _is_subclass(cls, sub_cls: type) -> bool:
        return sub_cls is str
