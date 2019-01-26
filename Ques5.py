#!/usr/bin/python

file1 = open("input_file.txt","r")
file2 = open("output_file.txt","w")
line = 0
for i in file1.readlines():
    char = 0
    word = 0
    line+= 1
    char+= len(i)
    word+= len(i.split())
    print("at line %d no of characters are: %d and no of words are: %d" %(line,char,word))
    file2.write("At line no %d the no of characters - %d and no of words are - %d\r\n" %(line,word,char))



