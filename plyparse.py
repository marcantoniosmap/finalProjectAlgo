import ply.yacc as yacc
from plytoken import tokens
import sys

# grammars

def p_base(p):
    '''
    base :  expression 
         |  empty
    '''
    print(p[1]) # prints out expression the whole expression

# Nonterminal symbols (or syntactic variables) are replaced by groups of terminal symbols

# TODO unfinished non-terminal expressions
def p_expression_nonterminal(p):
    '''
    expression : expression R_ANGLE expression
               | expression SIBLING expression
    '''
    p[0] = (p[2], p[1], p[3])

# TODO temporary solution to ID tokens will change in the future
def p_expression_terminal(p):
    '''
    expression : DIV 
               | INT
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
    parser.parse(s)