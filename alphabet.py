# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:28:47 2021

@author: ja
"""

s = input("Write a word:")
n = 1
sum = 0
ind = 0

alf = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

for i in range(len(s)-1):
    if alf.index(s[i]) <= alf.index(s[i+1]):
        n +=1
    elif n > sum:
        ind = i-n+1
        sum = n
        n = 1
    else:
        n = 1
        
if sum == 0:
    sum = len(s)

if n > sum:
    ind = i-n+2
    sum = n

print (s[ind:ind+sum])