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
    os.chdir("C:/Users/Laboratorio/StokeMatix/CaptureHub/old/5.28cun")
    
        
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

    im_0=leftP[500:600,520:620] #(611-100/612+100) (654-200/655+200)
    im_45=leftP[1500:1600,520:620] #(1636-100/1637+100) (654-200/655+200)

    im_n45=rightP[500:600,520:620]
    im_90=rightP[1500:1600,520:620]

    norm_0=im_0/255.0
    
    norm_90=im_90/255.0
    
    norm_45=im_45/255.0
    
    norm_n45=im_n45/255.0
    
    
    s0_H_V=norm_0+norm_90
    
    s0_D_A=norm_45+norm_n45
    
    S0_avg=(norm_0+norm_90+norm_45+norm_n45)/2
    s0=S0_avg/S0_avg
    s1=(norm_0-norm_90)/S0_avg
    s2=(norm_45-norm_n45)/S0_avg
    
    
   
    
   
    
    
    return s1
 