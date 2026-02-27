from .prob import Prob


def bottom() -> Prob:
    return 0.0


def top() -> Prob:
    return 1


def random(p: Prob) -> bool:
    return True


random(0.5)
random(Prob(0.5))

Prob(0.5) ** 2
[][Prob(0.5)]  # type: ignore [call-overload]
