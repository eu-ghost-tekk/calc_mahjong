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

########################
#
#Collect = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 15, 16, 17, 18, 19, 19, -1, -1]
#
#def picIdentification(DB, Query):
#    index = []
#    for i, q in enumerate(tqdm(Query)):
#        q = q.astype(np.float32)
#        minDif = 9999999999
#        totalDiffPoint = 0
#        for j, d in enumerate(DB):
#            d = d.astype(np.float32)
#            totalDiffPoint = sum(sum(sum(abs(q - d))))
#            if totalDiffPoint < minDif:#より小さい値に更新
#                minDif = totalDiffPoint
#                index[i] = j #index記録   
#        #print(i, minDif, index[i]//10, Collect[i])
##    for i in range(len(index)):
##        index[i] = index[i] // nPicPerPerson
#    return index

########################
# 元画像
img = cv2.imread(a_img_path)
plt.imshow(img)

a, b = DT.detect_contour(a_img_path, 100)
plt.imshow(a)

#DB_files= []
#DB = []
#
#DB_files = sorted(glob.glob(DB_path + '*.jpg'))
#for i in range(len(DB_files)):
#    img = cv2.imread(DB_files[i]) 
#    DB.append(img)
#
#
#Query_files = []
#Query = []
#
#Query_files = sorted(glob.glob(split_path + '*.jpg'))
#for i in range(len(Query_files)):
#    img = cv2.imread(Query_files[i])
#    Query.append(img)


    

    






