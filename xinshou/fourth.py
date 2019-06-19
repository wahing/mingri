from common.functions import random_W, role_drap
import pyautogui
from time import sleep

class Fourth():
    def __init__(self):
        print(4)
        
    def formation(self):
#         pyautogui.click(640, 1060, 1)#切换到模拟器
        pyautogui.click( random_W(100) , random_W(100) , 6 , 2 )#点击屏幕
        sleep(2)
        pyautogui.click( random_W(840) , random_W(365) , 1 )#选中加号
        sleep(1)
        pyautogui.click( random_W(740) , random_W(321) , 1)#点击人物
        sleep(1)
        pyautogui.click( random_W(1685) , random_W(980) , 1 )#点击打勾
        sleep(1)
        pyautogui.click( random_W(410) , random_W(90) , 1 )#点击导航栏
        sleep(1)
        pyautogui.click( random_W(200) , random_W(370) , 1 )#点击首页
    
#     formation(1)
