# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:21:33 2021

@author: ja
"""


def remain_balance (balance, annualInterestRate, monthlyPaymentRate, months):
   
    """ balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal"""
    
    monthlyInterestRate = annualInterestRate / 12
    
    if months == 0:
        return balance
    minimalMonthlyPayment = monthlyPaymentRate * remain_balance(balance, annualInterestRate, monthlyPaymentRate, months-1)
    monthlyUnpaidBalance = remain_balance(balance, annualInterestRate, monthlyPaymentRate, months-1) - minimalMonthlyPayment
    remainingBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    return round(remainingBalance, 2)