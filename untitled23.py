# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:08:36 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create("gce.racterub.me")
from random import randrange
from time import time

def binarySearch():
    sTime = time()
    low = 0 
    top = 10000000
    
    while low <= top:
        mid = (low + top) // 2
        
        if mid < number:
            low = mid + 1
            
        elif mid > number:
            top = mid - 1
        else:
            print("找到答案了 ! 是" + str(mid))
            print("二元搜尋法 : 花了 " + str(time() - sTime) + "秒")
            break
        
number = randrange(1, 10000001)
binarySearch()
            