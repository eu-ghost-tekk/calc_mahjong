#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import glob
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm, trange
from IPython.display import display, Image

import preprocessing as PP
import resize as RS
import detect as DT
import geometric_transformation as GT

a_img_path = '/Users/mac/Desktop/sample/agari2.png'
DB_path = '/Users/mac/Desktop/sample/DB/'
split_path = '/Users/mac/Desktop/sample/split/'

##################################

def display_cv_image(image, format='.png'):
    decoded_bytes = cv2.imencode(format, image)[1].tobytes()
    display(Image(data=decoded_bytes))
    
img = cv2.imread(a_img_path)
display_cv_image(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filtered = cv2.GaussianBlur(gray, (5, 5), 0)

# 二値化
ret,th1 = cv2.threshold(filtered,200,255,cv2.THRESH_BINARY)
display_cv_image(th1)

# 輪郭抽出
image, contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 面積の大きいもののみ選別
areas = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 10000:
        epsilon = 0.020*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        areas.append(approx)

cv2.drawContours(img,areas,-1,(0,255,0),3)
display_cv_image(img)
display_cv_image(GT.transformation(img, areas[0]))



    
