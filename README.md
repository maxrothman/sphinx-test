# Sphinx Testing

This repo contains some basic stuff to play around with Sphinx, e.g. directives, plugins, etc.

## What's here?

- `code` is in Sphinx's `PYTHONPATH`, so it can import things from there (whether to document them, like `test.py` or to use them, like `directives.py`)
- `docs` is the Sphinx root directory
- `_static` and `_templates` are used for Sphinx's `html_static_path` and `templates_path`, respectively
- `example-dom.xml` is an xml-ified doctree of a file in `code`
- `ideal.rst` was generated by autodoc from `code/test.py`