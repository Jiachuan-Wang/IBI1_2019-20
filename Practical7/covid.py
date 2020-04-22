# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:10:37 2020

@author: 汪嘉川
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/WangJiachuan/Desktop")
covid_data = pd.read_csv("full_data.csv")

print(covid_data.iloc[0:18:3])

Afghanistan=[]
x= covid_data.iloc[:,1]
for y in range (0,7996):
    if x[y]=='Afghanistan':
        Afghanistan.append(True)
    else:
        Afghanistan.append(False)
print(covid_data.loc[Afghanistan,'total_cases'])

world=[]
a= covid_data.iloc[:,1]
for b in range (0,7996):
    if a[b]=='World':
        world.append(True)
    else:
        world.append(False)
world_date=covid_data.loc[world,'date']
world_new_cases=covid_data.loc[world,'new_cases']
world_new_deaths=covid_data.loc[world,'new_deaths']
print('Mean=',np.mean(world_new_cases,axis=0))
print('Median=',np.median(world_new_cases,axis=0))

plt.boxplot(world_new_cases,
            vert= True,
            whis= 1.5,
            patch_artist=True,
            meanline=True,
            showbox=True,
            showcaps=False,
            showfliers=True,
            notch= False,
            medianprops={'color':'red'},
            whiskerprops={'color':'black'})
plt.title('Boxplot of New Cases Worldwide')
plt.ylabel('Number')
plt.show()

plt.scatter(world_date,world_new_cases,c='blue',label='World new cases')
plt.scatter(world_date,world_new_deaths,c='red',label='World new deaths')
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)
plt.title('Scatterplot of New Cases and New Deaths Worldwide')
plt.xlabel('Date')
plt.ylabel('Number')
plt.legend(loc='upper left')
plt.show()

china=[]
d= covid_data.iloc[:,1]
for e in range (0,7996):
    if d[e]=='China':
        china.append(True)
    else:
        china.append(False)
china_date=covid_data.loc[china,'date']
china_new_cases=covid_data.loc[china,'new_cases']
china_total_cases=covid_data.loc[china,'total_cases']
plt.scatter(china_date,china_new_cases,c='blue',label='China new cases')
plt.scatter(china_date,china_total_cases,c='green',label='China total cases')
plt.xticks(china_date.iloc[0:len(china_date):4],rotation=-90)
plt.title('Scatterplot of New Cases and Total Deaths in China')
plt.xlabel('Date')
plt.ylabel('Number')
plt.legend(loc='upper left')
plt.show()