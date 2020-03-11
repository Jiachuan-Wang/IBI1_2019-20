# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:42:38 2020

@author: 汪嘉川
"""

#Define an x as an input value
x=1750
#Save the original input value
origin=x
#Define a string A to store recursive statements
A=str()
#Iteratively divide(integer form) x value
for n in range(0,13):
    #If the original input value is greater than 2 ** n, the position of the index is 1, and this information is stored in A
    if x%2==1:
        x=(x-1)/2
        A="2**"+str(n)+"+"+A
    #If it is divisible by 2, then the position of the index is 0, there is no need to enter the string A
    else:
        x=x/2
#Improve the format and print out
B=str(origin)+" is "+A
print(B[:-1])