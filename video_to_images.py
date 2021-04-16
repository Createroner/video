#-------------------------------------#
#   调用摄像头或者视频进行检测
#   调用摄像头直接运行即可
#   调用视频可以将cv2.VideoCapture()指定路径
#-------------------------------------#
import time

import cv2
import numpy as np
from PIL import Image

from frcnn import FRCNN
import os
#-------------------------------------#
#   调用摄像头
#   capture=cv2.VideoCapture("1.mp4")
#-------------------------------------#


vidio_name = r'test02'
os.makedirs(vidio_name, exist_ok=True)

vidio_path = r'demo/test02.avi'

capture=cv2.VideoCapture(vidio_path)




capture.set(cv2.CAP_PROP_FPS, 0.1)
weight = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'MJPG')


frames_num=capture.get(7)
fps = 0.0

timeF = 1
c = 0
while (capture.isOpened()):

    ret,frame=capture.read()
    c = c +1
    if (c%timeF==0):

        if ret == True:

            cv2.imwrite('{}/{}.jpg'.format(vidio_name,c),frame)

        else:
            break
capture.release()
cv2.destroyAllWindows()

