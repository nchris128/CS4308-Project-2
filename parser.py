
# modified welcome.scl file

# open files that are inside the source folder and read

keywordsCheck = ['import', 'implementations', 'function', 'variables', 'return', 'type', 'integer', 'is', 'of', 'exit', ',']
operatorsCheck = ['=', '*', '/', '('')', '[]', '<=', ":"]
identifiersCheck = ["x", "main", "scl.h", "45.95"]

def compiler(filename):

    # open files that are inside the source folder
    file = open(filename, 'r')
    f = file.read()

    cleantext = f.split()
    print(cleantext)
    return cleantext

def lookup(lexeme):
    if lexeme in keywordsCheck:
        return "0"
    elif lexeme in identifiersCheck:
        if lexeme == "43.95":
            return 1
        else:
            0
    elif lexeme in operatorsCheck:
        if lexeme == "+":
            return 21
        elif lexeme == "-":
            return 22
        elif lexeme == "*":
            return 23
        elif lexeme == "/":
            return 24
        elif lexeme == "=":
            return 10
    else:
        return 99

#keyword function
def keywords(text, nextword):
    print("<ENTERING KEYWORDS>")
    if text in keywordsCheck:
        if nextword in identifiersCheck:
            print("<RETUNRING KEYWORDS>")
            return
        else:
            print('SYNTAX ERROR!')
    else:
        print("<RETUNRING KEYWORDS>")
        return

#get identifier
def identifier(text,nextword):
    print("<ENTERING IDENTIFIERS>")
    if text in identifier:
        if nextword in operatorsCheck:
            print('<RETURNING IDENTIFIERS>')
            return
        elif nextword in keywordsCheck:
            print('<RETURNING IDENTIFIERS>')
            return
        else:
            print('SYNTAX ERROR!')
    else:
        print('<RETURNING IDENTIFIERS>')
        return

 # get operators
def operators(text, nextword):
    print("<ENTERING OPERATORS>")
    if text in operatorsCheck:
        if nextword in identifiersCheck:
            print("<RETURNING OPERATORS>")
            return
        else:
            print('SYNTAX ERROR!')
    else:
        print('<RETURNING IDENTIFIERS>')
        return
def syntaxError():
    print('SYNTAX ERROR')

# MAIN GOES HERE
print("Please enter a file name: ")  # enter welcome.scl
filename = input()
full_list = compiler(filename)

index = 0
peek = index + 1

for i in full_list:

    print("Next token is: " + lookup(full_list[i+1]) + " Next word is: " + full_list[i])
    keywords(full_list[index], full_list[peek])
    identifier(full_list[index], full_list[peek])
    operators(full_list[index], full_list[peek])
    index += 1



