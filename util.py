from globall import TokenType as tp


def printToken(token,tokenString):
    if ((tp.MAIN or tp.IF or tp.THEN or tp.ELSE
    or tp.END or tp.DO or tp.WHILE or tp.REPEAT
    or tp.UNTIL or tp.CIN or tp.COUT or tp.REAL
    or tp.INT or tp.BOOLEAN) == token) :
        print ( "RESERVED WORD {0}".format(tokenString) )
    elif ( tp.PLUS == token ):
        print( "+" )
    elif ( tp.MINUS == token ):
        print( "-" ) 
    elif ( tp.TIMES == token ):
        print( "*" )
    elif ( tp.OVER == token ):
        print( "/" )
    elif ( tp.RES == token ):
        print( "%" )
    elif ( tp.LESST == token ):
        print( "<" )
    elif ( tp.LESSET == token ):
        print( "<=" )
    elif ( tp.GREATERT == token ):
        print( ">" )
    elif ( tp.GREATERET == token ):
        print( ">=" )
    elif ( tp.EQ == token ):
        print( "=" )
    elif ( tp.DIFF == token ):
        print( "<>" )        
    elif( token == tp.ASSIGN):
        print ( ":=" )
    elif ( tp.LPAREN == token ):
        print( "(" )
    elif ( tp.RPAREN == token ):
        print( ")" )
    elif ( tp.LBPAREN == token ):
        print( "{" )
    elif ( tp.RBPAREN == token ):
        print( "}" )
    elif ( tp.PLUSP == token ):
        print( "++" )
    elif ( tp.LESSL == token ):
        print( "--" )
    elif ( tp.COMMA == token ):
        print( "," )
    elif ( tp.SEMMICOL == token ):
        print( ";" )
    elif ( tp.ID == token ):
        print( "ID, NAME: {}".format(tokenString) )
    elif ( tp.ENTERO == token ):
        print( "ENTERO, VALUE: {}".format(tokenString) )
    elif ( tp.NUMREAL == token ):
        print( "REAL, VALUE: {}".format(tokenString) )
    elif ( tp.ENDFILE == token ):
        print( "EOF" )
    elif ( tp.ERROR == token ):
        print( "ERROR: {}".format(tokenString) )
    else:
        print("UNKNOWN TOKEN: {}".format(tokenString))
    
    
    
    
            
    