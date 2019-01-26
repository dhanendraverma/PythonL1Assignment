#!/usr/bin/python



list1 = [4,6,7,2,0,9,12,67,89]
list2 = [34,76,56,2,34,889,43,45,66]
list3 = [7,123,75,43,75322,67,34]
list1.sort()
list2.sort()
list3.sort()

Maxlist = []
Maxlist.extend(list1[-2:])
Maxlist.extend(list2[-2:])
Maxlist.extend(list3[-2:])
temp=0
for i in Maxlist:
    temp=0
    temp+= i

print('Average of MaxList is',temp/6)

Minlist = []

Minlist.extend(list1[:2])
Minlist.extend(list2[:2])
Minlist.extend(list3[:2])

for i in Minlist:
    temp=0
    temp+= i

print('Average of Minkist is',temp/6)
