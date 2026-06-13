from typing import Any

from debug import install

from ._dynamic import DynamicCheck

install()

original_new = DynamicCheck.__new__

mcls_instances: list[type[type]] = []


def mock_new(*args: Any, **kwargs: Any) -> Any:
    cls = original_new(*args, **kwargs)
    mcls_instances.append(cls)
    return cls


DynamicCheck.__new__ = mock_new  # type: ignore [method-assign]
