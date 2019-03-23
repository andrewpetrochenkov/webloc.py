#!/usr/bin/env python
"""read/write webloc url"""
import os
import plistlib
import public


@public.add
def read(path):
    """return webloc url"""
    if hasattr(plistlib, "load"):
        return plistlib.load(open(path, 'rb')).get("URL")
    return plistlib.readPlist(path).get("URL")


@public.add
def write(path, url):
    """write url to webloc file"""
    data = dict(URL=str(url))
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
    if hasattr(plistlib, "dump"):
        plistlib.dump(data, open(path, 'wb'))
    else:
        plistlib.writePlist(data, path)
