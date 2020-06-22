# URI Converter Extension for Python-Markdown

An extension to covert tag URIs.

**NOTE** Convert paths to URIs needed for this extension via

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


## Usage

    markdown.markdown(some_text, extensions=[UriConverterExtension(option='value')])

or

    markdown.markdown(some_text, extensions=['uriconverter'], extension_configs={'uriconverter': {'option': 'value'}})

## Configuration

- `base`: Extend URIs with this base URI (use complete URI of current file) - _default: `""`_
- `replace`: List of search/replace URI pairs applied to the head of URI - _default: `[]`_
- `relative_base`: Make URIs relative to this URI (don't forget a trailing `/`!) - _default: `""`_
- `tags`: Tags to convert `src` and/or `href` attributes in - _default: `img scripts a link`_

