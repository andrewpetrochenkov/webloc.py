[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/webloc.svg?longCache=True)](https://pypi.org/pypi/webloc/)
[![](https://img.shields.io/pypi/v/webloc.svg?maxAge=3600)](https://pypi.org/pypi/webloc/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/webloc.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/webloc.py/)

#### Install
```bash
$ [sudo] pip install webloc
```

#### Functions
function|description
-|-
`webloc.read(path)`|return webloc url
`webloc.write(path, url)`|write url to webloc file

#### CLI
usage|description
-|-
`python -m webloc [url]`|read/write webloc url

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

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>