from typing import Any, cast, overload

__all__ = ["strict_cast"]


@overload
def strict_cast[T](typ: type[T], expr: Any, /) -> T: ...


@overload
def strict_cast(typ: None, expr: Any, /) -> None: ...


@overload
def strict_cast(typ: object, expr: Any, /) -> Any: ...


def strict_cast(typ: object, expr: Any, /) -> Any:
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
