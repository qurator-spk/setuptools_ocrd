# setuptools_ocrd

Manage your Python package version through `ocrd-tool.json`.

To use this, set the `version` field in `ocrd-tool.json` and use this in your `pyproject.toml`:

```
[build-system]
requires = ["setuptools>=61.0.0", "wheel", "setuptools-ocrd"]

[project]
# ... any other options ...
dynamic = ["version"]
```

## Developer information
*Please refer to [README-DEV.md](README-DEV.md).*
