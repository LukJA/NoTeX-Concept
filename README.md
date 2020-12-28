# NoTeX-Concept

NoTeX - I [like] TeX, but I want something better... This repo is a temporary store while I develop the concept.

See https://lukja.github.io/NoTeX-Concept/ for more details about the concept...

**DISCLAIMER** - I genuinely have not got a clue what I am doing, take all content as opinion without merit...

## Contributions

Contribution are welcome! I expect this project to be a sizable undertaking...

**Typos and Errors** - Open an Issue, or if you're feeling kind fix it and send in a pull request :smile:

**Feature Ideas** - Open an Issue tagged "Feature Request" with details

**Code Contributions** - Yet to begin, but get in touch!

### Useful Links

- https://towardsdatascience.com/creating-pdf-files-with-python-ad3ccadfae0f
- https://en.wikipedia.org/wiki/PDF
- https://www.reportlab.com/dev/opensource/pyrxp/
- https://pyfpdf.readthedocs.io/en/latest/index.html
- https://kivy.org/doc/stable/api-kivy.input.html

### Notes

- To speed up diagram drawings, positions could be aliased, and the aliases used to create lines and sketches much faster, and allow for multiple lines to be modified by moving a single point reference.

### pack_tutorial pip builds

N.B. all development is done in a local venv setup

```bash
python3 -m venv .

# Setuptools build:
python setup.py sdist bdist_wheel

# Twine upload:
python3 -m twine upload --repository testpypi dist/*

# Twine Download:
pip install -vvv --no-cache-dir --index-url https://test.pypi.org/simple/ --no-deps example-pkg-LukJA

# Symlinking module locally for development:
pip install -e .
# ~ then the integration tests can use the local raw dev files  ~

# to test:
pytest
```
