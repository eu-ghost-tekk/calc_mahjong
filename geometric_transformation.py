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

##########################

def transformation(img, area):
    dst = []

    pts1 = np.float32(area)
    pts2 = np.float32([[560,60],[560,0],[0,0],[0,60]])

    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(img,M,(560, 60))
    
    return dst


    
