def fun1():                            # the corn function
    global a                           # sets 'a' as global
    a = int(input("set var a\n"))      # get int var "a" from user

fun1()                                 # run corn function
print("input var\n", a)                # prints "a" from corn function
