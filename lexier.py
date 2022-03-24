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

#remove comments using scanner and run
def parsefilename():
    global nextToken
    file = scl_scanner.cleanup()
    
    #iterate though file lexeme by lexeme
    for nextToken in file:
        lex()

    
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
        nextToken = ASSIGN_OP #20
    else:
        addChar()
        nextToken = "EOF"
    return nextToken

#add characters to make full lexemes
def addChar():
    global lexeme
    global index
    global nextToken

    #if the lexeme is only a single character declare it without iterating
    if len(nextToken) == 1:
        lexeme = nextToken
        return True

    #checking to see if the lexeme is too long
    if len(lexeme) <= 98:

        #add current character
        lexeme += nextToken[index]

        #test to stop when lexeme is finished
        try:
            test = nextToken[index+1]
        
        #return true when lexeme is finished
        except IndexError:
            return True

        #iterate through lexeme
        index += 1

        #retun false to show the lexeme is not complete
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
        
    #check to see if is identifier
    elif type(nextToken[index]) == str:
        try:
            intCheck = float(nextToken)
        except(ValueError):
            addChar()
            while type(nextToken[index]) == str or type(nextToken[index]) == int:
                if addChar(): break
            nextToken = IDENT
        else:
        #final check to see if it is an int or float
            if type(nextToken == int or float):
                addChar()
                
                #keep adding ints to make full number
                while type(nextToken[index] == int or float):
                    if addChar(): break
                
                #if there is a decmal declare it as float
                if '.' in nextToken:
                    nextToken = FLOAT
                
                else:
                    nextToken = INT_LIT

    #if it does not pass any send EOF maybe change !!!!!!!!
    else:
        lexeme = 'EOF'

    #add lexeme to list of lexemes
    lexemeList.append(lexeme)

    #output token and lexeme
    print("Next token is: " + str(nextToken) + ", Next lexeme is " + lexeme)
    return nextToken

# parsefilename()


#
# def :
#     if nextChar != 'EOF':
#         if isalpha(nextChar):
#             charClass = LETTER
#         elif isDigit(nextChar):
#             charClass = DIGIT
#         else:
#             charClass = UNKNOWN
#     else:
#         charClass = EOF

