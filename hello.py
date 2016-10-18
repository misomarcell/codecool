import sys

arg = "World"

if len(sys.argv) > 1:
    arg = sys.argv[1]

if arg:
    print("Hello " + str(arg) + "!")
else:
    print("Hello World!")