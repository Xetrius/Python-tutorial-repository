
#a (Global Variables)

### main.py ### 

    def fun1():                           # the fun1 function
        global a                          # sets 'a' as global, global must be declared before Var is set  
        a = int(input("set var a\n"))     # get the "var" from user, as an "int", print w/new line

    fun1()                                # run fun1 function
    print(a)                              # prints "a" from fun1 function

### EOF ###

### main output ### 
iputed var
#####

what we have learned
if (the function is called) and (the var is global) the var can be reused outside the function

#####



#b   (calling a function var from another file)

lets rename main.py to settings.py because" import main" throws all kinds of errors

both files must be in same directory

### settings.py ###
    def fun1():      # defines the function fun1
        global a      # sets "a" as a global var
        a = 6666     # the var "a"
### EOF ###

####  main.py ###
    import settings    # imports settings.py, when calling from settings.py  use "settings.*****"
    settings.fun1()    # runs the function fun1(): with "settings." prefix
    b =  settings.a     # sets "b" from "a" in settings.py from def fun1(): 
    print(b)                  # print the new "b" var created from fun1(): "a" 
### EOF ###

### output of main.py ###
6666 
#####

what we have learned 
(import name) with a (.) is setup for (running python commands as normal) from imported file

####



#c ( call a var from a function by another function? (is this worded right?lol) )

### main.py ###
    def fun1():
        global a
        a = int(input("set var a\n"))

    def fun2():
        fun1()
        print("input var\n", a)

    fun1()
    print("input var\n", a)
    fun2()

### EOF ###

