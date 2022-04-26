"""CLI entrypoint for app."""

import shutil
import webbrowser
import zipfile

import typer
from urlpath import URL

from offline_docs.dependencies import (
    parse_major_minor,
    read_running_python_version_full,
)
from offline_docs.download import download
from offline_docs.paths import PYTHON_DIR, ROOT_DIR

app = typer.Typer(add_completion=False)


@app.command()
def python():
    """Download and show docs for the running version of Python."""
    # python version
    typer.echo("Infering running python version...")
    version_patch = read_running_python_version_full()
    version_minor = parse_major_minor(major_minor_patch=version_patch)

    # download docs
    url = URL(
        f"https://docs.python.org/{version_minor}/archives/python-{version_patch}-docs-html.zip"  # noqa: E501
    )
    target_dir = ROOT_DIR / "python"
    out_file = download(url=url, target_dir=target_dir)

    # extract
    python_version_dir = PYTHON_DIR / version_patch
    python_version_dir.mkdir(parents=True, exist_ok=True)
    python_html = python_version_dir / f"python-{version_patch}-docs-html/index.html"

    if python_html.exists():
        typer.echo("Found extracted docs. Skipping extraction.")
    else:
        typer.echo("Extracting docs (Python {version_patch})...")
        with zipfile.ZipFile(str(out_file), "r") as zip_ref:
            zip_ref.extractall(python_version_dir)

    # open docs
    webbrowser.open(url=str(python_html))


@app.command()
def clean():
    """Remove all downloaded docs from disc."""
    typer.echo(f"Empyting folder {ROOT_DIR}...")
    if ROOT_DIR.exists():
        shutil.rmtree(str(ROOT_DIR))
    typer.echo("Done.")


def main():
    """Run CLI."""
    app()


if __name__ == "__main__":
    main()
