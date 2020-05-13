# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:09:01 2020

@author: 汪嘉川
"""

# import libraries
from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
import numpy as np
# list the elements
DOMTree = xml.dom.minidom.parse("go_obo.xml")
term = DOMTree.documentElement
root = DOMTree.documentElement
terms = root.getElementsByTagName('term')
# define the arrays
defs=[]
ids=[]
names=[]
definitions=[]
is_a=[]
array=[]
dic={}
# filter the nodes
for term in terms:
    defsList=term.getElementsByTagName('def')
    idsList=term.getElementsByTagName('id')[0]
    is_asList=term.getElementsByTagName('is_a')
    for m in is_asList:
        is_a.append(m.childNodes[0].data)
    dic[idsList.childNodes[0].data]=is_a[:]
    is_a.clear()
    for DEF in defsList:
        defstr=DEF.getElementsByTagName('defstr')[0]
        defs.append(defstr.childNodes[0].data)  
# find "autophagosome"
for m in range(len(defs)):
    if 'autophagosome' in defs[m]:
        array.append(m)
# record the corresponding information in elements' texts
for i in array:
    idsList=terms.item(i).getElementsByTagName('id')[0]
    ids.append(idsList.childNodes[0].data)
    Names=terms.item(i).getElementsByTagName('name')[0]
    names.append(Names.childNodes[0].data)
    definitions.append(defs[i])
# count the number of childnodes
childnode = []
for i in ids:
    x = []
    count = 0
    for j in dic:
        if i in dic[j]:
            count += 1
            x.append(j)
    y = x[:]
    inc = count
    while inc != 0 :
        x = []
        inc = 0
        for k in y:
            for j in dic:
                if k in dic[j]:
                    inc += 1
                    count += 1
                    x.append (j)
        y = x[:]
    childnode.append(count)
# mapping
dataframe=pd.DataFrame({'id':ids,'name':names,'definition':definitions,'childnodes':childnode})
dataframe.to_excel('Autophagosome.xlsx',columns=['id','name','definition','childnodes'],index=False)