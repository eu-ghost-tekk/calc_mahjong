#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:34:59 2018

@author: mac
"""
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def binary_threshold(img):
    under_thresh = 20
    upper_thresh = 160
    maxValue = 255
    th, drop_back = cv2.threshold(img, under_thresh, maxValue, cv2.THRESH_BINARY)
    th, clarify_born = cv2.threshold(img, upper_thresh, maxValue, cv2.THRESH_BINARY_INV)
    merged = np.minimum(drop_back, clarify_born)
    
    return merged

# 元画像
img = cv2.imread('/Users/mac/Desktop/sample/agari2.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


binary_img = binary_threshold(gray_img)
plt.imshow(binary_img)