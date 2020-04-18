# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:09:30 2020

@author: Asus
"""

#*************************************
#ex2

x=input ("enter your number ")
i=int(x)
fact=1
for j in range(1,i+1):
   fact = fact*j
print ('le factoriel de',i, "est",fact)
    