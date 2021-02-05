# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:07:34 2021

@author: USER
"""

from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
x, y, z = mc.player.getPos()
mc.setSign (x, y, z, 68, 0, "我愛", "Minecraft", "", "也愛 python")