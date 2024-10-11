## Testing

### Without build isolation

To test without `build`'s isolated build environment:

- Install `build`, `setuptools` and `wheel` into a venv
- Install this git version of `setuptools_ocrd` in there as well
- Try to build a test project using `python3 -m build --no-isolation`

This should build an sdist tar and a wheel. Check that _both_ have the correct version, as `build`
uses the sdist to build the wheel and `setuptools_ocrd` must make sure that `ocrd-tool.json` is
included in there as well.

e.g.:
```
Successfully built pyproject_demo-1.2.3.tar.gz and pyproject_demo-1.2.3-py3-none-any.whl
```

To troubleshoot when the wheel has the wrong version (0.0.0), inspect the sdist tar if it has
`ocrd-tool.json` (including any symlinkery) in the top directory and maybe try to build from the
sdist to debug.

### With build isolation

Testing `setuptools_ocrd` with `build`'s isolated build environment is somewhat difficult as it must
be available to pip during the build process. So to test a new version, build a local wheel and
serve it over HTTP, so pip can install it:

```
sh serve-local-wheel.sh
```

In another terminal, try to install (or build) your package using `setuptools_ocrd` (configured in
your project's `build-system.requires`):

```
cd ~/devel/another_project
PIP_EXTRA_INDEX_URL=http://127.0.0.1:28486/ python3 -m build .
```

## How does it work?

`setuptools_ocrd` hooks into setuptools by setting the `setuptools.finalize_distribution_options`
entry-point. This causes setuptools to call us and, if applicable, retrieve a version from
`ocrd-tool.json`. The `setuptools.file_finders` entry-point causes setuptools to include the
`ocrd-tool.json` symlinks/files to be included in the sdist (necessary to build a wheel with a
correct version, if built from the sdist.)


## Releasing

* Update the version in `pyproject.toml`
  * Yes, this is in `pyproject.toml`, we are not a OCR-D tool
* `git add` the `pyproject.toml` and `git commit -m 'v<version>'`
* `git tag -m 'v<version>' 'v<version>'`
* `git push; git push --tags` (or `git push --follow-tags`)

The GitHub Action (`.github/workflows/release.yml`) creates a release on GitHub and uploads to PyPI.

## How to use pre-commit

This project optionally uses [pre-commit](https://pre-commit.com) to check commits. To use it:

- Install pre-commit, e.g. `pip install -r requirements-dev.txt`
- Install the repo-local git hooks: `pre-commit install`
