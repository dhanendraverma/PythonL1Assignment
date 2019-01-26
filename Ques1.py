#!/usr/bin/python

mylist = list(range(4))

seclist = mylist
print(seclist)  #output-->[0, 1, 2, 3]


mylist.append(4)
print(seclist)  #output-->[0, 1, 2, 3, 4]

seclist = mylist[:]
print(seclist)  #output-->[0, 1, 2, 3, 4]

mylist.append(5)
print(seclist)  #output-->[0, 1, 2, 3, 4]