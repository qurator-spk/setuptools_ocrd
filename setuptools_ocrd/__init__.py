from __future__ import annotations

from ._get_version import _get_version

def get_version():
    return _get_version()

__all__ = [
    "get_version",
]
