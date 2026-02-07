from typing import Literal, cast

from .type_utils import strict_cast

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
