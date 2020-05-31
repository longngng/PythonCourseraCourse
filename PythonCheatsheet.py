#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:06:03 2020

@author: longnn
"""

#%% print format
def hello():
    print("Hello World!")
    print("Hello ", end='')
    print("World!")

hello()    
#%% input
def getNum():
    strnum1 = input("Enter 1st number: ")
    strnum2 = input("Enter 2nd number: ")
    x = int(strnum1)
    y = int(strnum2)
    print("Sum is", x+y)
    print("Product is", x*y)
    
getNum()
#%% if-else
def bmi(x):
    if (x > 23):
        print("You are fat!")
    elif(x > 21):
        print("You are good!")
    else:
        print("You are too thin!")

bmi(25)
bmi(22)
bmi(10)
#%% loops
def sum_odd(n):
    my_sum = 0
    for i in range(1, n, 2):
        my_sum += i
    print("Sum of odd numbers is ", my_sum)

sum_odd(4)
sum_odd(6)
#%% List
def iterate_list():
    lis1 = ["rice", "bread", "prata"]
    for it in lis1:
        print(it)
iterate_list()
#%%