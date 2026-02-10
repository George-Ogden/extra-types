from .char import Char
from .nat import Nat

type Modified[T] = T
type Unmodified[T] = T
type New[T] = T

__all__ = ["Char", "Modified", "Nat", "New", "Unmodified"]
