from . import PosInt


def succ(x: PosInt, /) -> PosInt:
    return x + 1


def one() -> PosInt:
    return 1


succ(succ(one()))

succ(
    succ(
        0.0  # type: ignore [arg-type]
    )
)

assert isinstance(PosInt(0), PosInt)
assert isinstance(0, PosInt)
assert isinstance(1, PosInt)
assert isinstance(-1, PosInt)

PosInt(5) % PosInt(3)
succ(succ(PosInt(3)) // PosInt(2))
"value: " + PosInt(5)  # type: ignore [operator]
