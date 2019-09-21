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
    D=[L[i]-E[i] for i in range(3)]
    D=UntMnger(D)
    if D[0]<0:
        if D[2]!=0:
            D[2]=60-D[2]
            D[1]+=1
        if D[1]!=0:
            D[1]=60-D[1]
            D[0]+=1
    Ans=str(D[0])+':'+str(D[1])+':'+str(D[2])
    return Ans
print (SbtrctTime('16:67:64','0:97:60'))

#mixed plusses and minuses 
#say (-16:+30:-4) should be (-15:30:04)
#now would be (-16:30:04)
#the untmnger would be (-16:29:56)
