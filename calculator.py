def getInput():
    usrInput1 = raw_input("Enter a number (or a letter to \033[1mexit\033[0m): ")
    try:
        a = int(usrInput1)
        #Input is numeric
        usrOperator = raw_input("Enter an operator: ")
        usrInput2 = raw_input("Enter another number: ")
        calculate(usrInput1, usrInput2, usrOperator)
    except ValueError:
        #Input is not numeric
        exit()

def calculate(a, b, o):
    a = int(a)
    b = int(b)

    if o == "+":
        res = a + b
    elif o == "-":
        res = a - b
    elif o == "*":
        res = a * b
    elif o == "/":
        res = a / b
    elif o == "**":
        res = a ** b
    else:
        print("Unkown operator")
    
    print("Result: " + str(res))
    print("")

i = 1
while i == 1:
    getInput()