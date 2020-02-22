# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:47:07 2019

@author: omer
"""

def abjad(Letter):
    b=''
    Vowels=['a','e','i','o','u']
    MinorVow=['a','o','u']
    punct=[' ',',',';','.',':','"',"'",'!','?','(',')','-']
    for i,char in enumerate(Letter):
        iot=char=='i' and not Letter[i+1] in Vowels
        cog=(char=='e' or iot) and not Letter[i-1] in ['c','g','C','G']
        edge=Letter[i+1:i+2] in punct or Letter[i-1] in punct
        final=(char in MinorVow or cog) and not edge
        if final:
           b+=''
        elif Letter[i]=='h' and Letter[i-1] in Vowels:
           b+="'h"
        else:
            b+=char     
    return b
#print(abjad('A vowel is a syllabic speech sound pronounced without any stricture in the vocal tract. Vowels are one of the two principal classes of speech sounds, the other being the consonant. Vowels vary in quality, in loudness and also in quantity (length). They are usually voiced, and are closely involved in prosodic variation such as tone, intonation and stress.'))
#print(abjad('aahe'))