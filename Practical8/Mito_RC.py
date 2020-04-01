# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:44:28 2020

@author: 汪嘉川
"""

import re
fr=open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
fw=open(r'Reverse complementary sequences of mitochondria genes.fa','w')
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
for a in range(count):
    gene[a]=re.sub(r'A+?','t',gene[a])
    gene[a]=re.sub(r'T+?','A',gene[a])
    gene[a]=re.sub(r'G+?','c',gene[a])
    gene[a]=re.sub(r'C+?','G',gene[a])
    gene[a]=re.sub(r'c+?','C',gene[a])
    gene[a]=re.sub(r't+?','T',gene[a])
    gene[a]=gene[a][::-1]
for i in range(count):
    if ':Mito:' in x[i]:
        line1='>'+genename[i]+'   '+str(len(gene[i]))+'\n'
        line2=gene[i]+'\n'
        fw.write(line1)
        fw.write(line2)
fr.close()
fw.close()
fr2=open(r'Reverse complementary sequences of mitochondria genes.fa')
output=fr2.read()
print(output)