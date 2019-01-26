#!/usr/bin/python

from xml.dom import minidom

doc = minidom.parse('bookstor.xml')
temp1 = doc.getElementsByTagName('bookstore')
temp2 = doc.getElementsByTagName('book')
temp3 = doc.getElementsByTagName('title')
temp4 = doc.getElementsByTagName('year')
temp5 = doc.getElementsByTagName('price')
temp6 = doc.getElementsByTagName('author')


print("Hi! your current section is:",temp1[0].attributes['shelf'].value)
print("Books available in this section and their descriptions are given below")
print("---------------------------------------------------------------------------")

for i in temp2:
    print('*Category           :', i.attributes['category'].value)

for i in temp3:
    print("*Language           :", i.attributes['lang'].value)

for i in temp3:
    print("*Book name          :",i.firstChild.data)

for i in temp4:
    print("*Year of publishing :",i.firstChild.data)

for i in temp6:
    print("*Author             :",i.firstChild.data)


for i in temp5:
    print("*Price              :",i.firstChild.data)