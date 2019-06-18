from common.functions import random_W, role_drap
import pyautogui
from time import sleep
from multiprocessing import sys
from test.sortperf import doit

class First():
    def __init__(self):
        print(1)

    def doit(self):
        pyautogui.click(666, 1060, 1)#切换到模拟器
        #sys.exit() 
        pyautogui.click(random_W(1683), random_W(106), 1)#点击跳过    
        sleep(2)
        
        pyautogui.click( random_W(1298) , random_W(736) , 1 )#点击确定
        sleep(8)
        
        """
                进入教程
        """
        pyautogui.click(random_W(200), random_W(200), 18 , 3)#点击界面跳过对话
        
        role_drap([[1589,956,1.5,1],[862,621,4,2],[1481,615,2,2]])#拖拽第一个角色  
        sleep(3)#拖拽第一个角色并且等待
        
        pyautogui.click(random_W(200), random_W(200) , 3 , 2)#点击界面跳过对话 
        sleep(10)#等待
        
        pyautogui.click(random_W(200), random_W(200) , 2 , 3)#点击界面跳过对话
        
        role_drap([[1746,951,1.5,1],[1011,461,3,2],[1028,984,2,2]])#拖拽第二个角色
        
        pyautogui.click(random_W(200), random_W(200) , 5 , 3)#点击界面跳过对话 
        sleep(15)#等待战斗结束
        
        pyautogui.click(random_W(200), random_W(200) , 10 , 2)#点击界面跳过对话
    doit(1)


    


    
    