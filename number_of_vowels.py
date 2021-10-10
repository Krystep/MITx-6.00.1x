# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:33:29 2021

@author: ja
"""

s = input("Write a word:")
vowels = ['a', 'e', 'i', 'o', 'u']
x = 0

for i in s:
    if i in vowels:
        x += 1

print ("Number of vowels:", x)