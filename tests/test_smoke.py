"""Smoke test: the package must import cleanly on a bare install."""
import importlib.metadata

import quiet_book_seeder


def test_package_imports():
    assert quiet_book_seeder is not None  # presence of the module is the contract


def test_package_has_version():
    assert importlib.metadata.version("quiet-book-seeder")
