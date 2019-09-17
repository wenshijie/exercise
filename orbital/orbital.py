# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:18:28 2019

@author: lenovo
"""

def orbital(c:list,t:int):
    p_ways = []  # possible way 可能的拼图
    p_dict = {}  # 可能的拼图组合    
    for i in c:
        if c<=t:
            p_ways.append(i)
            p_dict[i]=i  # 长度为i的路径可能的组合
    