# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:54:53 2021

@author: USER
"""

from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
x, y, z = mc.player.getTilePos()
try:
 blockType = int(input("請輸入你要的方塊ID:"))
 mc.setBlock(x, y, z, blockType)
except:
 print("只能輸入數字喔!!")