
# modified welcome.scl file

# open files that are inside the source folder and read
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
    cleantext = f.split()
    print(cleantext)

 #get keywords from input
def compile(self, input):


 #keyword function
def keywords(self):


 #get identifier
def identifier(self):


 # get operators
def operators(self):


# getnexttoken
def getnexttoken(self):


# MAIN GOES HERE
print("Please enter a file name: ")  # enter welcome.scl
filename = input()
arrayFilename(filename)



