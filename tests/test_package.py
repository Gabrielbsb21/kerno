from importlib.machinery import EXTENSION_SUFFIXES
from importlib.metadata import version
from importlib.resources import files

import kerno
from kerno import _core


def test_core_is_a_native_extension():
    assert _core.__file__ is not None
    assert _core.__file__.endswith(tuple(EXTENSION_SUFFIXES))


def test_version_matches_native_module_and_distribution():
    assert isinstance(kerno.__version__, str)
    assert kerno.__version__ == _core.__version__ == version("kerno")


def test_package_includes_type_information():
    package = files("kerno")
    assert package.joinpath("py.typed").is_file()
    assert package.joinpath("_core.pyi").is_file()
