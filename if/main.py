var1 = 42
while True:
    var2 = int(input("guess my number\n"))
    if var2 > var1:
        print("too high\n")
    if var2 < var1:
        print("too low\n")
    if var2 == var1:
        print("very good\n")
        exit()
