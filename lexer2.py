
#TO DO NEXT : GROUPING

import ply.lex as lex
import ply.yacc as yacc
import  sys



tokens=[
    'SIBLING',
    'R_ANGLE',
    'MULTIPLY',
    'L_CURLY',
    'R_CURLY',
    'CLIMB',
    'DOT',
    'HASH',

    'CLASS_NAME',
    'ID_NAME',
    'INT',
    "A",
    "DIV",
    "SPAN",
    "P",
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "UL",
    "LI",
    "TABLE",
    "TD",
    "TR",
    "IMG",
    "BR",


]
#
# t_DIV=r'\div'
t_SIBLING=r'\+'
t_R_ANGLE=r'\>'
t_MULTIPLY=r'\*'
t_L_CURLY=r'\{'
t_R_CURLY=r'\'
t_CLIMB=r'\'
t_DOT=r'\'
t_HASH=r'\'

# t_CLASS_NAME=r'\'
# t_ID_NAME=r'\'

t_A=r'\'
t_DIV=r'\'
t_SPAN=r'\'
t_P=r'\'
t_H1=r'\'
t_H2=r'\'
t_H3=r'\'
t_H4=r'\'
t_H5=r'\'
t_H6=r'\'
t_UL=r'\'
t_LI=r'\'
t_TABLE=r'\'
t_TD=r'\'
t_TR=r'\'
t_IMG=r'\'
t_BR=r'\'