# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:17:57 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def building(x, y, z, base=18):
    height = (base//2) + 1

    for i in range(height):
        x1 = x + i
        y1 = y + i
        z1 = z + i
    
        x2 = x + base - i
        #y與y2相同
        z2 = z + base - i
        mc.setBlocks(x1, y1, z1, x2, y1, z2, 24)
    
    x,y,z = mc.player.getTilePos()
    building(x, y, z, 9)
    
