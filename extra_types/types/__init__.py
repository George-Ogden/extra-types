from .char import Char
from .nat import Nat
from .pos_int import PosInt

type Modified[T] = T
type Unmodified[T] = T
type New[T] = T

__all__ = ["Char", "Modified", "Nat", "New", "PosInt", "Unmodified"]
