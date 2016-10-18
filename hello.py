import sys

arg = "World"

if len(sys.argv) > 1:
    arg = sys.argv[1]

print("Hello " + str(arg) + "!")