#!/usr/bin/python


string = str(input("Enter the string to be checked: "))

def DoubleECheck(string1):
    for i in range(len(string1)-1):
        if (string1[i] is 'e' or string1[i] is 'E') and (string1[i+1] is 'e' or string1[i+1] is 'E'):
            return True
        elif i is len(string1)-1:
            return False


if DoubleECheck(string):
    print('True')
else:
    print('False')