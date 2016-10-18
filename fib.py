num = input("Number count: ");

i = 0
prn = 0
spc = 0
lis = [0,1]

print("Calculating " + str(num) + " Fibonacci numbers:")

if num < 101:
    while i < num:
        last = lis[len(lis) - 1]
        blast = lis[len(lis) - 2]
        prn = int(last) + int(blast)
        lis.append(prn)
        spc = len(str(prn)) + len(str(i))
        print(str(i + 1) + "."*(50-spc) + str(prn))
        i = i + 1
else:
    print("Max number count is 100")