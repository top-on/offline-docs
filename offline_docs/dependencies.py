"""Read dependencies."""

import sys


def read_running_python_version_full() -> str:
    major_minor_patch = sys.version.split(" ")[0]
    return major_minor_patch


def parse_major_minor(major_minor_patch: str) -> str:
    return major_minor_patch.split(".")[0] + "." + major_minor_patch.split(".")[1]
