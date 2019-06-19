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
    login = Login()
    login.login_exists()
    login.doGuest()
     
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
    
    ####第一次抽卡不好匹配，先点到干员，再判断,重新验证
    sleep(2)
    pyautogui.click( random_W(162) , random_W(86) , 2 , 1 )#点击返回
    pyautogui.click(1500, 500, 1)#点干员按钮
    imagedif = imageDif()
    six_nums = imagedif.doIt()
    if six_nums > 0:
        print('first successd')
        return True
    else:
        print('first failed')
    pyautogui.click( random_W(162) , random_W(86) , 2 , 1 )#点击返回
    
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
    
    return False #返回flase为重复循环，True为终止循环刷

flag = False
count = 0
pyautogui.click(640, 1060, 1)#切换到模拟器
while flag == False:
    if count > 0:
        login = Login()
        login.login_exit()
        
    count += 1
    flag = mingri()
    print('---执行第'+ count +'次----')
    
