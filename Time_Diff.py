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
    #E is for early and L is for late. 
    #If L is smaller you'll get answer for L in the next day. 
    E=TimeCnvrt(E)
    L=TimeCnvrt(L)
    sign=L[0]>=E[0]
    D=[L[i]-E[i] for i in range(3)]
    if not sign:
        D[0]+=24
        lu=str(L[0])+':'+str(L[1])+':'+str(L[2])
        print('for',lu,'in next day')
        #helps the user notice that a 'day overflow' had occured
    D=UntMnger(D)
    Ans=str(D[0])+':'+str(D[1])+':'+str(D[2])
    return Ans
print (SbtrctTime('22:00:00','15:30'),SbtrctTime('16:00:00','9:30'))

