# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:07:09 2020

@author: Asus
"""

# --------ex6------------------
text="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
print(text)
print()

text_crypted=''
for c in text:

    if(c=='y'):
         c1=ord('a')
    elif (c=='z'):
        c1=ord('b')
    elif (c==' '):
        c1=ord('*')
    else:
        c1=ord(c) +2

    text_crypted=text_crypted + chr(c1)
print(text_crypted)

