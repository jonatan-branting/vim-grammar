from dragonfly import Choice

def letterChoice(name="letter"):
    return Choice(name, {
        'arch': 'a',
        'brov': 'b',
        'char': 'c',
        'delta': 'd',
        'echo': 'e',
        'foxy': 'f',
        'goof': 'g',
        'hotel': 'h',
        'india': 'i',
        'julia': 'j',
        'kilo': 'k',
        'lima': 'l',
        'mike': 'm',
        'novakeen': 'n',
        'oscar': 'o',
        'prime': 'p',
        'quebec': 'q',
        'romeo': 'r',
        'sierra': 's',
        'tango': 't',
        'uniform': 'u',
        'victor': 'v',
        'whiskey': 'w',
        'x-ray': 'x',
        'yankee': 'y',
        'zulu': 'z',

        'upper arch': 'A',
        'upper brov': 'B',
        'upper char': 'C',
        'upper delta': 'D',
        'upper echo': 'E',
        'upper foxy': 'F',
        'upper goof': 'G',
        'upper hotel': 'H',
        'upper india': 'I',
        'upper julia': 'J',
        'upper kilo': 'K',
        'upper lima': 'L',
        'upper mike': 'M',
        'upper novakeen': 'N',
        'upper oscar': 'O',
        'upper prime': 'P',
        'upper quebec': 'Q',
        'upper romeo': 'R',
        'upper sierra': 'S',
        'upper tango': 'T',
        'upper uniform': 'U',
        'upper victor': 'V',
        'upper whiskey': 'W',
        'upper x-ray': 'X',
        'upper yankee': 'Y',
        'upper zulu': 'Z',

        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',

        'ace': 'space',
        'tabby': 'tab',

        'ampersand': 'ampersand',
        '(apostrophe | post)': 'apostrophe',
        'single quote': 'squote',
        '(asterisk | starling)': 'asterisk',
        'at': 'at',
        'backslash': 'backslash',
        'backtick': 'backtick',
        'pipe': 'bar',
        'caret': 'caret',
        'deckle': 'colon',
        'boom': 'comma',
        'dollar': 'dollar',
        '(dot|period)': 'dot',
        'quote': 'dquote',
        'equal': 'equal',
        'clamor': 'exclamation',
        'hashtag': 'hash',
        'hyphen': 'hyphen',
        'minus': 'minus',
        'modulo': 'percent',
        'plus': 'plus',
        'questo': 'question',
        'semper': 'semicolon',
        'slash': 'slash',
        'tilde': 'tilde',
        '(underscore | score)': 'underscore',

        'langle': 'langle',
        'lace': 'lbrace',
        'lack': 'lbracket',
        'laip': 'lparen',
        'rangle': 'rangle',
        'race': 'rbrace',
        'rack': 'rbracket',
        'raip': 'rparen',
        })
