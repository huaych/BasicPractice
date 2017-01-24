# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 18:12:47 2017

@author: whua
"""

def bubbleSort(L):
    swap = True
    while swap != False:
        swap = False
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i + 1]
                L[i + 1] = temp
                swap = True
                
    return L