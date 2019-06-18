from common.functions import random_W, role_drap
import pyautogui
from time import sleep

#用于第一次抽卡
class Third():
    def __init__(self):
        print(3)
        
    def doIt(self):
        pyautogui.click(682, 1060, 1)#切换到模拟器

        sleep(4)
        pyautogui.click( random_W(100) , random_W(100) , 1 , 1 )#点击屏幕
        
        sleep(5)
        pyautogui.click( random_W(1300) , random_W(945) , 1 , 1 )#点击寻访一次
        
        sleep(4)
        pyautogui.click( random_W(1760) , random_W(100) , 3 , 1 )#点击skip
        
        sleep(5)
        pyautogui.click( random_W(100) , random_W(100) , 1 , 1 )#点击屏幕
        

#     doIt(1)
        
        
        
        