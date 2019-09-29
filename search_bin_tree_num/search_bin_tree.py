# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:21:45 2019

@author: lenovo
"""
"""
把n个数分解成根节点为1,2,...,n的数,则n个数的二叉搜索树的个数为
1为根节点则为后n-1个数组成的搜索树个数及dp[n-1]
2为根节点则为左树为1个数组成的,右子树为n-2个数组成的搜索树,dp[1]dp[n-2]
3为根节点左子树1,2,右子树4,5,...n,则为dp[2]*dp[n-3]
"""
# search_bin_tree
def search_bin_tree(n):
    dp=[0]*(n+1)
    dp[0],dp[1] = 1, 1
    for i in range(2,n+1):
        for j in range(i):
            dp[i] += dp[j]*dp[i-j-1]
    return dp[n]

if __name__=='__main__':
    result = search_bin_tree(4)