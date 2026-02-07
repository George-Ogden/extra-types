import abc
from typing import TYPE_CHECKING, Any


class DynamicCheck(type, abc.ABC):
    def __new__(
        mcls: type[type],
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        /,
        **kwargs: Any,
    ) -> type:
        assert "_is_instance" in namespace or any(hasattr(base, "_is_instance") for base in bases)
        assert "_is_subclass" in namespace or any(hasattr(base, "_is_instance") for base in bases)
        return type.__new__(mcls, name, bases, namespace, **kwargs)

    def __instancecheck__(cls, instance: object) -> bool:
        return cls._is_instance(instance)

    @classmethod
    @abc.abstractmethod
    def _is_instance(cls, instance: object) -> bool: ...

    def __subclasscheck__(cls, subclass: type) -> bool:
        return cls._is_subclass(subclass)

    @classmethod
    @abc.abstractmethod
    def _is_subclass(cls, instance: object) -> bool: ...


class DynamicInstantiation:
    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        [base_cls, *_] = (
            base_cls for base_cls in cls.__bases__ if not issubclass(base_cls, DynamicInstantiation)
        )
        obj = super().__new__(base_cls, *args, **kwargs)
        if not isinstance(obj, cls):
            raise TypeError(f"{obj} is not an instance of {cls.__name__}")
        return obj


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
