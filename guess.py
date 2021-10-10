# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:48:48 2021

@author: ja
"""

print( 'Please think of a number between 0 and 100!')

low = 0
high = 100
guess = (low+high)/2

while True:
    print ('Is your secret number ', int(guess), '?')
    a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if a == 'h':
        high = int(guess)
        guess = (low+high)/2
    elif a == 'l':
        low = int(guess)
        guess = (low+high)/2
    elif a == 'c':
        print ("Game over. Your secret number was: ", int(guess))
        break
    else:
        print ('Sorry, I did not understand your input.')