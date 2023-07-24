from setuptools.build_meta import *  # noqa

# intentionally left blank


def __getattr__(name):
    print(name)
    if name == "version":
        return "0.0.0"  # FIXME
    raise AttributeError(name)
