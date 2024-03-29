"""CLI entrypoint for app."""

import subprocess
import shutil
import zipfile

import typer
from urlpath import URL

from offline_docs.dependencies import (
    parse_major_minor,
    read_running_python_version_full,
)
from offline_docs.download import download
from offline_docs.paths import PYTHON_DIR, ROOT_DIR

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="Quick access to Python library docs, cached for offline availability.",
)


@app.command()
def python():
    """Open docs for the current Python version in browser."""
    # python version
    typer.echo("Infering running python version...")
    version_full = read_running_python_version_full()
    version_minor = parse_major_minor(major_minor_patch=version_full)

    # download docs
    url = URL(
        f"https://docs.python.org/{version_minor}/archives/python-{version_full}-docs-pdf-a4.zip"  # noqa: E501
    )
    target_dir = ROOT_DIR / "python"
    out_file = download(url=url, target_dir=target_dir)

    # extract
    python_version_dir = PYTHON_DIR / version_full
    python_pdf = python_version_dir / "docs-pdf/library.pdf"

    if python_pdf.exists():
        typer.echo("Found extracted docs. Skipping extraction.")
    else:
        typer.echo("Extracting docs (Python {version_patch})...")
        python_version_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(str(out_file), "r") as zip_ref:
            zip_ref.extractall(python_version_dir)

    # open docs
    subprocess.Popen(["xdg-open", python_pdf])


@app.command()
def clean():
    """Remove all downloaded docs from local cache."""
    typer.echo(f"Empyting folder {ROOT_DIR}...")
    if ROOT_DIR.exists():
        shutil.rmtree(str(ROOT_DIR))
    typer.echo("Done.")


def main():
    """Run CLI."""
    app()


if __name__ == "__main__":
    main()
