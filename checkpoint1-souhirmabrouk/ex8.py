# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:25:08 2020

@author: Asus
"""



#-------------------ex8----------------------------------------------------
import numpy as np
def covariance(x,y):
    return np.cov(x,y)

arr2=np.array([0, 1,2 ])
arr3=np.array([2 ,1 ,0])
coov=covariance(arr2,arr3)
print()
print(coov)
