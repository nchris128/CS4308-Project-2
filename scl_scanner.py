#removing comments and unnecessary symbols
def cleanup():
    strippedText = ''
    cleanedText = ''

    #characters to remove from code
    toStrip = ',.":'

    #replacing each instance of the character with spaces
    for toStrip in toStrip:
        strippedText = scl.replace(toStrip, ' ')

    #split the code into a list of lines
    lineText =  strippedText.splitlines()
    descriptionIndex = 0
    lineText = [i.lstrip() for i in lineText]

    for descriptionLine in lineText:

        #finding lines with description
        if 'description' in descriptionLine.lstrip():
            descriptionIndex = lineText.index('description')

            #remove lines until */ is found
            while '*/' not in lineText[descriptionIndex]:
                descriptionLine = lineText.pop(descriptionIndex)

            #else to remove the leftover end comment
            else:
                descriptionLine = lineText.pop(descriptionIndex)

    #removing single line comments by creating a substring before //
    for line in lineText:

        if '//' in line:
            index = line.index('//')
            cleanedText = cleanedText + line[0:index] + '\n'

        else:
            cleanedText = cleanedText + line + '\n'
    cleanedText = cleanedText.split()
    return(cleanedText)

def keywordScanner():
    #table for keywords to compare to the scl file
    keywordTable =['import', 'begin', 'call','using', 'endfun', 'set', 'exit',
                 'symbol', 'forward', 'function', 'parameters', 'array', 'integer',
                 'struct', 'double', 'Serial.println', 'char', 'float', 'byte', 'display', 'while', 'endwhile',
                 'unsigned', 'long', 'short', 'definetype', 'forward', 'return', 'type', 'void', 'parameters',
                 'pointer', 'DataT', 'listT', 'nodePtrT', 'address', 'using', 'destroy', 'NodeType', 'variables',
                 'parameters', 'bool']
    keywordList = []

    #iterates through scl to find keywords and add it to new list
    for i in cleanedSCL:
        if i in keywordTable:
            keywordList.append(i)

    print('\nKeywords Found:')
    print(keywordList)
    print('Keywords Total: ' + str(len(keywordList)))
 
def identifierScanner():
    
    #iterates through scl looking for identifiers being defined then adding to new list
    idx = 0
    identifiterList = []
    for i in cleanedSCL:
        idx += 1
        if i == 'define':
            identifiterList.append(cleanedSCL[idx])

    print('\nIdentifiers Found:')
    print(identifiterList)
    print('Identifier Total: ' + str(len(identifiterList)))    

def operatorScanner():
    #iterates through scl to find operators and add it to new list
    operatorTable = [ '=', '*', '/', '(', ')', '[]', '<=', '>=', ':']
    operatorList = []
    for i in cleanedSCL:
        if i in operatorTable:
            operatorList.append(i)

    print('\nOperators Found:')
    print(operatorList)
    print('Operator Total: ' + str(len(operatorList)))

def read():
    # print('Please enter the name for the scl file to scan\nExample: arduino_ex1.scl')
    # file = input()
    file = 'welcome.scl'
    openedFile = open(file)
    scl = openedFile.read()
    return(scl)
#user enters scl location to scan then is opened to read

scl = read()
cleanedSCL = cleanup()
keywordScanner()
identifierScanner()
operatorScanner()


