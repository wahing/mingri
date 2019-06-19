from PIL import ImageGrab
import cv2
import numpy as np
import pyautogui
from time import sleep


class imageDif():
    def __init__(self):
        sleep(3)
        print('image')
#         pyautogui.click(640, 1060, 1)#切换到模拟器
#         sleep(1)
#         pyautogui.click(1500, 500, 1)#点干员按钮

    def dif(self,big,small):
        floder = 'images/'
        suffix = '.png'
        big = floder + big + suffix
        small = floder + small + suffix
        img_bgr = cv2.imread(big)
        img_gray = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
         
        template = cv2.imread(small,0)
        # template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]
         
        #     methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
         
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        
        ret = 0
#         print(loc)
        if len(loc[0]):
            ret = 1
#         for pt in zip(*loc[::-1]):
#             cv2.rectangle(img_bgr,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
#         cv2.imshow('detected',img_bgr)
#         cv2.waitKey(0) 
        return ret
        
    def doIt(self):
        sleep(1)
        pos = (0,0,1920, 1080)
        cut_img = ImageGrab.grab(pos)
        floder = 'images/'
        suffix = '.png'
        big = 'screen'
        cut_img.save(floder + big + suffix) #保存截图到文件夹中
        print("screenshots sucess")
        character = ['ajln','sl','tjzw','yh','yy','xx']
#         character = ['moyao']
        ret = 0
        for small in character:
            ret += self.dif(big,small)
        return ret
    
# a = imageDif()
# x = a.doIt()
# print(x)