import os, re

extensionRegex = re.compile(r'.txt$')
textRegex = re.compile(r'New York')

for filename in os.listdir(os.getcwd()):
    if extensionRegex.search(filename):
        openFile = open(filename, 'r')
        lines = openFile.readlines()
        for line in lines:
            if textRegex.search(line):
                print(filename + '\t' + line)