"""Test functions for infering dependency versions."""

import re

from offline_docs.dependencies import (
    parse_major_minor,
    read_running_python_version_full,
)


def test_read_running_python_version_full():

    python_version = read_running_python_version_full()

    regex = r"[23].\d+.\d+"
    assert re.match(regex, python_version), "Python version not does not match pattern."


def test_extract_major_minor():

    assert parse_major_minor("3.8.12") == "3.8"
