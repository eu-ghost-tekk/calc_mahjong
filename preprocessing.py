#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import glob
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm, trange

import preprocessing as PP
import resize as RS
import detect as DT
import geometric_transformation as GT

a_img_path = '/Users/mac/Desktop/sample/agari2.png'
DB_path = '/Users/mac/Desktop/sample/DB/'
split_path = '/Users/mac/Desktop/sample/split/'

#################前処理######################
# グレースケール化関数
def to_grayscale(path):
    img = cv2.imread(a_img_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

# ブラー
def blur(img):
    filtered = cv2.GaussianBlur(img, (3, 3), 0)
    return filtered

# 閾値処理
def binary_threshold(path):
    gray_img = to_grayscale(path)
    filterd_img = blur(gray_img)
    under_thresh = 20
    upper_thresh = 160
    maxValue = 255
    th, drop_back = cv2.threshold(filterd_img, under_thresh, maxValue, cv2.THRESH_BINARY)
    th, clarify_born = cv2.threshold(filterd_img, upper_thresh, maxValue, cv2.THRESH_BINARY_INV)
    merged = np.minimum(drop_back, clarify_born)
    
    return merged
