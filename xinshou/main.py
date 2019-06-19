from xinshou.first import First
from xinshou.second_process import Second
from xinshou.third import Third
from xinshou.fourth import Fourth
from xinshou.fifth import Fifth
from xinshou.sixth import Sixth
from xinshou.seventh import Seventh
import sys
from xinshou.imageDif import imageDif
import pyautogui
from xinshou.login import Login

# login = Login()
# login.doGuest()

first = First()
first.doit()
 
second = Second()
second.doit()
 
third = Third()
third.doIt()
 
#第一次抽卡不好匹配，先验证一遍
imageDif = imageDif()
six_nums = imageDif.doIt()
if six_nums > 0:
    print('first successd')
    sys.exit()
else:
    print('first failed')
     
fourth = Fourth()
fourth.formation()
 
fifth = Fifth()
fifth.doit()
 
sixth = Sixth()
sixth.doit()

#第一次抽卡不好匹配，先点到干员，再判断,重新验证
pyautogui.click(1500, 500, 1)#点干员按钮
imageDif = imageDif()
six_nums = imageDif.doIt()
if six_nums > 0:
    print('first successd')
    sys.exit()
else:
    print('first failed')


seventh = Seventh()
seventh.doit()

#最后看是否抽到
pyautogui.click(1500, 500, 1)#点干员按钮
six_nums = imageDif.doIt()
if six_nums > 1:
    print('second successd')
    sys.exit()
else:
    print('second failed')