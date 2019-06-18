'''
Created on 2019年6月14日

@author: wahing
'''
import random
import pyautogui

#type = 1时为x,y轴坐标,2时为拖拽时常
def random_W(W, rtype=1,v=[-2,2]):
    if rtype == 1:
        W = W + random.randint(v[0],v[1])
    else:
        if not v:
            v = [-0.2,0.2]
        W = W + round(random.uniform(v[0],v[1]),2)
    return W
    
#xyArr是一组角色移动的开始到结束的xy轴坐标加拖动事件的数组,例:[[350，740,1.5,1],[1373，390 ,2.5,1]]
#xyArr[[x,y,times,rtype]]
#rtype=1为moveTo，2为dragTo
def role_drap(xyArr):
    for xy in xyArr:
        if xy[3] == 1:
            pyautogui.moveTo(random_W(xy[0]),random_W(xy[1]),random_W(xy[2],2),
                             pyautogui.easeInBounce)
        elif xy[3] == 2:
            pyautogui.dragTo(random_W(xy[0]),random_W(xy[1]),random_W(xy[2],2),
                             button='left')

