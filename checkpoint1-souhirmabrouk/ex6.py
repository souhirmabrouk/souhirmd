# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:47:52 2020

@author: Asus
"""

# this program runs on python 2.7 but in python 3 maketrans is not defined 
# I tested it on python 2.7 and it worked 

from string import maketrans  

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
text1 = maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
print(text.translate(text1))