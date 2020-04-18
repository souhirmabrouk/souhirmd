# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:25:43 2020

@author: Asus
"""

    
#**************************************
#ex4
# input a sequense of comma separated values 
import math as m
C=50
H=30
L = [int(x) for x in input("Enter multiple values\n").split(',')] 
print("\nThe values of input are", L)  
def calcul(D):
    return round(m.sqrt(2*C*D/H))

for D in L:
    Q=calcul(D)
    print(Q, end=',')
    
#*******************************************
