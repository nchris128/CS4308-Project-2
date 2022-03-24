import os
import parser
import scanner

def printMenu():
    print("========Menu========")
    print("1) Enter File Name ")
    print("2) Read File Name ")
    print("3) Separate the keywords, operators, and identifiers from the File Name")
    print("4) Check for next Token")
    print("5) Exit ")
    print("====================")

def compiler(filename):
    file = open(filename, 'r')
    f = file.read()
    cleantext = f.split()
    # print(cleantext)
    return cleantext

choice = 0
while choice != 5:
    printMenu()
    choice = int(input())

    if choice == 1:
        print("Please enter a file name: ")
        filename = input()

    elif choice == 2:
        try:
            scanner.readFilename(filename)
        except:
            print("File Name: " + filename + " was not found!!!")

    elif choice == 3:
        try:
            scanner.arrayFilename(filename)
        except:
            print("File Name: " + filename + " was not found!!!")

    elif choice == 4: #check for next token Not Working
        #try:
            parser.parsefilename(filename)
        #except:
            #print("File Name: " + filename + " was not found!!!")

    elif choice == 5:
        print("Exiting Program........")

    else:
        print("Wrong Choice, Try Again")