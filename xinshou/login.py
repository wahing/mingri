from common.functions import *
import pyautogui
from time import sleep
from multiprocessing import sys
import win32clipboard as w
# import win32con
from common.name import *

class Login():
    def __init__(self):
        print('login')
#         pyautogui.click(640, 1060, 1)#切换到模拟器
        sleep(2)

    def doGuest(self):
        sleep(10)
        print('doGuest')
        pyautogui.click(1350, 980, 1)#点击账号管理
        
        sleep(2)
        pyautogui.click(1260, 750, 1)#点击游客登陆
        sleep(15)
        
        pyautogui.click(950, 970, 1)#点击下一步
        sleep(3)
        
        pyautogui.click(841, 612, 1)#点击姓名栏
        sleep(2)
        
        
        printname = Generate()
        settext(printname.name())#随机生成姓名
        
        pyautogui.hotkey('ctrl', 'v')#复制到剪切板
        
        pyautogui.typewrite(['enter'])#输入
        
        sleep(1)
        
        pyautogui.click(934, 733, 1)#点击登陆
        
        

    def login_exists(self):
        print('login_exists')
        phoneNumber = '18866478814'
        psw = '12345678a'
        
        pyautogui.click(1350, 980, 1)#点击账号管理
        sleep(1)
        pyautogui.click(640, 740, 1)#账户登陆
        
        sleep(1)
        pyautogui.click(940, 640, 1)#点击账号
        pyautogui.typewrite(['backspace'])
        sleep(1)
        pyautogui.typewrite(['backspace'])
        pyautogui.typewrite(phoneNumber,0.3)
        pyautogui.typewrite(['enter'])
        
        pyautogui.click(940, 710, 1)#点击密码
        sleep(1)
        settext(psw)    #复制到剪切板
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.typewrite(['enter'])
        
        pyautogui.click(940, 845, 1)#点击登陆
        
        pyautogui.click(1250, 750, 1)#点击确认删除
        sleep(5)
        self.login_exit()
        
    def login_exit(self):
        print('login_exit')
        sleep(15)
        pyautogui.click( random_W(1770) , random_W(115) , 1)#点击取消
         
        sleep(1)
        pyautogui.click( random_W(118) , random_W(88) , 1)#点击设置
         
        sleep(2)
        pyautogui.click( random_W(900) , random_W(755) , 1)#点击退出账号
         
        sleep(1)
        pyautogui.click( random_W(1250) , random_W(750) , 1)#点击确认退出
        
    def test(self):
        printname = Generate()
        settext(printname.name())#随机生成姓名
        
        pyautogui.hotkey('ctrl', 'v')#复制到剪切板
        
# a = Login()
# a.login_exists()
# a.login_exists()