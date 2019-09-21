# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:50:19 2019

@author: omer
"""
def Timecnvrt(i):
    i=str(i)
    mid=i.index(':')
    H=int(i[:mid])
    M=int(i[mid+1:])
    return H,M
    
def SbtrctTime(E,L):
    E=Timecnvrt(E)
    L=Timecnvrt(L)
    return E,L
print (SbtrctTime('16:52','5:02'))