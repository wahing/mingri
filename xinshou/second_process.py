from common.functions import random_W, role_drap
import pyautogui
from time import sleep

class Second():
    def __init__(self):
        print(2)

    def doit(self):
#         pyautogui.click(682, 1060, 1)#切换到模拟器
        sleep(2)
        
        pyautogui.click( random_W(250) , random_W(250) , 3 , 1.5 )#跳过对话
        sleep(10)#等待
        
        pyautogui.click( random_W(250) , random_W(250) , 5 , 1.5 )#跳过对话然后准备点击技能
        sleep(25)
        
        pyautogui.click( random_W(704) , random_W(466) , 6 , 1 )#点击技能介绍
        pyautogui.click( random_W(1278) , random_W(627) , 6 , 1 )#使用技能
        sleep(5)#技能释放然后等待
        
        pyautogui.click( random_W(250) , random_W(250) , 5 , 1.5 )#跳过对话
        sleep(10)#等待对话
        
        pyautogui.click( random_W(300) , random_W(300) , 6 , 1.5 )#跳过对话出现教官
        sleep(15)#等待战斗结束
        
        pyautogui.click( random_W(971) , random_W(111) , 5 , 1.5 )#跳过对话出现驴
        sleep(20)#等待动画
        
        pyautogui.click( random_W(872) , random_W(517) , 5 , 1.5 )#跳过对话，出现敌方支援
        sleep(5)#敌方动画
        
        pyautogui.click( random_W(372) , random_W(517) , 3 , 1.5 )#我方出现支援
        sleep(3)#我方动画
        
        pyautogui.click( random_W(343) , random_W(769) , 3 , 1.5 )#跳过对话
        sleep(50)#等待战斗结束
        
        pyautogui.click( random_W(300) , random_W(300) , 8 , 1.5 )#跳过对话
        
        pyautogui.click(random_W(1683), random_W(106), 1)#点击跳过    
        sleep(2)
        
        pyautogui.click( random_W(1298) , random_W(736) , 1 )#点击确定
    
#     doit(1)
