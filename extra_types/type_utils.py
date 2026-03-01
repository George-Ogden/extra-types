from typing import Any, TypeVar, cast, overload

from .types import Unmodified

__all__ = ["strict_cast", "strict_not_none"]

_T = TypeVar("_T")


@overload
def strict_cast(typ: type[_T], expr: Any, /) -> _T: ...


@overload
def strict_cast(typ: None, expr: Any, /) -> None: ...


@overload
def strict_cast(typ: object, expr: Any, /) -> Any: ...


def strict_cast(typ: object, expr: _T, /) -> Unmodified[_T]:
    """
    Determine whether an object is of a given type at runtime.
    This method is currently very limited in its ability to express types;
    as a result, it will produce false-positives, such as with `Literal` types.
    If the type does not match, this raises a `TypeError`.
    """
    if not _dynamic_type_check(typ, expr):
        raise TypeError(f"{expr} is not an instance of {typ}")
    return expr


def _dynamic_type_check(typ: object, expr: Any, /) -> bool:
    if typ is None:
        return expr is None
    try:
        return isinstance(expr, cast(type, typ))
    except TypeError:
        return True


def strict_not_none(expr: _T | None, /) -> Unmodified[_T]:
    """
    Check that an expression is not `None`.
    If it is `None`, this raises a `TypeError`.
    """
    if expr is None:
        raise TypeError(f"{expr} is {None}")
    return expr
