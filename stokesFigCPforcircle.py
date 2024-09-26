# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib as mpl


#LC is at 45 degree to camera, the panels of 0 degree and 90 degree are for circular polarizations.
def CalS3(imName):
    os.chdir("C:/Users/Laboratorio/StokeMatix/CaptureHub/27.05big image")
    
        
    print(imName)
    openName="h"+str(imName) #"green"+
    # print(imName[i])
    saveName="new_h"
    im=plt.imread(openName+".tif")
    print(openName+".tif")



    im1=im[:,:,1] # green channel
    
    mpl.rcParams['font.size'] = 20
    # im_45=im_45withlabel[120:620,100:600] # adjust these arraies to make the light in the center
    leftP=im1[0:2048,0:1223]
    rightP=im1[0:2048,1224:2448]
    
    im_0=leftP[420:920,390:890] #(380:960,350:930)
    im_45=leftP[1420:1920,390:890] #(1380:1960,350:930)
    
    im_n45=rightP[420:920,390:890]
    im_90=rightP[1420:1920,390:890]
    
    x0,y0=250,250
    r=200
    
    lenx_0,leny_0=im_0.shape
    # print(lenx_0,leny_0)       
    newcircle_0=im_0.copy()
    sum_pixels_0 = 0
    count_pixels_0 = 0
    for i0 in range(lenx_0):  
        for j0 in range(leny_0):
            distance_squared = (i0 - x0) ** 2 + (j0 - y0) ** 2
            if distance_squared > r ** 2:             
                newcircle_0[i0,j0]=0
            else:
                sum_pixels_0 += im_n45[i0,j0]
                count_pixels_0 += 1
                
    lenx_90,leny_90=im_90.shape
    # print(lenx_90,leny_90)       
    newcircle_90=im_90.copy()
    for i1 in range(lenx_90):  
        for j1 in range(leny_90):
            distance_squared = (i1 - x0) ** 2 + (j1 - y0) ** 2
            if distance_squared > r ** 2:             
                newcircle_90[i1][j1]=0
                
    lenx_45,leny_45=im_45.shape
    # print(lenx_45,leny_45)       
    newcircle_45=im_45.copy()
    for i2 in range(lenx_45):  
        for j2 in range(leny_45):
            distance_squared = (i2 - x0) ** 2 + (j2 - y0) ** 2
            if distance_squared > r ** 2:             
                newcircle_45[i2][j2]=0
                
    lenx_n45,leny_n45=im_n45.shape
    # print(lenx_n45,leny_n45)       
    newcircle_n45=im_n45.copy()
    for i3 in range(lenx_n45):  
        for j3 in range(leny_n45):
            distance_squared = (i3 - x0) ** 2 + (j3 - y0) ** 2
            if distance_squared > r ** 2:             
                newcircle_n45[i3][j3]=0
    
    
    norm_0=newcircle_0/255
    norm_n45=newcircle_n45/255
    norm_45=newcircle_45/255
    norm_90=newcircle_90/255
    
    S0_H=norm_0+norm_90
    S0_45=norm_45+norm_n45
    S_avg=(S0_H+S0_45)/2
    epsilon = 1e-30
    S_avg_safe = np.where(S_avg == 0, epsilon, S_avg)
    S0_norm=S_avg_safe/S_avg_safe
    
    sum_pixels_0 = 0
    count_pixels_0 = 0
    for i0 in range(lenx_0):  
        for j0 in range(leny_0):
            distance_squared = (i0 - x0) ** 2 + (j0 - y0) ** 2
            if distance_squared < r ** 2:             
                sum_pixels_0 += S0_norm[i0,j0]
                count_pixels_0 += 1
    S1=norm_0-norm_90
    S1_norm=S1/S_avg_safe
    sum_pixels_1 = 0
    count_pixels_1 = 0
    for i0 in range(lenx_0):  
        for j0 in range(leny_0):
            distance_squared = (i0 - x0) ** 2 + (j0 - y0) ** 2
            if distance_squared < r ** 2:             
                sum_pixels_1 += S1_norm[i0,j0]
                count_pixels_1 += 1    
    
    
   
    
   
    
    
    return S1_norm
 