
# modified welcome.scl file

# open files that are inside the source folder and read

keywordsCheck = ['import', 'implementations', 'function', 'variables', 'return', 'type', 'integer', 'is',
                 'of']
operatorsCheck = ['=', '*', '/', '('')', '[]', '<=', ":"]
identifiersCheck = ["x", "main", "scl.h"]

def compiler(filename):

    # open files that are inside the source folder
    file = open(filename, 'r')
    f = file.read()

    cleantext = f.split()
    print(cleantext)
    return cleantext

def nexttoken(text):

#keyword function
def keywords(text):
    print("<ENTERING KEYWORDS>")


#get identifier
def identifier(self):
    print("<ENTERING IDENTIFIERS>")

 # get operators
def operators(self):
    print("<ENTERING OPERATORS>")


def syntaxError():
    print('SYNTAX ERROR')

# MAIN GOES HERE
print("Please enter a file name: ")  # enter welcome.scl
filename = input()
full_list = compiler(filename)

