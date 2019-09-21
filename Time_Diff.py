# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:50:19 2019

@author: omer
"""
#def PlceCnvrt(t):

    
def TimeCnvrt(i):
    i=str(i)
    j=i.split(':')
    j=j[:3]
    j=[int(k) for k in j]
    while len(j)<3:
        j.append(0)
    for k in range(2):
        j[k]+=j[k+1]//60
        j[k+1]=j[k+1]%60
    return j[0],j[1],j[2]
    
def SbtrctTime(E,L):
    E=TimeCnvrt(E)
    L=TimeCnvrt(L)
    D=[L[i]-E[i] for i in range(3)]
    return D
print (SbtrctTime('16:67:64','5:02'))