'''
Created on 2019年6月14日

@author: wahing
'''
import random
import pyautogui
from common.functions import random_W
# import win32clipboard as w
# import win32con

#点击返回
def back(counts=1,times=1):
    pyautogui.click( random_W(162) , random_W(86) , counts, times )
    
#点击空白处
def blank(counts=1,times=1):
    pyautogui.click( random_W(60) , random_W(50) , counts , times )

#点击设置
def settings(counts=1,times=1):
    pyautogui.click( random_W(118) , random_W(88) , counts , times )