# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:07:54 2020

@author: Asus
"""

#----------------ex7-------------------------------------------------------
import numpy as np

def conversion(arr):
    return arr.tolist()

arr1=np.array([[1,2],[3,4],[5,6]])
print(arr1)
L=conversion(arr1)
print(L)