<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/webloc.svg?maxAge=3600)](https://pypi.org/project/webloc/)
[![](https://img.shields.io/npm/v/webloc.svg?maxAge=3600)](https://www.npmjs.com/package/webloc)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/webloc.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/webloc.py/actions)

### Installation
```bash
$ [sudo] pip install webloc
```

```bash
$ [sudo] npm i -g webloc
```

#### Examples
```python
>>> import webloc
>>> webloc.write("path.webloc","https://www.google.com/")
>>> webloc.read("path.webloc")
'https://www.google.com/'
```

```bash
$ python -m webloc "path.webloc" "https://www.github.com/"
$ python -m webloc "path.webloc"
https://www.github.com/
```

```bash
$ webloc file.webloc https://github.com/
$ webloc file.webloc
https://github.com/
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
