# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:59:41 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

for i in range(0,16):
    mc.setBlock(x+i, y, z, 35, i)