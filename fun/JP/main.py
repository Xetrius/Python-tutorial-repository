#!/usr/bin/env python3
import time
import webbrowser

print("Jurassic Park System Secruity Interface")
print("Version 4.0.5, Alpha E")
print("Ready...")
while True:
    var1 = input(">")
    if var1 == "access main security grid":
        break
    if var1 != "access main security grid":
        print("access: PERMISSION DENIED")
a = ("https://www.youtube.com/watch?v=fmz-K2hLwSI")
webbrowser.open_new(a)
print("access: PERMISSION DENINED", "...and..." )
time.sleep(1)
while True:
    print ("YOU DIDN'T SAY THE MAGIC WORD")
    time.sleep(0.1)
