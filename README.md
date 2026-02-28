# Extra Types

Extra types and type utilities for Python.
It provides some useful types that can be easily integrated into your code.
Documentation available at (TODO)

## Example

`PosInt` represents positive integers.

```python
from extra_types.types import PosInt

isinstance(0, PosInt) # False
isinstance(1, PosInt) # True
isinstance(2, PosInt) # True
isinstance(1.5, PosInt) # False
isinstance(object(), PosInt) # False


# Use it as a type hint
def setup_agents(num_agents: PosInt) -> None:
    ...

# Validate with attrs
import attrs
@attrs.define
class AgentConfig:
    agent_size: PosInt = attrs.field(validator=attrs.validators.instance_of(PosInt))

# Check with strict cast
from extra_types.type_utils import strict_cast

def generate_positive_integer() -> PosInt:
    number = ...
    return strict_cast(PosInt, number) # raises a TypeError if not a positive integer
```

## Install

### Quick Install

```bash
uv pip install git+https://github.com/George-Ogden/extra-types
```

### Slow Install

```bash
pip install git+https://github.com/George-Ogden/extra-types
```

## Bugs/Feedback

Use the issue tracker for bugs/feedback, please.
