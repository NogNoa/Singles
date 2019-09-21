# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:50:19 2019

@author: omer
"""
def PlceCnvrt(t):
    

def TimeCnvrt(i):
    i=str(i)
    mid=i.index(':')
    H=int(i[:mid])
    i=i[mid+1:]
    mid=i.find(':')
    try:
        M=int(i[:mid])        
    except:
        return H,0,0
    if mid==-1:
        return H,M,0
    i=i[mid+1:]
    mis=i.find(':')
    if i!='':
        S=i
    else:
        S=0
    return H,M,S
    
def SbtrctTime(E,L):
    E=TimeCnvrt(E)
    L=TimeCnvrt(L)
    return E,L
print (SbtrctTime('16:52','5:02'))