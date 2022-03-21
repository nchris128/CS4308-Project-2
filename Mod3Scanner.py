import os
# deliverable 1 for group 9

def printMenu():
    print("========Menu========")
    print("1) Enter File Name ")
    print("2) Read File Name ")
    print("3) Separate the keywords, operators, and identifiers from the File Name")
    print("4) Exit ")
    print("====================")

def readFilename(filename):
    # open files that are inside the source folder and read
    file = open(filename, 'r')
    text = file.read()
    print(text)

    print("\n===============================")
    print("End of File Name: " + filename)
    print("===============================\n")

def arrayFilename(filename):
    keywords = []
    operators = []
    identifiers = []
    dump = []

    keywordsCheck = ['import', 'begin', 'call', 'using', 'endfun', 'set', 'exit',
                     'symbol', 'forward', 'function', 'parameters', 'array', 'integer',
                     'struct', 'double', 'Serial.println', 'char', 'float', 'byte', 'display', 'while', 'endwhile',
                     'unsigned', 'long', 'short', 'definetype', 'forward', 'return', 'type', 'void', 'parameters',
                     'pointer', 'DataT', 'listT', 'nodePtrT', 'address', 'using', 'destroy', 'NodeType', 'variables',
                     'parameters', 'bool']
    operatorsCheck = ['=', '*', '/', '('')', '[]', '<=', ":"]

    identifiersCheck = ['setup', 'sensorValue', 'voltage', 'loop', 'MM', 'NHG', 'MYHV', 'MYSHV', 'num_elements',
                        'xcoord', 'ycoord', 'MAX', 'ARRAY_SIZE', 'varm2', 'var3', 'strname', 'var6', 'main', 'marray',
                        'max_val',
                        'kelements', 'j', 'mybhvar', 'myihvar', 'xc', 'i', 'max_elem', 'hh', 'max_array', 'MN', 'varb',
                        'varc1', 'varc2', 'varc3', 'varc4', 'd1', 'd2', '<stdio.h>', '<stdlib.h>', '<string.h>',
                        'Datablock', 'stname', 'age', 'jobcode', 'make_dblock', 'nname', 'nage', 'njobcode',
                        'display_data',
                        'traverse_display', 'create_list', 'clist', 'dblock', 'pjobcode', 'dbsize', 'ldatab', 'strcpy',
                        'node', 'llist', 'numnodes', 'maxnodes', 'sname', 'Head', 'current', 'maxn', 'pname', 'pnode',
                        'remove_front', 'empty_list', 'full_list', 'lpos', 'plist', 'get_front', 'get_next',
                        'remove_last', 'csize', 'lposition', 'insert_node', 'get_node']

    # open files that are inside the source folder
    file = open(filename, 'r')
    f = file.read()

    # file cleanup
    y = f.replace(',', '')
    y = f.replace('(', '')
    y = f.replace(')', '')
    y = f.replace('.', '')
    y = f.replace('"', '')
    y = f.replace(':', '')
    cleantext = y.split()

    # print(cleantext)
    index = 0;
    for i in cleantext:
        # print (cleantext[index])
        if cleantext[index] in keywordsCheck:
            keywords.append(cleantext[index])
            index += 1

        elif cleantext[index] in operatorsCheck:
            operators.append(cleantext[index])
            index += 1

        elif cleantext[index] in identifiersCheck:
            identifiers.append(cleantext[index])
            index += 1

        else:
            dump.append(cleantext[index])
            index += 1

        #Count the number of element for each list
        countKey = len(keywords)
        countOp = len(operators)
        countId = len(identifiers)

    print("Total Keywords: " ,countKey)
    print("Total Operators: " , countOp)
    print("Total Identifiers: " , countId, "\n")

    print("Keywords in .scl files: ", keywords, "\n")
    print("Operators in .scl files: ", operators, "\n")
    print("Identifiers in .scl files: ", identifiers, "\n")

    print("\n===============================")
    print("End of File Name: " + filename)
    print("===============================\n")

#======MAIN PROGRAM=====

choice = 0
while choice != 4:
    printMenu()
    choice = int(input())

    if choice == 1:
        print("Please enter a file name: ")
        filename = input()

    elif choice == 2:
        try:
            readFilename(filename)
        except:
            print("File Name: " + filename + " was not found!!!")

    elif choice == 3:
        try:
            arrayFilename(filename)
        except:
            print("File Name: " + filename + " was not found!!!")

    elif choice == 4:
        print("Exiting Program........")

    else:
        print("Wrong Choice, Try Again")