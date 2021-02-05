# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:35:27 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time 
mc=Minecraft.create()
time.sleep(1)
x, y, z = mc.player.getTilePos()
mc.setBlock(x, y, z, 49)
mc.setBlock(x, y+1, z, 49)
mc.setBlock(x, y+2, z, 49)
mc.setBlock(x, y+3, z, 49)
mc.setBlock(x, y+4, z, 49)
mc.setBlock(x, y+4, z+1, 49)
mc.setBlock(x, y+4, z+2, 49)
mc.setBlock(x, y+3, z+2, 49)
mc.setBlock(x, y+2, z+2, 49)
mc.setBlock(x, y+2, z+1, 49)
mc.setBlock(x, y+2, z, 49)
mc.setBlock(x, y, z+6, 49)
mc.setBlock(x, y+1, z+6, 49)
mc.setBlock(x, y+2, z+6, 49)
mc.setBlock(x, y+3, z+6, 49)
mc.setBlock(x, y+4, z+6, 49)
mc.setBlock(x, y+4, z+5, 49)
mc.setBlock(x, y+4, z+7, 49)