import webbrowser
from offline_docs_py.dependencies import read_running_python_version_full

from offline_docs_py.paths import OUT_DIR


python_ver_full = read_running_python_version_full()
python_zip = OUT_DIR / f"python-{python_ver_full}-docs-html/index.html"

webbrowser.open(url=str(python_zip))
