import webbrowser

from offline_docs_py.paths import OUT_DIR

PYTHON_ZIP = OUT_DIR / "python-3.7.12-docs-html/index.html"

webbrowser.open(url=str(PYTHON_ZIP))
