# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:05:22 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create("104.199.150.71")
from random import randrange
import time
red = 14
yellow = 4
green = 5
#red = 38度
#yellow = 37度
#orange = 36度
playerID = mc.getPlayerEntityId("MIUESXO")
mc.executeCommand("tp MIUESXO -450 63 472")
mc.postToTitle(playerID, "疫情在中國爆發")
time.sleep(3)
mc.postToTitle(playerID, "我要趕快離開這裡了","目標:離開中國")
time.sleep(3)
mc.executeCommand("tp MIUESXO -346 132 425")
playerID = mc.getPlayerEntityId("MIUESXO")
mc.postToTitle(playerID, "歡迎搭乘XX航空")
time.sleep(3)
mc.postToTitle(playerID, "在幾分鐘後","即將抵達台灣")
time.sleep(8)
mc.executeCommand("tp MIUESXO -428 67 309")
mc.postToTitle(playerID, "歡迎來到台灣")
time.sleep(3)
mc.executeCommand("tp MIUESXO -534 64 325")
mc.postToTitle(playerID, "請配合測量體溫","這裡是入境大廳")

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        p = -383
    
        if data == red:
            mc.postToChat("38 fever")
            time.sleep(1)
            mc.executeCommand("tp MIUESXO -502 86 281")
            mc.postToTitle(playerID, "立刻集中隔離","這裡是醫院")
            time.sleep(0.5)
            mc.executeCommand("tp MIUESXO -502 86 275")
            time.sleep(1)
            mc.executeCommand("tp MIUESXO -515 86 275")
            time.sleep(1)
            mc.executeCommand("tp MIUESXO -528 87 275")
            time.sleep(1)
            mc.executeCommand("tp MIUESXO -538 86 287")
            time.sleep(1)
            mc.executeCommand("tp MIUESXO -548 86 287")
            time.sleep(1)
            mc.executeCommand("tp MIUESXO -565 86 304")
            time.sleep(1)
            mc.executeCommand("tp MIUESXO -570 86 304")
            time.sleep(1)
            mc.executeCommand("tp MIUESXO -570 87 301")
            mc.postToTitle(playerID, "慢慢的隔離吧","這裡是隔離區")
            while True:
                mc.executeCommand("tp MIUESXO -570 87 301")
                time.sleep(1)
        elif data == yellow:
            mc.postToChat("37 good")
            time.sleep(1)
            mc.executeCommand("tp MIUESXO -380 83 394")
            mc.postToChat("請隔離14天才能出去")
            time.sleep(14)
            mc.postToChat("隔離結束恭喜你重獲自由記得不要去人潮多的地方")
            mc.executeCommand("tp MIUESXO -316 64 334")
            break
        elif data == green:
            mc.postToChat("36 very good")
            time.sleep(1)
            mc.executeCommand("tp MIUESXO -380 83 394")
            mc.postToChat("請隔離14天才能出去")
            time.sleep(14)
            mc.postToChat("隔離結束恭喜你重獲自由記得不要去人潮多的地方")
            mc.executeCommand("tp MIUESXO -316 64 334")
            break
