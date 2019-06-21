from common.functions import random_W, role_drap
import pyautogui
from time import sleep

class Sixth():
    def __init__(self):
        print(6)
        
    def doit(self):
#         pyautogui.click(640, 1060, 1)#切换到模拟器
        sleep(3)
        
        pyautogui.click( random_W(700) , random_W(600) , 20 , 1.5 )#点击屏幕    
        
        pyautogui.click( random_W(450) , random_W(905) , 3 , 1 )#点击领取
        pyautogui.click( random_W(700) , random_W(600) , 5 , 1.5 )
        
        sleep(15)
        
        pyautogui.click( random_W(1580) , random_W(966) , 9 , 1 )#点击开始行动
        sleep(5)
        
        pyautogui.click( random_W(1580) , random_W(730) , 15 , 1 )#点击开始
        sleep(6)
        
        pyautogui.click(random_W(1683), random_W(106), 1)#点击跳过    
        sleep(2)

        pyautogui.click( random_W(1300) , random_W(750) , 1 )#点击确定
        
        sleep(3)
        
        role_drap([[1590,950,2,1] , [1340,490,3,2] , [990,543,2,2]])#拖拽第一个角色
        sleep(2)
        role_drap([[1750,950,2,1] , [1390,660,3,2] , [1050,680,2,2]])#拖拽第二个角色
        
        sleep(35)
        
        pyautogui.click( random_W(450) , random_W(905) , 10 , 1 )#跳过对话
        
        role_drap([[1740,940,2,1] , [1280,396,4.5,2] , [1280,760,3,2]])#拖拽奶妈
        
        sleep(35)
        pyautogui.click( random_W(450) , random_W(905) , 5 , 3 )#跳过对话
#     doit(1)   