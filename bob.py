# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:42:13 2021

@author: ja
"""

s = input("Write a word:")

x = 0
n = 0

for i in range(len(s)-2):
    if s[i] == 'b':
        if s[i+1] == 'o':
            if s[i+2] == 'b':
                x += 1
    n += 1
    
print ("Number of times bob occurs is:", x)