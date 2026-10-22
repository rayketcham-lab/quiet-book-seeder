"""Smoke test: the package must import cleanly on a bare install."""
import quiet_book_seeder


def test_package_imports():
    assert quiet_book_seeder.__doc__ or True  # presence of the module is the contract


def test_package_has_version():
    import importlib.metadata

    assert importlib.metadata.version("quiet-book-seeder")
