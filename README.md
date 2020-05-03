# Smart User Symbols Extension for Python-Markdown

## Installation

    pip3 install .
    
## Usage

    markdown.markdown(some_text, extensions=[SmartUserSymbolsExtension(option='value')])

or

    markdown.markdown(some_text, extensions=['smartusersymbols'], extension_configs={'smartusersymbols': {'option': 'value'}})

## Configuration

### Default substitutions

- `symbols`: Symbols _(default: `True`)_
- `dice`: Dice _(default: `True`)_
- `arrows`: Arrows _(default: `True`)_
- `numbers`: Numbers in circles _(default: `True`)_
- `fractions`: Fractions _(default: `True`)_
- `math`: Math _(default: `True`)_
- `roman`: Roman numbers _(default: `True`)_
- `greek`: Greek letters _(default: `False`)_
- `ordinal_numbers`: Ordinal Numbers _(default: `True`)_

### User substiutions

**Option name:** `substitutions`

**Format:** Three different possibilities

- List of substitution pairs (most efficient)

      [
          ('<-', '←'),
          ('<=', '&leq;'),
          ('%%%', lambda s: 'LaTeX'.lower())
      ]

- Dictionary (ensure unique keys)

      {
          '<-': '←',
          '<=': '&leq;',
          '%%%': lambda s: ('MyStRiNg'+s).lower()
      }

- String with key/value pairs:

    - Line syntax: `sss=c`.
    - Last `=` is used to split.
    - Whitespace is *not* removed.
    - Comment syntax: `;COMMENT`.
    - Empty lines are ignored.

          """
          <-=←
          <==&leq;
          """


## Documentation

Generate tables with all default symbol definitions

    python3 ./smartusersymbols/smartusersymbols_patterns.py > tab.md
