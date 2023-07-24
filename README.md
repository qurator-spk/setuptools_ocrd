# setuptools_ocrd

Manage your package version through `ocrd-tool.json`.

⚠ This is not on PyPI yet, so this will only work for testing, using the instructions in
`README-DEV.md` ⚠

To use this, set the `version` field in `ocrd-tool.json` and use this in your `pyproject.toml`:

```
[build-system]
requires = ["setuptools>=61.0.0", "wheel", "setuptools-ocrd"]

[project]
# ... any other options ...
dynamic = ["version"]
```
