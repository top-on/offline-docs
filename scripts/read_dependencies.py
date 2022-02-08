# %%
from pathlib import Path

from offline_docs.dependencies import read_dependencies_poetry


PYPROJECT = Path("pyproject.toml")

# %% LOAD DEPENDENCIES

depencencies = read_dependencies_poetry(PYPROJECT)

# %%
