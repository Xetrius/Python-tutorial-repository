#!/usr/bin/env python3
import time
import webbrowser
a = ("https://www.youtube.com/watch?v=fmz-K2hLwSI")
#b = ("google-chrome")
#webbrowser.get(using=b)
print("access: PERMISSION DENINED",)
time.sleep(.3)
print("...and...")
webbrowser.open_new(a)
time.sleep(.5)

while True:
    print ("YOU DIDN'T SAY THE MAGIC WORD")
    time.sleep(0.1)
