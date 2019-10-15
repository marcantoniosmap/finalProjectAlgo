# TODO multiplication, grouping, attribute operatos(ID, CLASS, item numbering), test {} 
# https://docs.emmet.io/abbreviations/syntax/

# import markuPy.Modules.ply.yacc as yacc
# from .plytokenCopy import tokens
import sys

import ply.yacc as yacc
from run_file import *
from plytokenCopy import tokens


# grammars

def p_base(p):
    '''
    base :  expression 
         |  empty
    '''
    p[0] = p[1] # moved the print to the main loop

# Nonterminal symbols (or syntactic variables) are replaced by groups of terminal symbols

def p_special(p):
    '''
    expression : expression MULTIPLY INT R_ANGLE expression
    '''
    p[0]= (p[2],(p[4],p[1],p[5]),p[3])



def p_expression_nonterminal(p):
    '''
    expression : expression R_ANGLE expression
               | expression SIBLING expression
               | expression CLIMB expression

               | expression DOT string
               | expression HASH string
               | expression CONTENT string

               | expression MULTIPLY INT
    '''
    p[0] = (p[2], p[1], p[3])

def p_grouping(p):
    '''
    expression : L_PAREN expression R_PAREN
    '''
    p[0]=p[2]

def p_temp(p):
    '''
    expression : NAME
    '''
    p[0] = p[1]

def p_string(p):
    '''
    string : CONTENT_STRING
            | STRING
    '''
    p[0]=p[1]

# TODO temporary solution to ID tokens will change in the future
def p_expression_terminal(p):
    '''
    NAME : DIV
        | SPAN
        | P
        | H1
        | H2
        | H3
        | H4
        | H5
        | H6
        | UL
        | LI
        | TABLE
        | TD
        | TR
        | IMG
        | BR
    '''
    p[0] = p[1]


def p_empty(p):
    '''
    empty :
    '''
    pass

# TODO 
def p_error(p):
    pass

parser = yacc.yacc()

while True:
    try:
        s = input(">> ")
    except EOFError:
        break # ctrl + D ends the program
    if not s: continue
    result = parser.parse(s)

    # print(result)

    final = run(result)
    print(final)