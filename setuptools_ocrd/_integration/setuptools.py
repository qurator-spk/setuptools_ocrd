import logging
import warnings
import setuptools
from setuptools_ocrd import _get_version


log = logging.getLogger(__name__)


def _warn_on_old_setuptools(_version = setuptools.__version__):
    if int(_version.split(".")[0]) < 61:
        warnings.warn(RuntimeWarning(f"setuptools=={_version} is old!"))

_warn_on_old_setuptools()

def infer_version(dist):
    log.debug("infer_version: %r", vars(dist.metadata))

    if dist.metadata.version is not None:
        return

    if dist.metadata.name == "setuptools_ocrd":
        return

    dist.metadata.version = _get_version()
