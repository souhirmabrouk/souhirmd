# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:03:35 2020

@author: Asus
"""
# -----ex5---------------
def missing_char(st, n):
    st1= st.replace(st[n],'',1)
    return st1
str1 = input("enter your string \n")
n=int(input('enter the character index  :'))
if n in range (1,len(str1)) : 
    str2 = missing_char(str1,n)
    print(str2)
else : 
    print("error invalid input n")