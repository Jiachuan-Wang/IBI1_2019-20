# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 08:52:01 2020

@author: 汪嘉川
"""

import re
seq = 'ATGCGACTACGATCGAGGGCCAT'
seq=re.sub(r'A','t',seq)
seq=re.sub(r'T','a',seq)
seq=re.sub(r'G','c',seq)
seq=re.sub(r'C','g',seq)
seq=seq.swapcase()
seq=seq[::-1]
print(seq)