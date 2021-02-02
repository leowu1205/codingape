# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:58:57 2021

@author: USER
"""
import time 
from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
import random
a = 0
while a < 50:
  print(a)
  a = a+1
  color = random.randint(0,8)
  x, y, z = mc.player.getTilePos()
  flower = 38
  time.sleep(0.2)
  mc.setBlock(x, y, z, flower, color)
  
