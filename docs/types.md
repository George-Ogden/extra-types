## Types

This package provides a bunch of useful types.
They all support `isinstance`, `issubclass` and calling as validation.

### Behavior

For type checking, each class defaults to the listed base class (not `DynamicInstantiation`).
This means if you have a function like below, any number can be used for `p`.

```python
from extra_types.types import Prob # float when static type checking

def bernoulli(p: Prob):
    # p not type checked at run time

bernoulli(0.5) # this is fine
bernoulli(2.0) # this passes static type checking
bernoulli("NaN") # this will give you an error with a static type checker
```

There a few ways to improve this function:

```python
from extra_types.types import Prob
from extra_types.type_utils import strict_cast

def bernoulli(p: Prob):
    assert isinstance(p, Prob) # AssertionError
    p = Prob(p) # TypeError
    p = strict_cast(Prob, p) # TypeError
```

All of these will fail if you use `2.0` as your probability.

You can also use other libraries, like [`typeguard`](https://typeguard.readthedocs.io/en/latest/) and [`attrs`](https://www.attrs.org/en/stable/index.html) for automatic validation:

```python
import attrs

@attrs.define
class AgentConfig:
    agent_size: PosInt = attrs.field(validator=attrs.validators.instance_of(PosInt))


import typeguard

@typeguard.typechecked
def decrement(x: PosInt) -> Nat:
    return x - 1
```

Despite what it looks, you cannot create an instance of these classes (unless you do some magic of your own).
Take this sample:

```python
p = Prob("0.5") # Checks that p is valid.
assert type(p) is float # Always True
```

This makes it compatible with any other code.

The same logic applies to the other types!

::: extra_types.types
