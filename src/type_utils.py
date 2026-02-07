from typing import Any, cast, overload

__all__ = ["strict_cast"]


@overload
def strict_cast[T](typ: type[T], expr: Any, /) -> T: ...


@overload
def strict_cast(typ: object, expr: Any, /) -> Any: ...


def strict_cast(typ: object, expr: Any, /) -> Any:
    try:
        type_checks = isinstance(expr, cast(type, typ))
    except TypeError:
        ...
    else:
        if not type_checks:
            raise TypeError(f"{expr} is not an instance of {typ}")
    return expr
