import sys
import os
from os import walk

try:
    arg = sys.argv[1]
except:
    arg = 0

def createDir():
    if not os.path.exists("ideas"):
        os.makedirs("ideas")
createDir()

def writeFile(title, content):
    target = open("./ideas/" + str(title), 'w')
    target.write(content)
    target.close()

def listFiles():
    f = []
    for (dirpath, dirnames, filenames) in walk("./ideas"):
        f.extend(filenames)
        break
    return(f)

if arg == "-l":
    files = listFiles()
    files.sort()
    for x in files:
        file = open("./ideas/" + x, 'r')
        print(x + ". " + file.read())
elif arg == "-r":
        try:
            os.remove("./ideas/" + sys.argv[2])
            print("File " + sys.argv[2] + " successfully removed!")
        except:
            print("Syntax error, or file not exists. Usage: -r <ID>")
else:
    idea = raw_input("Type your idea: ")
    writeFile(len(listFiles()) + 1, idea)
    print("")
    
