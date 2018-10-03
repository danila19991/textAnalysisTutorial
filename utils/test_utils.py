from utils.version import version
import pytest


def test_correct_version():
    assert version() > 0


def test_incorrect_test():
    assert version() == 1
