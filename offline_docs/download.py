"""Functions for downloading."""

from pathlib import Path

import wget
from urlpath import URL

from offline_docs.paths import CACHE_DIR


def download(url: Path) -> Path:
    """Download file, if not in cache yet.

    Args:
        url (URL): URL form where to download.

    Returns:
        Path: Path to cached download.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    out_file = CACHE_DIR / url.name

    if out_file.exists():
        print(f"Found {out_file.name}. Skipping download.")
    else:
        print(f"Downloading file {url.name}...")
        wget.download(url=str(url), out=str(out_file))
        print("")

    return out_file
