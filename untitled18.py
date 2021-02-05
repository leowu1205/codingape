# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:55:00 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
number = 1
x, y, z = mc.player.getTilePos()
for i in range(8):
    for j in range(number):
        mc.spawnEntity(x, y, z, 60)
    number = number*2
    mc.postToChat("這次生成了 " + str(number) + "隻蠹魚")
    time.sleep(1)