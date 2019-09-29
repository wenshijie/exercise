# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:18:28 2019

@author: lenovo
"""

c=[2,5,1,3,2]
c.sort(reverse=True)
t=5
n = len(c)
results=[]
def orbital(i,s_t,res=[]):
    j=i+1
    if s_t==t:
        results.append(res)
    if s_t<t and j<n:
        orbital(j,s_t+c[j],res+[c[j]])
        orbital(j,s_t,res)
orbital(-1,0,[])
print([list(re) for re in set(map(tuple,results))])
    