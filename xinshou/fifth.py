from common.functions import random_W, role_drap
import pyautogui
from time import sleep



class Fifth():
    def __init__(self):
        print(5)
        
    def doit(self):
#         pyautogui.click(640, 1060, 1)#切换到模拟器
        sleep(3)
        pyautogui.click( random_W(200) , random_W(300) , 4 ,1 )#点击2下屏幕
        sleep(2)
        
        pyautogui.click( random_W(635) , random_W(502) , 1 )#选择章节
        sleep(2)
        
        pyautogui.click( random_W(944) , random_W(505) , 3 , 1 )#选择关卡
        sleep(3)
        
        pyautogui.click( random_W(1655) , random_W(948) , 1 )#开始行动
        sleep(3)
        
        pyautogui.click( random_W(944) , random_W(505) , 3 , 1 )#跳过对话
        sleep(3)
        
        pyautogui.click( random_W(1600) , random_W(750) , 1 )#开始行动
        sleep(5)
        
        pyautogui.click(random_W(1683), random_W(106), 1)#点击跳过    
        sleep(2)
    
        pyautogui.click( random_W(1298) , random_W(736) , 1 )#点击确定
        sleep(5)
        
        pyautogui.click( random_W(200) , random_W(300) , 5 , 2 )#点击1下屏幕
        sleep(1.5)
        """
                        拖拽角色
        """
        
        role_drap([[1266,953,1.5,1] , [1040,462,3,2] , [1200,462,2,2]])
        sleep(6)
        role_drap([[1260,950,1.5,1] , [1058,542,3,2] , [1280,542,2,2]])
        sleep(70)
        
        pyautogui.click(random_W(1683), random_W(106), 1)#点击跳过    
        sleep(2)
    
        pyautogui.click( random_W(1298) , random_W(736) , 1 )#点击确定
#     doit(1)