#!/usr/bin/python

import os

directory = str(input("Enter the directory path: "))

for (path,dir,files) in os.walk(directory):
    for file in files:
        filename = os.path.join(directory, file)
        size = os.path.getsize(filename)
        if(size==0):
            print(file)
