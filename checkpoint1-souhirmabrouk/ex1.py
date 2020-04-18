# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:09:02 2020

@author: Asus
"""

#************************************
# ex1
nums = []
for i in range(2000,3201):
   if (i % 7 == 0 and i % 5 !=0):
        nums.append(i)
print(nums)