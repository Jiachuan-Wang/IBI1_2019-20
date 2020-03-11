# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:47:34 2020

@author: 汪嘉川
"""

#Define a positive integer n (1 is currently given here)
n=1
#Make the first transition to n,That is, if n is an even number, divide it by 2; if it is an odd number, multiply it by 3 and add 1.
if n%2==0:
    n=n/2
else:
    n=3*n+1
#Repeat the transformation of n that has been transformed once
while 1==1:
#If n is 1, stop the program
    if n==1:
        break
#If n is not 1, transform n
    else:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1