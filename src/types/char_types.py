from . import Char


def increment(c: Char) -> Char:
    return chr(ord(c) + 1)


increment("A")
increment(Char(b"A"))
increment(1)  # type: ignore [arg-type]
increment(b"A")  # type: ignore [arg-type]

assert isinstance(Char("0"), Char)
assert isinstance("0", Char)
assert isinstance("00", Char)
assert isinstance("001", Char)

Char("a") + Char("b")
"abracadabr" + Char("a")
4 + Char("a")  # type: ignore [operator]
