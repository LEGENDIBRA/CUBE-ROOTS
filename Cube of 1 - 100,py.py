# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:13:21 2022

@author: OLAOLUWA
"""

#CUBE ROOTS OF 1 - 100
#Using List Comprehension
First_Hundred_List = [x for x in range(0,10000000001,1)]
def Cube(x):
    high = abs(x)
    low = 0.0
    epsilon = .01
    ans  = (high + low)/2
    while abs(ans**3 - abs(x)) >= epsilon:
        if ans**3 > abs(x):
            high = ans
        else:
            low = ans
        ans = (high + low)/2
    if x < 0:
        ans = -ans
    return ans

def List_Cube_Root(L, f):
    for i in range (len(L)):
        L[i] = f(L[i])
    return L

print(List_Cube_Root(First_Hundred_List, Cube))

