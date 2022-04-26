"""Functional tests of CLI."""


from offline_docs.cli import clean, python


def test_python():
    """Run 'python' command of CLI."""
    python()


def test_clean():
    """Run 'clean' command of CLI."""
    clean()
