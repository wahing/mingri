from xinshou.first import First
from xinshou.second_process import Second
from xinshou.third import Third
from xinshou.fourth import Fourth
from xinshou.fifth import Fifth
from xinshou.sixth import Sixth
from xinshou.seventh import Seventh
from xinshou.imageDif import imageDif
import pyautogui
from xinshou.login import Login
from common.functions import random_W, role_drap
from time import sleep

def mingri():
    first = First()
    first.doit()
          
    second = Second()
    second.doit()
       
    third = Third()
    third.doIt()
           
    fourth = Fourth()
    fourth.formation()
       
    fifth = Fifth()
    fifth.doit()
       
    sixth = Sixth()
    sixth.doit()
    
    seventh = Seventh()
    seventh.doit()
    
    #最后看是否抽到
    pyautogui.click(1500, 500, 1)#点干员按钮
    imagedif = imageDif()
    six_nums = imagedif.doIt()
    if six_nums > 1:
        print('second successd')
        return True
    else:
        print('second failed')
    pyautogui.click( random_W(162) , random_W(86) , 2 , 1 )#点击返回
    
    return False #返回false为重复循环，True为终止循环刷

    
currentExec = 1  #当前执行窗口数量
maxExec = 6   #最大执行窗口数
def Go():
    pyautogui.click(640, 1060, 1)#切换到模拟器
    pyautogui.click(587, 983, 1)#切换到第一个窗口
    
    global currentExec,maxExec
    flag = False
    login = Login()
    if currentExec== 1:
        count = 1
    else:
        count = 0
    while flag == False:
        if count > 0:
            login.login_exists()
    #         login.login_exit()
            login.doGuest(True)
        else:
            login.doGuest()
        
        flag = mingri()
        count += 1
        print('---执行第'+str(currentExec)+'个窗口'+'第'+ str(count) +'次执行----')
    
    currentExec += 1
    pyautogui.click(1860, 15, 1)#关闭模拟器
    sleep(1)
    pyautogui.click(1104, 596, 1)#点击退出按钮
    if currentExec > maxExec: #当完成最大数后退出程序
        exit()
    else:
        Go()
        
Go()
