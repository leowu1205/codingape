# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:29:26 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange
r = randrange(0, 16)
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
    
        if data == r:
            mc.postToChat("恭喜你找到我")
            mc.setBlock(hit.pos, 57)
            break
        elif data < r:
            mc.postToChat("找錯囉! 找找看更小的顏色 ID 吧")
        elif data > r:
            mc.postToChat("找錯囉! 找找看更大我顏色 ID 吧")