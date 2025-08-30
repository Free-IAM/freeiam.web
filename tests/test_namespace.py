"""Namespace packaging smoke tests."""

import importlib


def test_web_import() -> None:
    """The public package can be imported."""
    assert importlib.import_module('freeiam.web') is not None


def test_namespace_parent() -> None:
    """Do not turn the shared freeiam namespace into a regular package."""
    freeiam = importlib.import_module('freeiam')
    assert freeiam.__spec__ is not None
    assert freeiam.__spec__.origin is None
    assert freeiam.__path__
