#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg
from PIL import Image
import time
import threading
im = ""
fig = ""
last = False
pos = []

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/autojump.png')
    os.system('adb pull /sdcard/autojump.png .')

def update(*args):
    pull_screenshot()
    img = mpimg.imread('autojump.png')
    im.set_data(img)
    return im,

def on_click(event):
    global last
    global pos
    x,y = event.xdata,event.ydata
    if last:
        last = False
        os.system("adb shell input swipe %s %s %s %s" % (int(pos[0]),int(pos[1]),int(x),int(y)))
        pos = []
        pass
    else:
        print("点击了 %s %s 坐标!" % (x,y))
        pos = [x,y]
        last = True


def main():
    global im
    global fig
    fig = plt.figure()
    pull_screenshot()
    img = mpimg.imread('autojump.png')
    im = plt.imshow(img, animated=True)
    ani = animation.FuncAnimation(fig, update, interval=50, blit=True)
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()
if __name__ == '__main__':
    main()
