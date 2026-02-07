from . import Nat


def succ(x: Nat, /) -> Nat:
    return x + 1


def zero() -> Nat:
    return 0


succ(succ(zero()))

succ(
    succ(
        0.0  # type: ignore [arg-type]
    )
)

assert isinstance(Nat(0), Nat)
assert isinstance(0, Nat)
assert isinstance(1, Nat)
assert isinstance(-1, Nat)

Nat(5) % Nat(3)
succ(succ(Nat(3)) // Nat(2))
"value: " + Nat(5)  # type: ignore [operator]
