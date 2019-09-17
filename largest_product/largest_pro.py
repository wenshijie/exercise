# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:56:50 2019

@author: lenovo
"""

def pri(m,a):
    if m<3:
        return 0
    result_p = [0,0,0]  # 正数
    result_n = [0,0,0]  # 负数
    num_0 = 0
    for i in a:
        if i>result_p[0]:  # 正数前3或包括0的前三大
            result_p[0]=i
            result_p.sort()
        if i<0:  # 负数前3或包括0的前三小
            if result_n[-1]==0:
                result_n[-1]=i
                result_n.sort()
            elif i<result_n[-1]:
                result_n[-1]=i
                result_n.sort()
        if i==0:
            num_0 += 1
    while result_p[0]==0:  # 删除正数列表中的0项
        del result_p[0]
        if not result_p:  # 如果都是0，删除完了
            break
    while result_n[-1]==0:  # 删除负数列表中的0项
        del result_n[-1]
        if not result_n:  # 如果都是0，删除完了
            break
    if num_0>0:
        result_0 = [0,0,0]  # 如果0超级多不至于占内存，用一个0的话return中可能溢出指针
    else:
        result_0 = []
    result = result_n+result_0+result_p
    return max(result[0]*result[1]*result[-1],result[-3]*result[-2]*result[-1])

def pri2(m,a):  # 分别求出max1，max2，max3，min2，min1
    if m<3:
        return 0
    def get_max(b:list):  # 求最大
        max_ = b[0]
        max_index = 0
        for i in range(len(b)):
            if b[i]>max_:
                max_ = b[i]
                max_index = i
        return max_,max_index
    def get_min(b:list):  # 求最小
        min_ = b[0]
        min_index = 0
        for i in range(len(b)):
            if b[i]<min_:
                min_ = b[i]
                min_index = i
        return min_,min_index
    max1,max_index = get_max(a)
    del a[max_index]
    max2,max_index = get_max(a)
    del a[max_index]
    max3,max_index = get_max(a)
    a.extend([max1,max2])
    min1,min_index = get_min(a)
    del a[min_index]
    min2,min_index = get_min(a)
    return max(min1*min2*max1,max1*max2*max3)

m = int(input())
a = list(map(int,input().split(' ')))
print(pri(m,a))
print(pri2(m,a))