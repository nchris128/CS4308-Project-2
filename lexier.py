
from genericpath import exists
from tempfile import TemporaryFile
import scl_scanner


lexemeList = []
lexeme = ''
nextToken = ''
nextChar = ''
#Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99

#Token codes
INT_LIT = 10
IDENT = 11
FLOAT = 12
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

operatorTable = [ '=', '*', '/', '(', ')', '[]', '<=', '>=', ':']

def parsefilename():
    global nextToken
    file = scl_scanner.cleanup()
    
    #getChar()
    for nextToken in file:
        lex()
    # while nextToken != EOF:
    #         lex()
    
#Token function to look up operator and parentheses and return the token
def lookup(ch):
    global nextToken
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN #25
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN #26
    elif ch == '+':
        addChar()
        nextToken = ADD_OP #21
    elif ch == '-':
        addChar()
        nextToken = SUB_OP #22
    elif ch == '*':
        addChar()
        nextToken = MULT_OP #23
    elif ch == '/':
        addChar()
        nextToken = DIV_OP #24
    elif ch == '=':
        addChar()
        nextToken = ASSIGN_OP #24
    else:
        addChar()
        nextToken = "EOF"
    return nextToken

def addChar():
    global lexeme
    global index
    global nextToken
    #adr a character if it is shorter than 98 characters
    if len(nextToken) == 1:
        lexeme = nextToken
        return True
    if len(lexeme) <= 98:
        lexeme += nextToken[index]
        try:
            test = nextToken[index+1]
        except IndexError:
            return True
        index += 1
        return False
        # lexLen=+1
        # lexeme[lexLen] = nextChar
        # lexeme[lexLen] = 0
    else:
        print("Error - lexeme is too long")

#main lexical analyzer function
def lex():
    global lexeme
    global nextToken
    global index
    lexeme = ''
    index = 0
    #check if character is in operator table
    if nextToken in operatorTable:
        nextToken = lookup(nextToken)
        #getChar()
    
    #check to see if is identifier
    try:
        if isinstance(nextToken[index], str):
            addChar()
            while isinstance(nextToken[index], str) or isinstance(nextToken[index], str):
                if addChar(): break

            nextToken = IDENT
    except(ValueError):
        #final check to see if it is an int
        if isinstance(nextToken[index], int, float):
            addChar()
            #getChar()
            while isinstance(nextToken[index], int) and boundsCheck(nextToken, index):
                addChar()
                #getChar()
            if nextToken[index] == '.':
                addChar()
                #float check
                while isinstance(nextToken[index], int) and boundsCheck(nextToken, index):
                    index += 1
                    addChar()
                nextToken = FLOAT
            nextToken = INT_LIT

    else:
        lexeme = 'EOF'

    lexemeList.append(lexeme)
    print("Next token is: " + str(nextToken) + ", Next lexeme is " + lexeme)
    return nextToken

def boundsCheck(next, index):
    try:
        next[index+1]
    except IndexError:
        return True
    return False
parsefilename()
#
# def #getChar():
#     if nextChar != 'EOF':
#         if isalpha(nextChar):
#             charClass = LETTER
#         elif isDigit(nextChar):
#             charClass = DIGIT
#         else:
#             charClass = UNKNOWN
#     else:
#         charClass = EOF

