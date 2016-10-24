#Made by. Marcell Misó & Gábor Varga
import os

filename = "todo.txt"
todoList = []

def readFile(location):
    if os.path.isfile("./" + filename):
        file = open(location, 'r')
        return(file.read())
    else:
        target = open("./" + filename, 'w')
        target.write("")
        target.close()
        return("")

def writeFile(title, content):
    target = open("./" + str(title), 'w')
    target.write(content)
    target.close()

def deleteContent(fName):
    with open("./" + fName, "w"):
        pass

def start():
    print("Please specify a command [list, add, mark, archive]: ")
    command = input()

    if command == "list":
        tempList = readFile(filename)
        i = 0
        for line in tempList.splitlines():
            status, name = line.split(",")
            status2 = ""
            if status == "1":
                status2 = "X"
            elif status == "0":
                status2 = " "
            print(str(i) + ". [" + status2 + "]" + name)   
            i = i + 1     
    elif command == "add":
        todoName = input("What you want to do? ")
        tempList = readFile(filename)
        tempList = tempList + "0," + todoName + "\n"
        writeFile(filename, tempList)
    elif command == "mark":
        i = 0
        tempListMark = readFile(filename)
        tempListMark2 = ""
        id = input("Wich one? ")
        lineCount = tempListMark.count('\n') - 1
        if int(id) > int(lineCount) or int(id) < 0:
            print("No item with this ID")

        for line in tempListMark.splitlines():
            status, name = line.split(",")
            if int(id) == int(i):
                tempListMark2 = tempListMark2 + "1," + name + "\n"
            else:
                if int(status) == 1:
                    tempListMark2 = tempListMark2 + "1," + name + "\n"    
                else:
                    tempListMark2 = tempListMark2 + "0," + name + "\n"
            i = i + 1
        deleteContent(filename)
        writeFile(filename, tempListMark2)
    elif command == "archive":
        i = 0
        tempListArch = readFile(filename)
        tempListArch2 = ""
        for line in tempListArch.splitlines():
            status, name = line.split(",")
            if int(status) == 1:
                tempListArch2 = tempListArch2 + ""
            else:
                tempListArch2 = tempListArch2 + status + "," + name + "\n" 
            i = i + 1
        deleteContent(filename)
        writeFile(filename, tempListArch2)
    else:
        print("Unkown command")

start()
