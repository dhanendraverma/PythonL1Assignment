#!/usr/bin/python



len = int(input("Enter the value of subnet"))
netmask = '.'.join([str((0xffffffff << (32 - len) >> i) & 0xff) for i in [24, 16, 8, 0]])
print(netmask)