"""
Smart User Symbols.

dd001pymdx.smartusersymbols
Really simple plugin to add support for user defined symbols

    Keep in mind that many symbols can be accessed via HTML5 entities:
    https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references

    Custom substitutions can be defined in various ways:

    - List of substitution pairs (most efficient)

        [
            ('<-', '←'),
            ('<=', '&leq;'),
            ('%%%', lambda s: ('MyStRiNg'+s).lower())
        ]

    - Dictionary (ensure unique keys)

        {
            '<-': '←',
            '<=': '&leq;',
            '%%%': lambda s: 'LaTeX'.lower()
        }

    - String with key/value pairs:

      Line syntax: "sss=c".
      Last "=" is used to split.
      Whitespace is *not* removed.
      Comment syntax: ";COMMENT".
      Empty lines are ignored.

      Example:

        <-=←
        <==&leq;

    The substitution can be any UTF-8 string or even a function.

    Additionally, there are pre-defined substitution lists
    - Named XHTML 1.0 entities
    - Named HTML5 entities (only non-ASCII)
    - Numbered HTML entities &#<NUM>; (only non-ASCII)

    Note: This plugin runs as a tree-processor meaning that HTML tags <tag prop="val"> are ignored!

MIT license.

Copyright (c) 2020 Marcel Schnirring

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
from markdown import treeprocessors
from markdown.util import Registry
from markdown.inlinepatterns import InlineProcessor

from .smartusersymbols_patterns import getSubstitutions, normalizeSubstitutions, formatPattern

REPL_ORDINALS = (
    "smart-ordinal-numbers",
    r'''(?x)
    \b
    (?P<leading>(?:[1-9][0-9]*)?)
    (?P<tail>(?<=1)(?:1|2|3)th|1st|2nd|3rd|[04-9]th)
    \b
    ''',
    lambda m: '%s%s<sup>%s</sup>' % (
        m.group('leading') if m.group('leading') else '',
        m.group('tail')[:-2], m.group('tail')[1:]
    ),
    30
)

REPL_NASCII = (
    "smart-html-ascii",
    r'[^\x00-\x7F]',
    lambda m: '&#{0};'.format(ord(m[0])),
    8
)

class SmartUserSymbolsPattern(InlineProcessor):
    """Smart User symbols patterns handler."""

    def __init__(self, pattern, replace, md):
        """Setup replace pattern."""

        super(SmartUserSymbolsPattern, self).__init__(pattern, md)
        self.replace = replace

    def handleMatch(self, m, data):
        """Replace symbol."""

        replace = self.replace(m)
        if callable(replace):
            replace = replace(m[m.lastindex])

        # NOTE store() is needed when new HTML tags are added (ORDINALS)
        return self.md.htmlStash.store(replace), m.start(0), m.end(0)


class SmartUserSymbolsExtension(Extension):
    """Smart User Symbols extension."""

    def __init__(self, *args, **kwargs):
        """Setup config with user symbols."""

        self.config = {
            'substitutions': [[], 'Substitution list'],
            'symbols': [True, 'Symbols'],
            'dice': [True, 'Dice'],
            'arrows': [True, 'Arrows'],
            'numbers': [True, 'Numbers in circles'],
            'fractions': [True, 'Fractions'],
            'math': [True, 'Math'],
            'roman': [True, 'Roman numbers'],
            'greek': [False, 'Greek letters'],
            'ordinal_numbers': [True, 'Ordinal Numbers'],
            'html_entities': [False, 'Replace named HTML entities'],
            'html5_entities': [False, 'Replace named HTML5 entities'],
            'html_unicode': [False, 'Replace Unicode characters by ASCII HTML entities']
        }
        super(SmartUserSymbolsExtension, self).__init__(*args, **kwargs)

    def addPattern(self, name, pattern, replace, prio, md):
        """Construct the inline symbol pattern."""

        self.patterns.register(SmartUserSymbolsPattern(pattern, replace, md), name, prio)

    def addSubstitutions(self, name, subs, prio, md):
        """Construct the inline symbol pattern."""

        self.addPattern(name, *formatPattern(subs),  prio, md)

    def extendMarkdown(self, md):
        """Create replace patterns and add to the tree processor."""

        configs = self.getConfigs()
        self.patterns = Registry()

        # User configured patterns
        if configs['substitutions']:  # if not empty
            self.addSubstitutions('smart-user', normalizeSubstitutions(configs['substitutions']), 100, md)

        # Pre-defined patterns
        for name in ['symbols', 'dice', 'arrows', 'numbers', 'fractions', 'math', 'roman', 'greek']:
            if configs[name]:
                self.addSubstitutions('smart-'+name, *getSubstitutions(name), md)
        # NOTE regex too complex to use direct replacement mechanism
        if configs['ordinal_numbers']:
            self.addPattern(*REPL_ORDINALS, md)

        # Named XHTML 1.0 Latin-1 entities (incl ASCII)
        if configs['html_entities']:
            self.addSubstitutions('smart-html', *getSubstitutions('html_entities'), md)
        # Named HTML5 Unicode entities (excl. ASCII)
        if configs['html5_entities']:
            self.addSubstitutions('smart-html5', *getSubstitutions('html5_entities'), md)
        # Numbered HTML entities (excl. ASCII)
        if configs['html_unicode']:
            self.addPattern(*REPL_NASCII, md)

        # NOTE InlineProcessor (TreeProcesser) does *not* process HTML tags: <tag prop="val" />
        inlineProcessor = treeprocessors.InlineProcessor(md)
        inlineProcessor.inlinePatterns = self.patterns
        md.treeprocessors.register(inlineProcessor, "smart-user-symbols", 2.1)


def makeExtension(*args, **kwargs):
    """Return extension."""

    return SmartUserSymbolsExtension(*args, **kwargs)
