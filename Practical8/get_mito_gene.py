# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:22:32 2020

@author: 汪嘉川
"""


fr=open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
fw=open(r'mito_gene.fa','w')
x=[]
y=[]
z=str()
gene=[]
genename=[]
count=0
for line in fr:
    if line.startswith('>'):
        if z!='':
            gene.append(z)
        genename.append(line[1:8])
        z=''
        x.append(line)
        count=count+1
    else:
        line=line.rstrip()
        z=z+str(line)
gene.append(z)
for i in range(count):
    if ':Mito:' in x[i]:
        LINE='>'+genename[i]+'       '+str(len(gene[i]))+'\n'
        fw.write(LINE)
fr.close()
fw.close()
fr2=open(r'mito_gene.fa')
for line in fr2:
    print(line)