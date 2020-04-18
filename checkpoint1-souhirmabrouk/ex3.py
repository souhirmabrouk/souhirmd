# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:09:50 2020

@author: Asus
"""

#*************************************
#ex3
def carree(n):
    return n*n
n=input("enter your number")
n=int(n)
dict={
      1:1}
for i in range (2,n+1):
    dict[i]=carree(i)
print()
print(dict)