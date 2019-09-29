# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:55:35 2019

@author: lenovo
"""
"""
distance=[1,12,-5,-6,50,3]
[1, 13, 8, 2, 52, 55] 前n项的和
0.5 2/4 
10.4 52/5
9.17 55/6
[1, 13, 8, 1, 51, 54] 从第k项每项减去distance的第一项
12.75 51/4
10.8 54/5
[1, 13, 8, 1, 39, 42] 从第k+1项每项减去distance的第二项
10.5 42/4
"""

distance=[1,12,-5,-6,50,3]
k = 4
distance = [1,5,7,10,-6,-8,7,6]
k = 3

def fast_speed(distance,k):
    n = len(distance)
    fs_max = 0
    sum_dis = [distance[0]]
    for i in range(1,n):
        sum_dis.append(sum_dis[-1]+distance[i])
    i = 0
    k = k-1
    while k<n:
        for j in range(k,n):
            fs = sum_dis[j]/(j-i+1)
            #print(fs)
            if fs>fs_max:
                fs_max = fs 
            sum_dis[j] = sum_dis[j]-distance[i]
        k += 1
        i += 1
        
    return float('%.2f' % fs_max)

if __name__ == '__main__':
    print(fast_speed(distance,k))
            