# %%
import wget
import zipfile

from offline_docs_py.paths import OUT_DIR


URL = "https://docs.python.org/3.7/archives/python-3.7.12-docs-html.zip"
PYTHON_ZIP = OUT_DIR / "python-docs-html.zip"

# %% download
OUT_DIR.mkdir(parents=True, exist_ok=True)
wget.download(URL, out=str(PYTHON_ZIP))
# TODO: replace wget with e.g. requests


# %% unzip
with zipfile.ZipFile(PYTHON_ZIP, "r") as zip_ref:
    zip_ref.extractall(OUT_DIR)

# %%
