<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/webloc.svg?longCache=True)](https://pypi.org/project/webloc/)
[![](https://img.shields.io/pypi/v/webloc.svg?maxAge=3600)](https://pypi.org/project/webloc/)
[![](https://img.shields.io/npm/v/webloc.svg?maxAge=3600)](https://www.npmjs.com/package/webloc)
[![Travis](https://api.travis-ci.org/looking-for-a-job/webloc.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/webloc.py/)

#### Installation
```bash
$ [sudo] npm i -g webloc
```
```bash
$ [sudo] pip install webloc
```

#### Functions
function|`__doc__`
-|-
`webloc.read(path)` |return webloc url
`webloc.write(path, url)` |write url to webloc file

#### Executable modules
usage|`__doc__`
-|-
`python -m webloc [url]` |read/write webloc url

#### Scripts usage
```bash
usage: webloc path [url]
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
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>