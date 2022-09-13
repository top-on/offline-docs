"""Read dependencies."""

import sys


def read_running_python_version_full() -> str:
    """Look up full version of executed Python.

    Returns:
        str: Python version, e.g. '3.10.7'.
    """
    major_minor_patch = sys.version.split(" ")[0]
    return major_minor_patch


def parse_major_minor(major_minor_patch: str) -> str:
    """Extract MAJOR and MINOR part from version in SemVer format.

    Args:
        major_minor_patch (str): Input in MAJOR.MINOR.PATCH format, e.g. '3.10.7'.

    Returns:
        str: Returns MAJOR.MINOR, e.g. '3.10'.
    """
    return major_minor_patch.split(".")[0] + "." + major_minor_patch.split(".")[1]
