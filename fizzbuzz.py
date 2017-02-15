#!/usr/bin/env python3
print("FizzBuzz")
var2 = int(input("high number?\n"))
var = 0
for x in range(1,var2):
    var = var + 1
    if var%3==0 and var%5==0:
        print('FizzBuzz')
    elif var%3==0:
        print('Fizz')
    elif var%5==0:
        print('Buzz')
    else:
        print(var)
