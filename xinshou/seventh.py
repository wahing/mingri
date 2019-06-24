from common.functions import random_W, role_drap
import pyautogui
from time import sleep
from xinshou.imageDif import imageDif
from tkinter import messagebox
from xinshou.common.buttons import *


class Seventh():
    def __init__(self):
        print(7)
        
    def doit(self):
#         pyautogui.click(640, 1060, 1)#切换到模拟器
        sleep(5)
        pyautogui.click( random_W(162) , random_W(86) , 2 , 1 )#点击返回
         
        sleep(12)
        pyautogui.click( random_W(1745) , random_W(121) , 2 , 2 )#点击关闭签到
        
         
        sleep(3)
        pyautogui.click( random_W(60) , random_W(50) , 1 )#点击屏幕
        
        sleep(3)
        pyautogui.click( random_W(520) , random_W(850) , 1 )#点击合成玉石
        
        sleep(3)
        pyautogui.click( random_W(500) , random_W(1000) , 1 )#点击屏幕
        
        sleep(3)
        pyautogui.click( random_W(274) , random_W(351) , 1 )#点击新手任务
        
        sleep(3)
        pyautogui.click( random_W(1500) , random_W(300) , 1 )#点击合成与
        
        sleep(3)
        pyautogui.click( random_W(400) , random_W(400) , 1 )#点击屏幕
        
        sleep(3)
        pyautogui.click( random_W(1785) , random_W(140) , 1 )#点击关闭
        
        sleep(5)
        pyautogui.click( random_W(1773) , random_W(115) , 2 , 1 )#点击活动公告
        
        #第一次抽卡不好匹配，先验证一遍
#         messagebox.showinfo('先验证有没有6星', '先验证前面有没有6星')
        pyautogui.click(1500, 500, 1)#点干员按钮
        sleep(2)
        imagedif = imageDif()
        six_nums = imagedif.doIt()
        if six_nums > 0:
            print('first successd')
            return True;
        else:
            print('first failed')
        sleep(5)
        pyautogui.click( random_W(162) , random_W(86) , 1 , 1 )#点击返回
        
        
#         sleep(3)
#         pyautogui.click( random_W(1760) , random_W(100) , 2 , 1 )#点击skip
#         pyautogui.click( random_W(100) , random_W(100) , 1 , 1 )#点击屏幕
        
        sleep(2)
        pyautogui.click( random_W(320) , random_W(90) , 1 )#点击邮件
        
        sleep(2)
        pyautogui.click( random_W(1640) , random_W(960) , 1 )#点击合成玉
        
        sleep(2)
        pyautogui.click( random_W(60) , random_W(50) , 1 )#点击屏幕
        
        sleep(8)
        pyautogui.click( random_W(170) , random_W(100) , 1 )#点击返回
        
        sleep(4)
        pyautogui.click( random_W(1680) , random_W(760) , 1 )#点击干员寻访
        
        sleep(2)
        pyautogui.click( random_W(1585) , random_W(940) , 1 )#点击寻访十次
        
        sleep(2)
        pyautogui.click( random_W(1320) , random_W(730) , 1 )#点击确定
        
        sleep(20)
        pyautogui.click( random_W(1750) , random_W(95) , 1 )#点击skip
        blank(3)
        
        back()
        sleep(2)
        messagebox.showinfo('1')
        pyautogui.click( random_W(1156) , random_W(535) , 1 )#点击编队
        blank(3)
        pyautogui.click( random_W(1464) , random_W(93) , 1 )#点击快捷编队
        sleep(3)
        pyautogui.click( random_W(1700) , random_W(970) , 1 )
        sleep(1)
        back()
        
        
        
        #最后看是否抽到
        sleep(1)
        pyautogui.click(1500, 500, 1)#点干员按钮
        imagedif = imageDif()
        six_nums = imagedif.doIt()
        if six_nums > 1:
            print('second successd')
            return True
        else:
            print('second failed')
        sleep(3)
        back()  #点击返回
#     doit(1)  
        