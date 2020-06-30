#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webloc

path = "/tmp/name.webloc"
url = "https://github.com"
webloc.write(path, url)
assert webloc.read(path) == url
