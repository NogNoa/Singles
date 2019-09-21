# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:50:19 2019

@author: omer
"""
#def PlceCnvrt(t):

    
def TimeCnvrt(i):
    i=str(i)
    j=i.split(':')
    j=[int(k) for k in j]
    if len(j)<3:
        return j[0],j[1],0
    else:
        return j[0],j[1],j[2]
    
def SbtrctTime(E,L):
    E=TimeCnvrt(E)
    L=TimeCnvrt(L)
    return E,L
print (SbtrctTime('16:52:34','5:02'))