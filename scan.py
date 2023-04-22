import sys
from globall import TokenType as tp
from globall import lineno
from enum import Enum

bufsize = 0
MaxTokenLen = 40
TokenString = list()
linea = str()
MAXBUFFER = 1024
namefile = sys.argv[1]
source = open(namefile,'r')
colpos = 0
reservedWords ={
    'MAIN':tp.MAIN,
    'IF':tp.IF,
    'THEN':tp.THEN,
    'ELSE':tp.ELSE,
    'END':tp.END,
    'DO':tp.DO,
    'WHILE':tp.WHILE,
    'REPEAT':tp.REPEAT,
    'UNTIL':tp.UNTIL,
    'CIN':tp.CIN,
    'COUT':tp.COUT,
    'REAL':tp.REAL,
    'INT':tp.REAL,
    'BOOLEAN':tp.BOOLEAN


} 

class States(Enum):
    INICIO = 0
    EMENOS = 1
    EMMENOS = 2
    EMAS = 3
    EMMAS = 4
    EENTEROS = 5
    EPREAL = 6
    EREAL = 7
    EID = 8
    EASIGNA = 9
    EPCOMM = 10
    ECOMMSIMPLE = 11
    EPCOMMMULTI = 12
    ECOMMMULTI = 13
    EMAYOR = 14
    EMAYORIGUAL = 15
    EMENOR = 16
    EMENORIGUAL = 17
    EDIFERENTE = 18
    HECHO = 19
    
def getNextChar():
    if( not(colpos < bufsize) ):
        linea = source.readline()
        if not linea:
            lineno+=1
            bufsize = len(linea)
            colpos = 0
            char = linea[colpos]
            return char
        else:
            return tp.ENDFILE    
    else:
        char = linea[colpos]
        colpos+=1
        return char
        
def ungetChar():
    colpos-=1

def isReservedWord(tokenString:str)->tp:
    for key in reservedWords.keys():
        if(reservedWords[key] == tokenString):
            return reservedWords[key]

    return tp.ID    

def getToken()->tp:

    tokenStringIndex = 0
    currentToken:tp
    state:States
    while state != States.HECHO:
        c = getNextChar()
        if state == States.INICIO:
            if c.isdigit():
                state = States.EENTEROS
            elif c.isalnum() or c == "_":
                state = States.EID
            elif c == ":":
                state = States.EASIGNA
            elif c == "+":
                state = States.EMAS
            elif c == "-":
                state = States.EMENOS
                