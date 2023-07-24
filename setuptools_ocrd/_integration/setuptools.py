import logging
from setuptools_ocrd import _get_version


log = logging.getLogger(__name__)

def infer_version(dist):
    log.debug("infer_version: %r", vars(dist.metadata))

    if dist.metadata.version is not None:
        return

    if dist.metadata.name == "setuptools_ocrd":
        return

    dist.metadata.version = _get_version()
