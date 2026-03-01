import sys
from typing import TypeVar

if sys.version_info >= (3, 12):
    from typing import TypeAliasType
else:
    from typing_extensions import TypeAliasType

_T = TypeVar("_T")

Modified = TypeAliasType("Modified", _T, type_params=(_T,))
Unmodified = TypeAliasType("Unmodified", _T, type_params=(_T,))
New = TypeAliasType("New", _T, type_params=(_T,))
