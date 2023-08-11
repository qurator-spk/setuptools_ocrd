import logging
import os
import warnings

import setuptools

from setuptools_ocrd import _get_version

log = logging.getLogger(__name__)


def _warn_on_old_setuptools(_version=setuptools.__version__):
    if int(_version.split(".")[0]) < 61:
        warnings.warn(RuntimeWarning(f"setuptools=={_version} is old!"))


_warn_on_old_setuptools()


def get_ocrd_tool_version(dist):
    if dist.metadata.version is not None:
        return

    if dist.metadata.name == "setuptools_ocrd":
        return

    dist.metadata.version = _get_version()


def file_finder_ocrd_tool(dirname):
    """Find ocrd-tool.json (to be included by setuptools)"""

    # ocrd-tool.json is a symlink to somepath/ocrd-tool.json, find it and resolve if
    # necessary.
    name = os.path.join(dirname, "ocrd-tool.json")

    if os.path.lexists(name):
        yield name
        # resolve symlink
        yield os.path.relpath(os.path.realpath(name), start=dirname)
