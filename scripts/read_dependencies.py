# %%
import toml
from pathlib import Path

PYPROJECT = Path("pyproject.toml")

# %% LOAD DEPENDENCIES

depencencies = (
    toml.load(PYPROJECT).get("tool").get("poetry").get("dependencies").items()
)

# %%
