var1 = 42
while True:
    var1 = int(input("guess my number\n"))
    if var1 > 42:
        print("too high\n")
    if var1 < 42:
        print("too low\n")
    if var1 == 42:
        print("very good\n")
        exit()
