# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:59:59 2020

@author: 汪嘉川
"""

#Input gene lengths
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
#Sort gene lengths
gene_lengths=sorted(gene_lengths)
#Delete the longest and the shortest gene
del(gene_lengths[0])
gene_lengths.pop()
#Create a box chart
import matplotlib.pyplot as plt
plt.boxplot(gene_lengths,vert=True,whis=1.0,patch_artist=True,meanline=True,showbox=True,showcaps=True,showfliers=True,notch=False)
plt.show()