from offline_docs.dependencies import (
    min_python_version,
    parse_major_minor,
)


def test_min_python_version():
    dependencies = {"python": "^3.8"}

    result = min_python_version(dependencies=dependencies)

    assert result == "3.8"


def test_extract_major_minor():

    assert parse_major_minor("3.8.12") == "3.8"
