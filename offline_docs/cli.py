"""CLI entrypoint for app."""

import shutil
import webbrowser
import zipfile
from typing import Optional

import typer
import wget

from offline_docs.dependencies import (
    parse_major_minor,
    read_running_python_version_full,
)
from offline_docs.paths import PYTHON_DIR, CACHE_DIR, ROOT_DIR

app = typer.Typer(add_completion=False)


@app.command()
def python():
    """Download and show docs for the running version of Python."""
    # python version
    typer.echo(f"Infering running python version...")
    version_patch = read_running_python_version_full()
    version_minor = parse_major_minor(major_minor_patch=version_patch)

    # download docs
    url = f"https://docs.python.org/{version_minor}/archives/python-{version_patch}-docs-html.zip"
    python_zip_path = CACHE_DIR / f"python-{version_patch}-docs-html.zip"
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    typer.echo(f"Downloading docs (Python {version_patch})...")
    wget.download(url, out=str(python_zip_path))  # TODO: use requests, with caching

    # extract
    python_version_dir = PYTHON_DIR / version_patch
    python_version_dir.mkdir(parents=True, exist_ok=True)

    typer.echo(f"Extracting docs (Python {version_patch})...")
    # TODO: only extract if target folder does not exist
    with zipfile.ZipFile(python_zip_path, "r") as zip_ref:
        zip_ref.extractall(python_version_dir)

    # open
    python_html = python_version_dir / f"python-{version_patch}-docs-html/index.html"
    webbrowser.open(url=str(python_html))


@app.command()
def clean():
    """Remove all downloaded docs from disc."""
    typer.echo(f"Removing all downloads...")
    if ROOT_DIR.exists():
        shutil.rmtree(str(ROOT_DIR))
    typer.echo(f"Done.")


def main():
    """Run CLI."""
    app()


if __name__ == "__main__":
    main()
