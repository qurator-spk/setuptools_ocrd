from __future__ import annotations

from ._get_version import _get_version

def main():
    version = _get_version()
    print(version)

if __name__ == "__main__":
    main()
