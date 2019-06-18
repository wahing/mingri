from PIL import ImageGrab
import cv2
import numpy as np
import pyautogui
from asyncio.tasks import sleep


class imageDif():
    def __init__(self):
        sleep(5)
        print('image')
#         pyautogui.click(555, 1420, 1)#切换到模拟器
        
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
        threshold = 0.6
        loc = np.where(res >= threshold)
        
        ret = 0
        if len(loc[0]):
            ret = 1
#         for pt in zip(*loc[::-1]):
#             cv2.rectangle(img_bgr,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
#         cv2.imshow('detected',img_bgr)
#         cv2.waitKey(0) 
        return ret
        
    def doIt(self):
        pos = (0,0,1920, 1080)
        cut_img = ImageGrab.grab(pos)
        floder = 'images/'
        suffix = '.png'
        big = 'screen'
        cut_img.save(floder + big + suffix) #保存截图到文件夹中
        print("screenshots sucess")
        character = ['ajln','sl','tjzw','yh','yy']
        ret = 0
        for small in character:
            ret += self.dif(big,small)
        return ret
    

# a = imageDif()
# x = a.doIt()
# print(x)