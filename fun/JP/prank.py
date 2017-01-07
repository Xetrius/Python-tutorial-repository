#!/usr/bin/env python3
import time
import webbrowser

print("Jurassic Park System Secruity Interface")
print("Version 4.0.5, Alpha E")
print("Ready...")

'''
while True:
    var1 = input(">")
    if var1 == "access main security grid":
        break
    if var1 != "access main security grid":
        print("access: PERMISSION DENIED")
    if var1 == "help":
        print("*************HELP*************")
        print("*   To advance the program   *")
        print("*    enter the following     *")
        print("* access main security grid  *")
        print("******************************")
'''
a = ("https://www.youtube.com/watch?v=fmz-K2hLwSI")
webbrowser.open_new(a)
print("access: PERMISSION DENINED", "...and..." )
time.sleep(1)
for c in range(0, 200):
    print ("YOU DIDN'T SAY THE MAGIC WORD")
    time.sleep(0.1)
