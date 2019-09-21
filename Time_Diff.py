# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:50:19 2019

@author: omer
"""

def SbtrctTime(E,L):
    for i in [E,L]:
        if ':'==i[1]:
            i='0'+i
        elif ':'==i[-2]:
            i.insert(-2,'0')
        