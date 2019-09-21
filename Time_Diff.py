# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:50:19 2019

@author: omer
"""
#def PlceCnvrt(t):
def UntMnger(j):
    for k in range(2):
        j[k]+=j[k+1]//60
        j[k+1]=j[k+1]%60
    return j
    
    
def TimeCnvrt(i):
    i=str(i)
    j=i.split(':')
    j=j[:3]
    j=[int(k) for k in j]
    while len(j)<3:
        j.append(0)
    j=UntMnger(j)
    return j[0],j[1],j[2]
    
def SbtrctTime(E,L):
    E=TimeCnvrt(E)
    L=TimeCnvrt(L)
    sign=L[0]>E[0]
    if sign:
        D=[L[i]-E[i] for i in range(3)]
    else:
        D=[E[i]-L[i] for i in range(3)]
    D=UntMnger(D)
    Ans=str('-('*sign+str(D[0])+':'+str(D[1])+':'+str(D[2])+')'*sign)
    return Ans
print (SbtrctTime('0:97:60','16:67:64'))

