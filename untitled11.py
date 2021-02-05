# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:13:46 2021

@author: USER
"""

from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
#entity
x, y, z = mc.player.getPos()
mc.spawnEntity(x, y, z, 93)
