#!/usr/bin/env python
"""read/write webloc url"""
import click
import webloc


@click.command()
@click.argument('path')
@click.argument('url', required=False)
def _cli(path, url=None):
    if not url:
        url = webloc.read(path)
        if url:
            print(url)
    else:
        webloc.write(path, url)


MODULE_NAME = "webloc"
USAGE = 'python -m %s [url]' % MODULE_NAME
PROG_NAME = 'python -m %s' % MODULE_NAME


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
