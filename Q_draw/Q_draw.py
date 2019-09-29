# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:51:25 2019

@author: lenovo
"""
#n,m=tuple(map(int,input().split()))
#img = []
#for i in range(n):
#    img.append(list(input()))
n,m=6,5
img=[list('XBGBX'),list('YBBYB'),list('BGGXX'),list('XYYBG'),
     list('XYBGG'),list('YYXYX')]
i=0
result=0
while i<n:
    j = 0
    while j<m:
        if img[i][j] == 'Y' or img[i][j]=='G':
            result+=1
            ki,kj=i,j
            while ki<n and kj<m:
                if img[ki][kj]=='Y':
                    img[ki][kj]='X'
                elif img[ki][kj]=='G':
                    img[ki][kj]='B'
                else:
                    break
                ki,kj=ki+1,kj+1
        if img[i][j] == 'B' or img[i][j]=='G':
            result+=1
            ki,kj=i,j
            while ki<n and kj>=0:
                if img[ki][kj]=='B':
                    img[ki][kj]='X'
                elif img[ki][kj]=='G':
                    img[ki][kj]='Y'
                else:
                    break
                ki,kj=ki+1,kj-1
        j+=1
    i+=1
print(result)