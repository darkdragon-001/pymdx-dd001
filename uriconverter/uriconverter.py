"""
Uri Converter.

uriconverter
An extension for Python Markdown.

An extension to covert tag URIs.

NOTE Convert paths to URIs needed for this extension via

    pathlib.Path(<PATH>).as_uri()


This extension supports the following operations:

Normalization
:   Remove irrelevant parts like "foo/../", "./", reduce multiple "//" into a single "/".

Base URI extension
:   Prepend URIs with a base URI (e.g. convert relative to absolute URIs).

Replacement
:   Replace search URI with replacement URI.

Relativation
:   Make URIs relative to a given URI.

MIT license.

Copyright (c) 2014 - 2017 Isaac Muse <isaacmuse@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
from markdown import Extension
from markdown.postprocessors import Postprocessor

import re

from urllib.parse import urljoin

RE_TAG_HTML = r'''(?xus)
    (?:
        (?P<comments>(\r?\n?\s*)<!--[\s\S]*?-->(\s*)(?=\r?\n)|<!--[\s\S]*?-->)|
        (?P<open><(?P<tag>(?:%s)))
        (?P<attr>(?:\s+[\w\-:]+(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s]+))?)*)
        (?P<close>\s*(?:\/?)>)
    )
    '''

RE_TAG_LINK_ATTR = re.compile(
    r'''(?xus)
    (?P<attr>
        (?:
            (?P<name>\s+(?:href|src)\s*=\s*)
            (?P<path>"[^"]*"|'[^']*'|[^\s]+)
        )
    )
    '''
)


def urlbase(base, uri):
    return urljoin(base, uri)  # prepend base

def urlreplace(search, replace, uri):
    if uri.startswith(search):
        uri = replace+uri[len(search):]
    return uri

def splitpath(uri):
    path, sep, file = uri.rpartition('/')
    return path+sep, file

def urlrelative(base, uri):
    base = splitpath(base)[0]  # remove filename
    uri, filename = splitpath(uri)

    if base.startswith(uri):  # base longer -> add "../"
        uri = base[len(uri):].count('/')*'../'
    elif uri.startswith(base):  # base shorter -> remove base from uri
        uri = uri[len(base):]

    return uri + filename


def repl_path(m, config):
    """Replace path with relative path."""

    link = m.group(0)

    try:
        uri = m.group('path').strip('"\'')  # optional quotation

        if not config['base']:
            config['base'] = '.'  # always normalize
        uri = urlbase(config['base'], uri)

        if config['replace']:
            for search, replace in config['replace']:
                uri = urlreplace(search, replace, uri)

        if config['relative_base']:
            uri = urlrelative(config['relative_base'], uri)

        link = '%s"%s"' % ( m.group('name'), uri )

    except Exception:  # pragma: no cover
        # Parsing crashed and burned; no need to continue.
        pass

    return link


def repl_tag(m, config):
    """Replace matched HTML tag."""

    if m.group('comments'):
        tag = m.group('comments')
    else:
        tag = m.group('open')
        tag += RE_TAG_LINK_ATTR.sub(lambda m2: repl_path(m2, config), m.group('attr'))
        tag += m.group('close')
    return tag


class UriConverterPostprocessor(Postprocessor):
    """Post process to find tag lings to convert."""

    def run(self, text):
        """Find and convert paths."""

        tags = re.compile(RE_TAG_HTML % '|'.join(self.config['tags'].split()))
        return tags.sub(lambda m: repl_tag(m, self.config), text)


class UriConverterExtension(Extension):
    """UriConverter extension."""

    def __init__(self, *args, **kwargs):
        """Initialize."""

        self.config = {
            'base': ["", "Extend URIs with this base URI (use complete URI of current file) - Default: \"\""],
            'replace': [[], "List of search/replace URI pairs applied to the head of URI - Default: []"],
            'relative_base': ["", "Make URIs relative to this URI (don't forget trailing \"/\"!) - Default: \"\""],
            'tags': ["img script a link", "Tags to convert \"src\" and/or \"href\" attributes in - Default: 'img scripts a link'"]
        }

        super(UriConverterExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        """Add post processor to Markdown instance."""

        rel_path = UriConverterPostprocessor(md)
        rel_path.config = self.getConfigs()
        md.postprocessors.register(rel_path, "uri-converter", 2)
        md.registerExtension(self)


def makeExtension(*args, **kwargs):
    """Return extension."""

    return UriConverterExtension(*args, **kwargs)
