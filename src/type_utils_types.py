from typing import Literal, cast

from .type_utils import strict_cast, strict_not_none

cast2 = cast

a: int | None = 5
b = strict_cast(int, a)
b + 2
b + "oops"  # type: ignore [operator]


c: int | float | None = 5
d = strict_cast(int | float, c)
d + 2
d + "oops"  # type: ignore [operator]


e = strict_cast(Literal[5], 10)
e + 4

f = strict_cast(None, 10)
f + "oops"  # type: ignore [operator]


g = strict_cast((int, str), 10)
g + ()  # noqa: RUF005
g + 5

h: int | None = 5
i = strict_not_none(h)
i + 4


j: list[str] | str | None = ["a"]
k = strict_not_none(j)
k + 1  # type: ignore [operator]
k[0] + 2  # type: ignore [operator]
k[0] + "3"


l: None = None  # noqa: E741
m = strict_not_none(l)  # type: ignore [var-annotated]
