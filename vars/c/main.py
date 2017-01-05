def fun1():
    global a
    a = int(input("set var a\n"))

def fun2():
    fun1()
    print("input var\n", a)

fun1()
print("input var\n", a)
fun2()
