# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:53:08 2021

@author: USER
"""

from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit = hits[0]
        x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
        mc.player.setPos(x,y,z)
        mc.spawnEntity(x, y, z, 99)