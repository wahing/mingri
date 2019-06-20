from common.functions import random_W, role_drap
import pyautogui
from time import sleep
from xinshou.imageDif import imageDif
from tkinter import messagebox

#用于第一次抽卡
class Third():
    def __init__(self):
        print(3)
        sleep(10)
        
    def doIt(self):
        #pyautogui.click(640, 1060, 1)#切换到模拟器
        sleep(10)
        pyautogui.click( random_W(100) , random_W(100) , 20 , 1 )#点击屏幕
        
        sleep(10)
        messagebox.showinfo('点击寻访按钮', '点击寻访按钮')
        pyautogui.click( random_W(1300) , random_W(945) , 5 , 1 )#点击寻访一次
        
        sleep(5)
        pyautogui.click( random_W(1760) , random_W(100) , 1 , 1 )#点击skip
        
        #第一次抽卡不好匹配，先验证一遍
        imagedif = imageDif()
        six_nums = imagedif.doIt()
        if six_nums > 0:
            print('first successd')
            exit()
        else:
            print('first failed')
        
        sleep(5)
        pyautogui.click( random_W(1760) , random_W(100) , 2 , 1 )#点击skip
        pyautogui.click( random_W(100) , random_W(100) , 1 , 1 )#点击屏幕
        

    #doIt(1)
        
        
        
        