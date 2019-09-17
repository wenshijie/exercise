# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:55:40 2019

@author: lenovo
"""

def user_password(s:str):
    n = len(set(s))
    return s+str(2**n-1)

if __name__ == '__main__':
    s = 'abc'
    print(user_password(s))
    