
""" Substitution definitions. """

SUBSTITUTIONS = {}
SUBSTITUTIONS['symbols'] = ([
    (r'(tm)', r'&trade;'),
    (r'(c)', r'&copy;'),
    (r'(r)', r'&reg;'),
    (r'+/-', r'&plusmn;'),
    (r'=/=', r'&ne;'),
    (r'c/o', r'&#8453;'),
    (r'\check', r'&check;'),
    (r'\yes', r'&check;'),
    (r'\no', r'&cross;'),
    (r'N(o)', r'&numero;'),
], 100)
SUBSTITUTIONS['dice']=("""
|1|=⚀
|2|=⚁
|3|=⚂
|4|=⚃
|5|=⚄
|6|=⚅
""", 90)
# TODO search for missing arrows in unicode directly
SUBSTITUTIONS['arrows'] = ({
    # right
    '->': "&rarr;",
    '-->': "&xrarr;",
    '>->': "&rarrtl;",  # tail
    '|->': "&mapsto;",
    '->|': "&rarrb;",  # bar
    'o->': "&rarrlp;",  # loop
    '~>': "&rarrw;",  # squig
    '->>': "&Rarr;",
    '=>': "&rArr;",
    '==>': "&xrArr;",
    # left
    '<-': "&larr;",
    '<--': "&xlarr;",
    '<-<': "&larrtl;",  # tail
    '<-|': "&mapstoleft;",
    '|<-': "&larrb;",  # bar
    '<-o': "&larrlp;",  # loop
    #'<~': "&larrw;",  # squig; doesn't exist :(
    '<<-': "&Larr;",
    '<==': "&xlArr;",
    #'<=': "&lArr;",  # also used for less or equal  # TODO why are priorities not working!?
    # horizontal
    '<->': "&harr;",
    '<-->': "&xharr;",
    '<~>': "&harrw;",  # squig
    '<=>': "&hArr;",
    '<==>': "&xhArr;",
    # up
    '|^': "&uarr;",
    '||^': "&uArr;",
    '|^-': "&UpArrowBar;",
    '-|^': "&UpTeeArrow;",
    # down
    '|v': "&darr;",
    '||v': "&dArr;",
    '|v-': "&DownArrowBar;",
    '-|v': "&DownTeeArrow;",
    # vertical
    'v|^': "&varr;",
    '^|v': "&varr;",
    'v||^': "&vArr;",
    '^||v': "&vArr;",
    # diagonal
    '\\>': "&searr;", # south-east
    '\\v': "&searr;",
    '\\\\>': "&seArr;",
    '\\\\v': "&seArr;",
    '</': "&swarr;", # south-west
    'v/': "&swarr;",
    '<//': "&swArr;",
    'v//': "&swArr;",
    '/>': "&nearr;", # north-east
    '/^': "&nearr;",
    '//>': "&neArr;",
    '//^': "&neArr;",
    '<\\': "&nwarr;", # north-west
    '^\\': "&nwarr;",
    '<\\\\': "&nwArr;",
    '^\\\\': "&nwArr;",
    # circle
    '<o': "&circlearrowleft;",
    'o>': "&circlearrowright;",
    # TODO two arrows in single glyph
    #'->->': "&rightrightarrows;",  # two right
}, 95)
SUBSTITUTIONS['numbers']=("""
(1)=❶
(2)=❷
(3)=❸
(4)=❹
(5)=❺
(6)=❻
(7)=❼
(8)=❽
(9)=❾
(10)=❿
((1))=➀
((2))=➁
((3))=➂
((4))=➃
((5))=➄
((6))=➅
((7))=➆
((8))=➇
((9))=➈
((10))=➉
""", 91)
SUBSTITUTIONS['fractions'] = ({
    "1/2": "&frac12;",
    "1/3": "&#8531;",
    "2/3": "&#8532;",
    "1/4": "&frac14;",
    "3/4": "&frac34;",
    "1/5": "&#8533;",
    "2/5": "&#8534;",
    "3/5": "&#8535;",
    "4/5": "&#8536;",
    "1/6": "&#8537;",
    "5/6": "&#8538;",
    "1/7": "&#8528;",
    "1/8": "&#8539;",
    "3/8": "&#8540;",
    "5/8": "&#8541;",
    "7/8": "&#8542;",
    "1/9": "&#8529;",
    "1/10": "&#8530;"
}, 93)
SUBSTITUTIONS['math']=("""
\\cdot=·
\\div=÷
+-=±
-+=∓
<==≤
>==≥
>>=»
<<=«
~~=≈
===≡
!==≠
<>=≠
^==≙
o/=ø
O/=Ø
\\sub=⊂
\\sup=⊃
\\sube=⊆
\\supe=⊇
!!=¬
&&=∧
||=v
\\exist=∃
\\all=∀
\\ele=∈
\\nele=∉
\\sqrt=√
\\3sqrt=∛
\\4sqrt=∜
\\sum=∑
\\prod=∏
\\diff=∂
\\int=∫
\\cint=∮
\\-/=∇
/-\\=Δ
<)=∡
\\8=∞
\\inf=∞
""", 96)
# TODO wrap inside serif type font
SUBSTITUTIONS['roman'] = ("""
(i)=Ⅰ
(ii)=Ⅱ
(iii)=Ⅲ
(iv)=Ⅳ
(v)=Ⅴ
(vi)=Ⅵ
(vii)=Ⅶ
(viii)=Ⅷ
(ix)=Ⅸ
(x)=Ⅹ
(xi)=Ⅺ
(xii)=Ⅻ
""", 89)
# NOTE can also be accessed via "&letter;"
SUBSTITUTIONS['greek']=("""
\\alpha=α
\\beta=β
\\gamma=γ
\\delta=δ
\\epsilon=ε
\\zeta=ζ
\\eta=η
\\theta=ϑ
\\thetav=θ
\\iota=ι
\\kappa=κ
\\lambda=λ
\\mu=μ
\\nu=ν
\\xi=ξ
\\omicron=ο
\\pi=π
\\rho=ρ
\\sigma=σ
\\sigmav=ς
\\tau=τ
\\upsilon=υ
\\phi=φ
\\chi=χ
\\psi=ψ
\\omega=ω
\\Alpha=Α
\\Beta=Β
\\Gamma=Γ
\\Delta=Δ
\\Epsilon=Ε
\\Zeta=Ζ
\\Eta=Η
\\Theta=Θ
\\Iota=Ι
\\Kappa=Κ
\\Lambda=Λ
\\Mu=Μ
\\Nu=Ν
\\Xi=Ξ
\\Omicron=Ο
\\Pi=Π
\\Rho=Ρ
\\Sigma=Σ
\\Tau=Τ
\\Upsilon=Υ
\\Phi=Φ
\\Chi=Χ
\\Psi=Ψ
\\Omega=Ω
""", 88)


""" HTML entities functions. """

import html

# Named XHTML 1.0 Latin-1 entities incl ASCII: 34" 38& 60< 62>
HTML_ENTITY_UNICODE = [(u,'&'+n+';') for n,u in html.entities.entitydefs.items()]
SUBSTITUTIONS['html_entities'] = (
    HTML_ENTITY_UNICODE,
    10
)

# Named HTML5 Unicode entities excl. ASCII: 9\t 10\n 33! 34" 35# 36$ 37% 38& 39' 40( 41) 42* 43+ 44, 46. 47/ 58: 59; 60< 61= 62> 63? 64@ 91[ 92\ 93] 94^ 95_ 96` 123{ 124| 125}
# -> some special characters like ':', '\n' are needed for the binary representation used by treeprocessor
HTML5_ENTITY_UNICODE = dict()
for namedChar,unicodeChar in html.entities.html5.items():
    isAscii = lambda c: len(c) == 1 and ord(c) < 128  # some Unicode characters consist of two Unicode ordinals
    if not isAscii(unicodeChar):
        namedChar = '&' + namedChar + ( ';' if namedChar[-1]!=';' else '' )  # BUG https://github.com/Python-Markdown/markdown/issues/952
        if unicodeChar not in HTML5_ENTITY_UNICODE or len(namedChar) < len(HTML5_ENTITY_UNICODE[unicodeChar]):  # prefer shortest entity
            HTML5_ENTITY_UNICODE[unicodeChar] = namedChar
SUBSTITUTIONS['html5_entities'] = (
    HTML5_ENTITY_UNICODE,
    9
)


""" Substitutions handling functions. """

import re

def parseSubstitutions(subs):
    newSubs = dict()
    for line in subs.splitlines():
        if line and line[0] != ';':
            char = line.rsplit('=', 1)
            if len(char) > 1:
                newSubs[char[0]] = char[1]
    return newSubs

def escapeSubstitutions(subs):
    newSubs = []
    for k,v in subs:
        # replace non-ASCII with HTML entity
        if len(v) == 1 and ord(v) > 127:
            if v in HTML5_ENTITY_UNICODE:  # prefer human-readable name
                v = HTML5_ENTITY_UNICODE[v]
            else:
                v = '&#{0};'.format(ord(v))
        newSubs.append((k,v))
    return newSubs

def normalizeSubstitutions(subs, escape=True):
    if isinstance(subs, str):
        subs = parseSubstitutions(subs)
    if isinstance(subs, dict):
        subs = subs.items()
    if escape:
        subs = escapeSubstitutions(subs)
    return subs

# store all default substitutions in normalized form
for name, subInfo in SUBSTITUTIONS.items():
    SUBSTITUTIONS[name] = ( normalizeSubstitutions(subInfo[0]), subInfo[1] )

def getSubstitutions(name):
    return SUBSTITUTIONS[name]  # NOTE expect them to be normalized on declaration for speed

def formatPattern(subs):
    pattern = '|'.join('(%s)' % re.escape(p) for p, s in subs)
    substs = [s for p, s in subs]
    replace = lambda m: substs[m.lastindex - 1]
    return pattern, replace


""" List all default substitutions for documentation. """

def get_default_substitutions_table():
    res = ''
    for name in ['symbols', 'dice', 'arrows', 'numbers', 'fractions', 'math', 'roman', 'greek']:
        res += '|%s||\n' % name
        res += '|-|-|\n'
        for s in getSubstitutions(name)[0]:
            res += "| `%s` | %s |\n" % s
        res += '\n'
    return res

if __name__ == "__main__":
    print(get_default_substitutions_table())
