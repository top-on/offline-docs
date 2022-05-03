# offline-docs

Quick access to Python library docs, cached for offline availability.


## Usage

```
$ offline-docs --help


Usage: offline-docs [OPTIONS] COMMAND [ARGS]...

  Quick access to Python library docs, cached for offline availability.

Options:
  --help  Show this message and exit.

Commands:
  clean   Remove all downloaded docs from local cache.
  python  Open docs for the current Python version in browser.
```


## Related Projects

An overview of similar projects, and how `office-docs` is different:

### Zeal

Mission statement, according to [zealdocs.org](https://zealdocs.org/):

> *Zeal is an offline documentation browser for software developers.*

Compared to zeal, `offline-docs`: 
* provides a command-line interface,
* shows docs in the system's default browser,
* matches the versions of docs to the installed versions.

## Roadmap

This section gives an outlook on how `offline-docs` could develop in the future. 

* Download docs from [readthedocs.org](https://readthedocs.org).
