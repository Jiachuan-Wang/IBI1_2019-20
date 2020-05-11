# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:55:10 2020

@author: 汪嘉川
"""

#Input gene sequence，save as a string called DNA_string
DNA_string="ATGCTTCAGAAAGGTCTTACG"
#Measure the total number of DNA nucleotides in the gene sequence
Length=len(DNA_string)
#Create a dictionary to store the number of occurrences of each DNA nucleotide
n={}
for i in DNA_string:
    if i not in n:
        n[i]=1
    else:
        n[i]+=1
#Calculate the frequency of each DNA nucleotide and convert it into a pie chart parameter
A=n["A"]/Length*100
C=n["C"]/Length*100
G=n["G"]/Length*100
T=n["T"]/Length*100
print("Frequency Table:","A=",A,"%","C=",C,"%","G=",G,"%","T=",T,"%")
#Create a pie chart
import matplotlib.pyplot as plt
plt.title("Pie of the 4 DNA nucleotides",fontsize=14)
labels="A","C","G","T"
sizes=[A,C,G,T]
explode=(0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.show()