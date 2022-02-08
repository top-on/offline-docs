# %%
import zipfile

import wget

from offline_docs.dependencies import (
    parse_major_minor,
    read_running_python_version_full,
)
from offline_docs.paths import OUT_DIR

# %%
python_ver_full = read_running_python_version_full()
python_ver_major_minor = parse_major_minor(major_minor_patch=python_ver_full)
URL = f"https://docs.python.org/{python_ver_major_minor}/archives/python-{python_ver_full}-docs-html.zip"
PYTHON_ZIP = OUT_DIR / f"python-{python_ver_full}-docs-html.zip"

# %% download
OUT_DIR.mkdir(parents=True, exist_ok=True)
wget.download(URL, out=str(PYTHON_ZIP))
# TODO: replace wget with e.g. requests


# %% unzip
with zipfile.ZipFile(PYTHON_ZIP, "r") as zip_ref:
    zip_ref.extractall(OUT_DIR)

# %%
