
#TO DO NEXT : GROUPING

# import markuPy.Modules.ply.lex as lex
# import sys

import ply.lex as lex

states = (
    ('getString','inclusive'),
    ('content','inclusive')
 )

tokens = [
    'R_ANGLE',
    'SIBLING',
    'MULTIPLY',
    'L_PAREN',
    'R_PAREN',
    'CONTENT',
    'R_CURLY',
    'CLIMB',
    'DOT',
    'HASH',
    'INT',
    'STRING',
    'CONTENT_STRING',
]

reserved={
    'div': 'DIV',
    'span' : 'SPAN',
    'p' : 'P',
    'h1' : 'H1',
    'h2' : 'H2',
    'h3' : 'H3',
    'h4' : 'H4',
    'h5' : 'H5',
    'h6' : 'H6',
    "ul" : "UL",
    "li" : "LI",
    "table" : "TABLE",
    "td" : "TD",
    "tr" : "TR",
    "img" : "IMG",
    "br" : "BR"
}


tokens += reserved.values()

t_ignore=r' '

t_R_ANGLE=r'\>'
t_SIBLING=r'\+'
t_MULTIPLY=r'\*'
t_L_PAREN=r'\('
t_R_PAREN=r'\)'
# t_L_CURLY=r'\{'
# t_R_CURLY=r'\}'
t_CLIMB=r'\^'
# t_DOT=r'\.'
# t_HASH=r'\#'

def t_HASH(t):
    r'\#'
    t.lexer.begin('getString')
    return t

def t_DOT(t):
    r'\.'
    t.lexer.begin('getString')
    return t

def t_CONTENT(t):
    r'\{'
    t.lexer.begin('content')
    return t

def t_content_CONTENT_STRING(t):
    r'[a-zA-Z][ a-zA-Z0-9]*'
    return t

def t_content_R_CULRLY(t):
    r'\}'
    t.lexer.begin('INITIAL')


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type=reserved.get(t.value,'ID')
    if t.type == 'ID':
        return t_error(t)
    return t

def t_getString_STRING(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.lexer.begin('INITIAL')
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print('ERROR OCCURED ON :',t.lexpos)
    t.lexer.skip(1)


lexer=lex.lex()

# while True:
#     s=input(">> ")
#     lexer.input(s)
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break
#         print(tok)

# while True:
#     s=input(">> ")
#     lexer.input(s)
#     tok = lexer.token()
#     print(tok)
