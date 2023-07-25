## Testing

To test, build a local wheel and serve it over HTTP, to pip can install it:

```
sh serve-local-wheel.sh
```

In another terminal, try to install your package using `setuptools_ocrd` (by adding it to
`build-system.requires`):

```
cd ~/devel/another_project
pip install --extra-index-url http://127.0.0.1:28486/ .
```

## How does it work?

`setuptools_ocrd` hooks into setuptools by setting the `setuptools.finalize_distribution_options`
entry-point. This causes setuptools to call us and, if applicable, retrieve a version from
`ocrd-tool.json`.
