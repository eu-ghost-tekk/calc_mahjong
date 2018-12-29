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

#################物体検出##############
def detect_contour(path, min_size):
    contoured = cv2.imread(path)
    forcrop = cv2.imread(path)

    # 前処理
    hai = PP.binary_threshold(path)
    hai = cv2.bitwise_not(hai)

    # detect contour
    im2, contours, hierarchy = cv2.findContours(hai, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    crops = []
    # draw contour
    for c in contours:
        areas = cv2.contourArea(c)
        if areas < min_size:
            continue
        

        # rectangle area
        x, y, w, h = cv2.boundingRect(c)
        x, y, w, h = padding_position(x, y, w, h, 5)

        # crop the image
        cropped = forcrop[y:(y + h), x:(x + w)]
#        cropped = resize_image(cropped, (0, 0))
        crops.append(cropped)

        # draw contour
#        cv2.drawContours(contoured, c, -1, (0, 0, 255), 3)  # contour
        for i in range(15):
            cv2.rectangle(contoured, (x, y), (x + w//14*i, y + h), (0, 255, 0), 3)  #rectangle contour
            dst = contoured[y:(y + h), (x + w//14*i):(x + w//14*(i+1))]
            output = split_path + 'cut' + '%d' % i + '.jpg'
            cv2.imwrite(output, dst)
            
    return contoured, crops


def padding_position(x, y, w, h, p):
    return x - p, y - p, w + p * 2, h + p * 2