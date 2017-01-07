import winsound
print("lowest hz 37")
print("highest hz 32,767")
var1 = int(input("starting hz\n>"))
var2 = int(input("duration in sec\n>"))
dur1 = var2 * 1000

for a in range(var1,32767):
    print(a,"Hz")
    winsound.Beep(a,dur1)
